#! /usr/bin/python

import staticjinja
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil
import markdown


class Site( staticjinja.Site ):
    # Override a few methods to customize to my settings.

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
    #Site.copy_static = copy_static

    # Only render templates if necessary (according to mtimes)
    def render_template( self, template, context=None, filepath=None):
	if context is None:
	    context = self.get_context(template)

	try:
	    rule = self.get_rule(template.name)
	except ValueError:
	    self._ensure_dir(template.name)
	    if filepath is None:
		filepath = os.path.join(self.outpath, template.name)
	    src = os.path.join( self.searchpath, template.name )

	    if self.options.force or not os.path.isfile( filepath ) or \
		    os.stat(src).st_mtime - os.stat(filepath).st_mtime > 1:
		self.logger.info("Rendering %s..." % template.name)
		template.stream(**context).dump(filepath, self.encoding)
	else:
	    rule(self, template, context, filepath)

    ignored_re = re.compile( '.*\.(?:swp|un~)$', flags=re.I )
    def is_ignored( self, f ):
	return True if self.ignored_re.match( f ) else False

    partial_re = re.compile( '(?:^|.*/)_' ) 
    def is_partial( self, f):
	return True if self.partial_re.match( f ) else False

    static_re  = re.compile(
	    'static/(?!.*\.(:?swp|un~)$)|.*\.(:?pdf|jpg|png|svg|eps|ps)$',
	    flags=re.I )
    def is_static( self, f ):
	return True if self.static_re.match( f ) else False

def markdown_get_context(template):
    """ Convert markdown to html and read into context variables """
    with open(template.filename) as f:
	md = markdown.Markdown( extensions=[
	    'markdown.extensions.extra',
	    'markdown.extensions.meta',
	    'markdown.extensions.sane_lists',
	    'markdown.extensions.smarty',
	    'markdown.extensions.toc'
	] )
	html = md.convert( f.read() )

	context = { 'content': html, 'toc':  md.toc }
	for key in md.Meta.keys():
	    val = md.Meta[key]
	    context[key] = val[0] if len( val ) == 1 else val
	return context


# compilation rule
def markdown_render(self, template, context=None, filepath=None):
    """Render a template as a post."""
    try:
	layout = context['meta']['layout']
    except:
	layout = ''
    layout = os.path.join( '_layouts', layout or "md-default.html")
    post_template = self.get_template(layout)

    self._ensure_dir( template.name )
    if filepath is None:
	filepath = os.path.join(self.outpath, template.name)
	(f, ext) = os.path.splitext( filepath )
	if ext == '.md':
	    filepath = f + '.html'
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

    pwd = os.path.dirname(os.path.realpath(__file__))
    if pwd == os.getcwd(): pwd = '.'

    site = staticjinja.make_site(
	    searchpath=pwd + '/src',
	    outpath=pwd + ('/out-prod' if options.production else '/out'),
	    extensions=[MarkdownExtension],
	    contexts=[
		('.*.md', markdown_get_context),
	    ],
	    rules=[
		('.*.md', markdown_render),
	    ],
	)
    # Type cast to my class
    site.__class__ = Site

    site.options = options
    site.args = args

    # Tweak the Jinja2 environment
    site._env.line_statement_prefix = '<@Jinja2>'
    site._env.globals['dev_env'] = \
	'production' if options.production else 'local'

    # enable automatic reloading
    site.render(use_reloader=False)
