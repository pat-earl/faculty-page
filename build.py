#! /usr/bin/python

from staticjinja import make_site
import re

from jinja2_markdown import MarkdownExtension

if __name__ == "__main__":
    partial_re = re.compile( '(?:^|.*/)_' ) 
    ignored_re = re.compile( '.*\.(?:swp|un~)$', flags=re.I )
    static_re  = re.compile(
	    'static/(?!.*\.(:?swp|un~)$)|.*\.(:?pdf|jpg|png|svg|eps|ps)$',
	    flags=re.I )

    def is_partial( filename ):
	return True if partial_re.match( filename ) else False

    def is_ignored( filename ):
	return True if ignored_re.match( filename ) else False

    def is_static( filename ):
	return True if static_re.match( filename ) else False

    site = make_site(
	    searchpath='./src',
	    outpath='./out',
	    extensions=[MarkdownExtension],
	)

    site._env.line_statement_prefix = '<@Jinja2>'
    site.is_ignored = is_ignored
    site.is_partial = is_partial
    site.is_static = is_static

    # enable automatic reloading
    site.render(use_reloader=False)
