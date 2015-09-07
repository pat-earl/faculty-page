#! /usr/bin/python

import staticjinja
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil
import sys
import ConfigParser
import fnmatch
import glob

import mdconverter


pwd = os.path.dirname(os.path.realpath(__file__))
#if pwd == os.getcwd(): pwd = '.'
sys.path.append( pwd + '/ext/python-markdown-math' )
sys.path.append( pwd + '/ext/python-markdown-links' )

def get_context(site, template):
    """
    My custom get_context function (to replace Site.get_context). Rewritten to:
        1. Allow Site as an argument to the context function
        2. Inject dirname, basename, etc into the context.
    """
    try:
        context_generator = site._get_context_generator(template.name)
    except ValueError:
        context = None
    else:
        try:
            context = context_generator( site, template)
        except TypeError as e:
            try:
                context = context_generator( template)
            except TypeError:
                context = context_generator()

    return site.inject_name_vars( context, template )

class Site( staticjinja.Site ):
    # New methods
    def needs_rendering( self, template, filepath=None ):
        """
        Decide whether a template needs rendering.
        """
        src = os.path.join( self.searchpath, template.name )
        if filepath is None:
            filepath = os.path.join(self.outpath, template.name)

        if self.recompile_forced( filepath ) or not os.path.isfile( filepath ) or \
                os.stat(src).st_mtime - os.stat(filepath).st_mtime > 0:
            return filepath
        else:
            return None

    def recompile_forced( self, filename ):
        options = self.options

        if options.force:
            return True
        elif self.args:
            for i in self.args:
                if fnmatch.fnmatch( filename, i ):
                    return True

        return False

    def get_out_filename( self, src, out_ext='.html' ):
        " Add the out_ext"
        filepath = os.path.join(self.outpath, src)
        (f, ext) = os.path.splitext( filepath )
             
        return f + out_ext

    def inject_name_vars( self, context, template ):
        if context == None:
            context = {}
        context.update( {
            'name': template.name,
            'dirname': os.path.dirname( template.name ),
            'basename': os.path.basename( template.name )
        })
        return context


    # Overridden methods a few methods to customize to my settings.
    def copy_static( self, files):
        """
        Copy static files over, only if required by comparing mtimes or ctimes.
        For sym-links, copy it as a link.
        """
	for f in files:
	    src = os.path.join(self.searchpath, f)
	    dst = os.path.join(self.outpath, f)
	    self._ensure_dir(f)
	    if not ( os.path.isfile(dst) or os.path.islink(dst) ) or \
		    ( os.stat(src).st_mtime - os.stat(dst).st_mtime > 0 ) or \
		    ( os.stat(src).st_ctime - os.stat(dst).st_ctime > 0 ):
		self.logger.info("Copying %s to %s." % (f, dst))
		#shutil.copyfile(src, dst)
                if os.path.islink(src):
                    if os.path.islink(dst):
                        os.unlink(dst)
                    linkto = os.readlink(src)
                    os.symlink( linkto, dst )
                else:
                    shutil.copy(src, dst)
                    shutil.copymode(src, dst)

    def render_template( self, template, context=None, filepath=None):
        """
        Overrides site.render_template. This version calls my custom
        get_context (note site.get_context), and only renders templates if the
        need rendering based on mtimes.
        """
	if context is None:
	    context = get_context( self, template)

	try:
	    rule = self.get_rule(template.name)
	except ValueError:
	    self._ensure_dir(template.name)

	    filepath = self.needs_rendering( template, filepath )
	    if filepath:
		self.logger.info("Rendering %s..." % template.name)
		template.stream(**context).dump(filepath, self.encoding)
	else:
	    rule(self, template, context, filepath)

    ignored_re = re.compile( r'.*\.(?:swp|un~)$', flags=re.I )
    def is_ignored( self, f ):
	return True if self.ignored_re.match( f ) else False

    partial_re = re.compile( '(?:^|.*/)_|.*\.j2$' ) 
    def is_partial( self, f):
	return True if self.partial_re.match( f ) else False

    static_re  = re.compile(
	    '(?:(?:.*/)?static/(?!.*\.(:?swp|un~)$)|.*\.(:?pdf|jpg|png|svg|eps|ps)$)',
	    flags=re.I )
    def is_static( self, f ):
	return True if self.static_re.match( f ) else False


if __name__ == "__main__":
    # Options.
    parser = optparse.OptionParser()

    # Use -p for production. The global dev_env is set to 'local' or
    # 'production' respectively.
    parser.add_option( '-p', '--production', dest='production',
	    action='store_true', help='Generate site for production' )
    parser.add_option( '-f', '--force', dest='force',
	    action='store_true', help='Render even if source is unchanged' )

    ( options, args ) = parser.parse_args()

    site = staticjinja.make_site(
	    searchpath=pwd + '/src',
	    outpath=pwd + ('/out-prod' if options.production else '/out'),
	    extensions=[MarkdownExtension],
	    contexts=[
		('.*\.md', mdconverter.get_context),
	    ],
	    rules=[
		('.*\.md', mdconverter.render),
	    ],
	)
    # Type cast to my class
    site.__class__ = Site

    # Add in the markdown converter
    site.md = mdconverter.mdconverter( site )

    glob_re = re.compile( r'.*[*?{[]' )
    site.options = options
    site.args = [(a if glob_re.match(a) else '*'+a+'*') for a in args]

    if options.production:
        site.ignored_re = re.compile( 'dev|' + site.ignored_re.pattern )
        site.static_re = re.compile( '(?!dev)' + site.static_re.pattern )
        dev_env = 'production'

    else:
        dev_env = 'local'

    # Read configuration
    cfg = ConfigParser.ConfigParser()
    cfg.read( pwd + '/site.cfg' )

    # Tweak the Jinja2 environment
    #site._env.line_statement_prefix = '<@Jinja2>'
    site._env.globals['dev_env'] = dev_env
    site._env.globals.update( dict( cfg.items('common') ) )
    site._env.globals.update( dict( cfg.items(dev_env) ) )
    
    site._env.globals.update({
        'markdown': lambda s: site.md.mdconvert(s).html,
        'glob': glob.glob
    })
    site._env.filters['markdown'] = site._env.globals['markdown']

    # enable automatic reloading
    site.render(use_reloader=False)
