#! /usr/bin/python

import staticjinja
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil
import ConfigParser
import fnmatch
import glob
import subprocess

from stat import *

from jinja2 import contextfunction, contextfilter

import mdconverter

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
            #print e
            try:
                context = context_generator( template)
            except TypeError:
                context = context_generator()

    return site.inject_name_vars( context, template )

# Callable python functions / filters
def jinja_search( s, pat ):
    if type(s) == str or type(s) == unicode:
        return True if re.search( pat, s ) else False
    elif type(s) == list:
        return [ e for e in s if re.search( pat, e )]

def jinja_sub( s, pat, rep, count=0 ):
    if type(s) == str or type(s) == unicode:
        return re.sub( pat, rep, s, count )
    else:
        return [ re.sub( pat, rep, e, count ) for e in s ]

def jinja_test( site, context, arg ):
    print site.searchpath
    print context['dirname']
    return arg

def jinja_glob( site, context, pat ):
    """
    Return all glob pattern matches in the SOURCE directory
    """
    
    leading_slash = '/' if pat[0] == '/' else ''
    (pat, cdir) = site.get_cdir( context, pat )
    matches = glob.glob( os.path.join( cdir, pat ) )
    return [ leading_slash + os.path.relpath( m, cdir ) for m in matches ]

def remove_extra_static( site ):
    """
    Remove static files in outpath that are no longer present in searchpath
    """
    p = os.path
    for (root, dirs, files) in os.walk( site.outpath ):
        for f in files:
            name = p.relpath( p.join( root, f ), site.outpath )
            if site.is_static(name) and \
                    not p.exists( p.join( site.searchpath, name ) ):
                fn = p.join( root, f )
                site.logger.warn( 'Removed extra static file %s' % fn )
                os.unlink( fn )

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
        p = os.path
        context.update( {
            'name': template.name,
            'dirname': p.dirname( template.name ),
            'basename': p.basename( template.name ),
            'filesdir': p.splitext( p.basename( template.name ) )[0],
        })
        return context

    def get_cdir( self, context, filename ):
        """
        Get the "current directory" of filename. If filename starts with '/',
        it is stripped, and cdir is site.searchpath. If not, cdir is
        site.searchpath / context['dirname']
        """

        if filename.startswith( '/' ):
            filename = filename[1:]
            cdir = self.searchpath
        else:
            cdir = os.path.join( site.searchpath, context['dirname'] )
            
        return (filename, cdir)

    # Overridden methods a few methods to customize to my settings.
    def copy_static( self, files):
        """
        Copy static files over, only if required by comparing mtimes or ctimes.
        For sym-links, copy it as a link.
        """
        p = os.path
	for f in files:
	    src = p.join(self.searchpath, f)
	    dst = p.join(self.outpath, f)
	    self._ensure_dir(f)
	    if not ( p.isfile(dst) or p.islink(dst) ) or \
		    ( os.stat(src).st_mtime - os.stat(dst).st_mtime > 0 ) or \
		    ( os.stat(src).st_ctime - os.stat(dst).st_ctime > 0 ):
		self.logger.info("Copying %s to %s." % (f, dst))
		#shutil.copyfile(src, dst)
                if p.islink(src):
                    if p.islink(dst):
                        os.unlink(dst)
                    elif p.isdir(dst):
                        shutil.rmtree(dst)

                    # Check if link is relative inside the source tree
                    rsrc = p.relpath( p.realpath( src ), self.searchpath )
                    if rsrc.startswith( '..' ) or rsrc.startswith( '/' ):
                        # External. Copy it.
                        shutil.copy( src, dst )
                        shutil.copymode( src, dst )
                    else:
                        linkto = os.readlink(src)
                        os.symlink( linkto, dst )
                else:
                    shutil.copy(src, dst)
                    shutil.copymode(src, dst)

                if not p.islink(dst):
                    # Make sure it's readable
                    m = os.stat(dst).st_mode
                    if not S_IRUSR & m or not S_IRGRP & m or not S_IROTH & m:
                        self.logger.warn( 'WARNING: making %s readable' % dst )
                        os.chmod( dst, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH )

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
                shutil.copymode( template.filename, filepath )
	else:
	    rule(self, template, context, filepath)

    ignored_re = re.compile( r'\.(?:swp|un~)$', flags=re.I )
    def is_ignored( self, f ):
	return True if self.ignored_re.search( f ) else False

    partial_re = re.compile( '(?:^|/)_|\.j2$' ) 
    def is_partial( self, f):
	return True if self.partial_re.search( f ) else False

    static_re  = re.compile(
	    '(?:^|/)static/|\.(:?pdf|jpg|png|svg|eps|ps|txt|sty)$',
	    flags=re.I )
    def is_static( self, f ):
        if not self.is_ignored(f) and self.static_re.search( f ):
            return True
        else:
            return False


if __name__ == "__main__":
    # Options.
    parser = optparse.OptionParser()

    # Use -p for production. The global dev_env is set to 'local' or
    # 'production' respectively.
    parser.add_option( '-p', '--production', dest='production',
	    action='store_true', help='Generate site for production' )
    parser.add_option( '-f', '--force', dest='force',
	    action='store_true', help='Render even if source is unchanged' )
    parser.add_option( '-u', '--upload', dest='upload',
	    action='store_true', help='Upload after rendering (implies -p)' )

    ( options, args ) = parser.parse_args()
    if options.upload: options.production = True

    pwd = os.path.dirname(os.path.realpath(__file__))
    site = staticjinja.make_site(
	    searchpath=os.path.join( pwd, 'src' ),
	    outpath=os.path.join( pwd,
                'out-prod' if options.production else 'out'),
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

    # Ensure output directory exists
    site._ensure_dir( os.path.join( site.outpath, 'index.html' ) )


    # Add in the markdown converter
    site.md = mdconverter.mdconverter( site )

    glob_re = re.compile( r'[*?{[]' )
    site.options = options
    site.args = [(a if glob_re.search(a) else '*'+a+'*') for a in args]

    if options.production:
        site.ignored_re = re.compile( '(?:^|/)dev/|' + site.ignored_re.pattern )
        dev_env = 'production'

    else:
        dev_env = 'local'

    # Read configuration
    cfg = ConfigParser.ConfigParser()
    cfg.read( os.path.join( pwd, 'site.cfg' ) )

    # Tweak the Jinja2 environment
    #site._env.line_statement_prefix = '<@Jinja2>'
    site._env.globals['dev_env'] = dev_env
    site._env.globals.update( dict( cfg.items('common') ) )
    site._env.globals.update( dict( cfg.items(dev_env) ) )
    
    site._env.globals.update({
        'markdown': contextfunction( lambda c, s: site.md.mdconvert(c, s).html ),
        'glob': contextfunction( lambda c, p: jinja_glob( site, c, p) ),
        'get_meta': contextfunction( lambda c, f, k=None: \
                        site.md.jinja_get_meta( c, f, k ) ),
        'get_file': contextfunction( lambda c, f: site.md.get_file(c, f) ),
        'get_link': contextfunction(
            lambda c, f, rel=False: site.md.get_link(c, f, rel) ),
        'search': jinja_search,
        'sub': jinja_sub,
    })
    site._env.filters.update({
        'markdown': contextfilter( lambda c, s: site.md.mdconvert(c, s).html ),
        'search': jinja_search,
        'sub': jinja_sub,
    })

    # enable automatic reloading
    site.render(use_reloader=False)

    # Delete extra static files in site
    remove_extra_static( site )

    # Upload if asked
    if options.upload:
        os.chdir( pwd )
        subprocess.call( cfg.get( 'production', 'upload' ), shell=True )
