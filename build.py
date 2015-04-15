#! /usr/bin/python

from staticjinja import make_site
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os
import shutil

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

    site = make_site(
	    searchpath=pwd + '/src',
	    outpath=pwd + ('/out-prod' if options.production else '/out'),
	    extensions=[MarkdownExtension],
	)

    # Tweak the Jinja2 environment
    site._env.line_statement_prefix = '<@Jinja2>'
    site._env.globals['dev_env'] = \
	'production' if options.production else 'local'

    ignored_re = re.compile( '.*\.(?:swp|un~)$', flags=re.I )
    site.is_ignored = lambda f: True if ignored_re.match( f ) else False

    partial_re = re.compile( '(?:^|.*/)_' ) 
    site.is_partial = lambda f: True if partial_re.match( f ) else False

    static_re  = re.compile(
	    'static/(?!.*\.(:?swp|un~)$)|.*\.(:?pdf|jpg|png|svg|eps|ps)$',
	    flags=re.I )
    site.is_static = lambda f: True if static_re.match( f ) else False

    # Only copy static files if necessary
    def copy_static(files):
	self = site
	for f in files:
	    src = os.path.join(self.searchpath, f)
	    dst = os.path.join(self.outpath, f)
	    self._ensure_dir(f)
	    if not os.path.isfile(dst) or \
		    ( os.stat(src).st_mtime - os.stat(dst).st_mtime > 1 ):
		print("Copying %s to %s." % (f, dst))
		shutil.copyfile(src, dst)
    site.copy_static = copy_static

    # Only render templates if necessary
    def render_template(template, context=None, filepath=None):
	self = site

        if context is None:
            context = self.get_context(template)

        try:
            rule = self.get_rule(template.name)
        except ValueError:
            self._ensure_dir(template.name)
            if filepath is None:
                filepath = os.path.join(self.outpath, template.name)
	    src = os.path.join( self.searchpath, template.name )

	    if options.force or not os.path.isfile( filepath ) or \
		    os.stat(src).st_mtime - os.stat(filepath).st_mtime > 1:
		self.logger.info("Rendering %s..." % template.name)
		template.stream(**context).dump(filepath, self.encoding)
        else:
	    self.logger.info("Rendering %s..." % template.name)
            rule(self, template, **context)
    site.render_template = render_template


    # enable automatic reloading
    site.render(use_reloader=False)
