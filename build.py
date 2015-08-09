#! /usr/bin/python

import staticjinja
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil
import markdown
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
if pwd == os.getcwd(): pwd = '.'
sys.path.append( pwd + '/ext/python-markdown-math' )

from mdx_math import MathExtension


class Site( staticjinja.Site ):
    # Override a few methods to customize to my settings.

    def get_context(self, template):
	"Overridden to allow Site as an argument to the context function"
        try:
            context_generator = self._get_context_generator(template.name)
        except ValueError:
            return {}
        else:
            try:
                return context_generator( self, template)
            except TypeError:
		try:
		    return context_generator( template)
		except TypeError:
		    return context_generator()

    # Only copy static files if necessary (according to mtimes)
    def copy_static( self, files):
	for f in files:
	    src = os.path.join(self.searchpath, f)
	    dst = os.path.join(self.outpath, f)
	    self._ensure_dir(f)
	    if not os.path.isfile(dst) or \
		    ( os.stat(src).st_mtime - os.stat(dst).st_mtime > 1 ):
		print("Copying %s to %s." % (f, dst))
		shutil.copyfile(src, dst)

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

def markdown_get_context( self, template):
    """ Convert markdown to html and read into context variables """
    dst = get_out_filename( self, template.name )
    if not self.needs_rendering( template, dst ):
	return None

    if not hasattr( markdown_get_context, 'md' ):
	markdown_get_context.md = markdown.Markdown( extensions=[
	    'markdown.extensions.extra',
	    'markdown.extensions.codehilite',
	    'markdown.extensions.meta',
	    'markdown.extensions.sane_lists',
	    'markdown.extensions.smarty',
	    'markdown.extensions.toc',
	    'markdown.extensions.wikilinks',
	    MathExtension(enable_dollar_delimiter=True)
	] )
	markdown_get_context.mathre = re.compile(
		'.*<script\\s*type\\s*=\s*[\'"]math/tex(\\s|[\'";])',
		re.DOTALL )

    with open(template.filename) as f:
	md = markdown_get_context.md
	mathre = markdown_get_context.mathre
	md.reset()
	html = md.convert( f.read() )

	context = { 'content': html, 'toc':  md.toc }
	if mathre.match( html ):
	    context['needs_mathjax'] = 1
	
	for key in md.Meta.keys():
	    val = md.Meta[key]
	    context[key] = val[0] if len( val ) == 1 else val
	return context

# compilation rule
def markdown_render(self, template, context=None, filepath=None):
    """Render a template as a post."""
    try:
	layout = context['layout']
    except:
        if( template.name.startswith( "blog" ) ):
            layout = 'md-blogpost.j2'
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

    # Tweak the Jinja2 environment
    site._env.line_statement_prefix = '<@Jinja2>'
    site._env.globals['dev_env'] = \
	'production' if options.production else 'local'

    # enable automatic reloading
    site.render(use_reloader=False)
