#! /usr/bin/python

import staticjinja
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil
import markdown
import sys
import ConfigParser
from collections import namedtuple


pwd = os.path.dirname(os.path.realpath(__file__))
if pwd == os.getcwd(): pwd = '.'
sys.path.append( pwd + '/ext/python-markdown-math' )
sys.path.append( pwd + '/ext/python-markdown-links' )

# Local markdown extensions
import mdx_math
import mdx_link

def build_url( site, text, template=None ):
    """
        Build a url from the label text. First argument is a staticjinja Site
        to get globals (base, surl, etc.) from. If template is provided, then
        "auth/" links can be redirected to https as required by Shibboleth.
    """

    sep = text.find('|')
    if( sep >= 0 ):
        link = text[:sep]
        label = text[sep+1:]
    else:
        link = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', text)
        label = text

    g = site._env.globals
    if link.startswith( 'auth/' ) and template:
        link = os.path.join( g['site_surl'],
                os.path.dirname(template.name), link )
    elif link.startswith( '/' ):
        link = os.path.join( g['site_prefix'], link )

    (l, e) = os.path.splitext( link )
    if e == '.md':
        link = l + '.html'

    return ( link, label)

def convert_markdown( site, s, template=None ):
    """
        Convert a string (or list) into markdown

        site is an object of class Site. The _env.globals dict is used to
        build wiki_links using the [[ ... ]] syntax.
    """
    if type(s) == list:
        s = '\n'.join(s)

    if not hasattr( convert_markdown, 'md' ):
	convert_markdown.md = markdown.Markdown( extensions=[
	    'markdown.extensions.extra',
	    'markdown.extensions.codehilite',
	    'markdown.extensions.meta',
	    'markdown.extensions.sane_lists',
	    'markdown.extensions.smarty',
	    'markdown.extensions.toc',
	    mdx_math.MathExtension(enable_dollar_delimiter=True),
            mdx_link.makeExtension(
                link_chars = r'\w0-9|._ /-',
                build_url=lambda t, b, e: build_url( site, t,
                    template=template )
            )
	] )
        convert_markdown.md.set_output_format( 'html5' )

    md = convert_markdown.md
    md.reset()
    r = namedtuple( 'RenderedMarkdown', ['html', 'toc', 'Meta'])
    r.html = md.convert( s )
    r.toc = md.toc
    r.Meta = md.Meta
    for key in r.Meta.keys():
        val = r.Meta[key]
        if len( val ) == 1:
            r.Meta[key] = val[0]

    return r

class Site( staticjinja.Site ):
    # Override a few methods to customize to my settings.

    def get_context(self, template):
	"""
            Overridden:
                1. Allow Site as an argument to the context function
                2. Inject dirname, basename, etc into the context.
        """
        try:
            context_generator = self._get_context_generator(template.name)
        except ValueError:
            context = None
        else:
            try:
                context = context_generator( self, template)
            except TypeError:
		try:
		    context = context_generator( template)
		except TypeError:
		    context = context_generator()

        return inject_name_vars( self, template, context )

    # Only copy static files if necessary (according to mtimes)
    def copy_static( self, files):
	for f in files:
	    src = os.path.join(self.searchpath, f)
	    dst = os.path.join(self.outpath, f)
	    self._ensure_dir(f)
	    if not ( os.path.isfile(dst) or os.path.islink(dst) ) or \
		    ( os.stat(src).st_mtime - os.stat(dst).st_mtime > 0 ):
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

    def needs_rendering( self, template, filepath=None ):
	src = os.path.join( self.searchpath, template.name )
	if filepath is None:
	    filepath = os.path.join(self.outpath, template.name)

	if self.options.force or not os.path.isfile( filepath ) or \
		os.stat(src).st_mtime - os.stat(filepath).st_mtime > 1:
	    return filepath
	else:
	    return None

    # Only render templates if necessary (according to mtimes)
    def render_template( self, template, context=None, filepath=None):
	if context is None:
	    context = self.get_context(template)

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

def get_out_filename( site, src, out_ext='.html' ):
    " Add the out_ext"
    filepath = os.path.join(site.outpath, src)
    (f, ext) = os.path.splitext( filepath )
	 
    return f + out_ext

def inject_name_vars( self, template, context ):
    if context == None:
        context = {}
    context.update( {
        'name': template.name,
        'dirname': os.path.dirname( template.name ),
        'basename': os.path.basename( template.name )
    })
    return context

def markdown_get_context( self, template):
    """ Convert markdown to html and read into context variables """

    dst = get_out_filename( self, template.name )
    if not self.needs_rendering( template, dst ):
	return None

    if not hasattr( markdown_get_context, 'mathre' ):
	markdown_get_context.mathre = re.compile(
		'.*<script\\s*type\\s*=\s*[\'"]math/tex(\\s|[\'";])',
		re.DOTALL )
    mathre = markdown_get_context.mathre

    # Directly convert to markdown
    #f = open(template.filename):
    #    md = convert_markdown( f.read() )

    # Read until the first blank line to get the meta-data
    meta = ""
    with open(template.filename) as f:
        while True:
            l = f.readline()
            meta += l
            if not l.strip(): break

    # Should have meta-data segment in meta to use for context.
    md = convert_markdown( self, meta, template=template )
    context = inject_name_vars( self, template, md.Meta )

    # Now convert the whole document, using the meta-data as context
    md = convert_markdown( self, template.render(**context), template=template )

    context = {
        'content': md.html,
        'toc': md.toc,
    }
    if mathre.match( md.html ):
        context['needs_mathjax'] = 1
    context.update( md.Meta )
    
    return context

# compilation rule
def markdown_render(self, template, context=None, filepath=None):
    """Render a template as a post."""
    try:
	layout = context['layout']
    except:
        if( template.name.startswith( "blog" ) ):
            layout = 'md-blogpost.j2'
        elif re.match( r'teaching\/[0-9-]+\/[0-9a-z-]+\/index\.md', template.name ):
            layout = 'md-class.j2'
        else:
            layout = 'md-default.j2'
        
    layout = os.path.join( 'layouts', layout )
    post_template = self.get_template(layout)

    if filepath is None:
	filepath = get_out_filename( self, template.name )
    self._ensure_dir( template.name )
    src = os.path.join( self.searchpath, template.name )

    if self.options.force or not os.path.isfile( filepath ) or \
	    os.stat(src).st_mtime - os.stat(filepath).st_mtime > 1:
	self.logger.info("Rendering %s..." % template.name)
	post_template.stream(**context).dump( filepath, self.encoding)


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
		('.*\.md', markdown_get_context),
	    ],
	    rules=[
		('.*\.md', markdown_render),
	    ],
	)
    # Type cast to my class
    site.__class__ = Site

    site.options = options
    site.args = args

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
    
    site._env.globals['markdown'] = lambda s: convert_markdown( site, s).html
    site._env.filters['markdown'] = site._env.globals['markdown']

    # enable automatic reloading
    site.render(use_reloader=False)
