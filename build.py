#! /usr/bin/python

from staticjinja import make_site
from jinja2_markdown import MarkdownExtension
import re
import optparse
import os

if __name__ == "__main__":

    # Options.
    parser = optparse.OptionParser()

    # Use -p for production. The global dev_env is set to 'local' or
    # 'production' respectively.
    parser.add_option( '-p', '--production', dest='production',
	    action='store_true', help='Generate site for production' )

    ( options, args ) = parser.parse_args()

    site = make_site(
	    searchpath='./src',
	    outpath='./out-prod' if options.production else './out',
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

    # enable automatic reloading
    site.render(use_reloader=False)
