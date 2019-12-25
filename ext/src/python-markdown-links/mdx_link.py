'''
WikiLinks Extension for Python-Markdown
======================================

Converts [[WikiLinks]] to relative links.

See <https://Python-Markdown.github.io/extensions/wikilinks>
for documentation.

Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright The Python Markdown Project

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

MonkeyPatched version:

    * allow [[link|label]] style links.
    * build_url now returns an ordered pair (link, label).
    * Add link_chars for allowed characters in links

'''

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
import markdown.extensions.wikilinks as wl
from markdown.util import etree
import re, os


def build_url(text, base, end):
    """ Build a url from the label, a base, and an end. """

    sep = text.find('|')
    if( sep >= 0 ):
        link = text[:sep]
        label = text[sep+1:]
    else:
        link = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', text)
        label = os.path.basename(text)

    return ( base + link + end, label)

class LinkExtension(Extension):
    def __init__ (self, *args, **kwargs):
        self.config = {
            'base_url' : ['/', 'String to append to beginning or URL.'],
            'end_url' : ['/', 'String to append to end of URL.'],
            'html_class' : ['wikilink', 'CSS hook. Leave blank for none.'],
            'link_chars' : [r'\w0-9|_ -', 'Allowed characters in a link.'],
            'build_url' : [build_url, 'Callable formats URL from text.'],
        }
        
        super(LinkExtension, self).__init__(*args, **kwargs)
    
    def extendMarkdown(self, md, md_globals):
        self.md = md
    
        # append to end of inline patterns
        WIKILINK_RE = r'\[\[([%s]+?)\]\]' % self.getConfig( 'link_chars' )
        wikilinkPattern = Links(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        md.inlinePatterns.add('wikilink', wikilinkPattern, "<not_strong")

class Links(wl.WikiLinksInlineProcessor):
    def handleMatch(self, m, data):
        if m.group(1).strip():
            base_url, end_url, html_class = self._getMeta()
            (url, label) = self.config['build_url']( m.group(1).strip(),
                    base_url, end_url)
            a = etree.Element('a')
            a.text = label 
            a.set('href', url)
            if html_class:
                a.set('class', html_class)
        else:
            a = ''
        return a, m.start(0), m.end(0)

def makeExtension(*args, **kwargs) :
    return LinkExtension(*args, **kwargs)
