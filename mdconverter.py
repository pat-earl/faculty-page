#! /usr/bin/python
import markdown
import os
import sys
import re
from collections import namedtuple

pwd = os.path.dirname(os.path.realpath(__file__))
#if pwd == os.getcwd(): pwd = '.'
sys.path.append( pwd + '/ext/python-markdown-math' )
sys.path.append( pwd + '/ext/python-markdown-links' )

import mdx_math
import mdx_link

class mdconverter:
    def __init__(self, site):
        """
        site is a staticjinja Site object from which URL prefixes etc are extracted.
        """
        self.site = site
        self.current_template = None
        self.md = markdown.Markdown( extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.meta',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.toc',
            mdx_math.MathExtension(enable_dollar_delimiter=True),
            mdx_link.makeExtension(
                link_chars = r'\w0-9|:._ (),/-',
                build_url=lambda t, b, e: self.build_url( t )
            )
        ] )
        self.md.set_output_format( 'html5' )
        self.math_re = re.compile(
                '<script\\s*type\\s*=\s*[\'"]math/tex(\\s|[\'";])',
                re.DOTALL )

        # meta[md_file] holds data from the yaml block in md_file
        self.meta = {}

    def build_url( self, text ):
        """
            Build a url from the label text. If template is provided, then
            "auth/" links can be redirected to https as required by Shibboleth.
        """

        sep = text.find('|')
        if( sep >= 0 ):
            link = text[:sep]
            label = text[sep+1:]
        else:
            link = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', text)
            label = text

        g = self.site._env.globals
        if link.startswith( 'auth/' ) and self.current_template:
            link = os.path.join( g['site_surl'],
                    os.path.dirname(self.current_template.name), link )
        elif link.startswith( '/' ):
            link = os.path.join( g['site_prefix'], link )

        (l, e) = os.path.splitext( link )
        if e == '.md':
            link = l + '.html'

        return ( link, label)

    def mdconvert( self, s, current_template=None):
        """
            Convert a string (or list) into markdown
        """
        if type(s) == list:
            s = '\n'.join(s)

        self.md.reset()
        self.current_template = current_template
        r = namedtuple( 'RenderedMarkdown', ['html', 'toc', 'Meta'])

        r.html = self.md.convert( s )

        r.toc = self.md.toc
        r.Meta = self.md.Meta
        for key in r.Meta.keys():
            val = r.Meta[key]
            if len( val ) == 1:
                r.Meta[key] = val[0]

        return r

    def read_yaml_meta( self, filename ):
        """
        Read markdown metadata from filename.

        Note: This doesn't process the file through Jinja2 first. So the
        metadata has to be a simple yaml block that is understood by the
        markdown parser.
        """

        if not self.meta.has_key( filename ):
            # Read until the first blank line to get the meta-data
            meta = ""
            with open(filename) as f:
                while True:
                    l = f.readline()
                    meta += l
                    if not l.strip(): break

            self.meta[filename] = self.mdconvert( meta ).Meta
        return self.meta[filename]

    def jinja_get_meta( self, filename, key=None):
        """
        Return value of "key" in the yaml block in the markdown file "fn"
        """
        meta = self.read_yaml_meta( filename )
        if key:
            return self.meta[filename][key] if self.meta[filename].has_key(key) \
                else None
        else:
            return meta

# Was markdown_render
def render(site, template, context=None, filepath=None):
    """Render a markdown file."""
    if filepath is None:
        filepath = site.get_out_filename( template.name )
    if not site.needs_rendering( template, filepath ):
        return

    site.logger.info("Rendering %s..." % template.name)

    try:
        layout = context['layout']
    except:
        if( template.name.startswith( "blog" ) ):
            layout = 'md-blogpost.j2'
        elif re.match( r'teaching\/[0-9-]+\/[0-9a-z-]+\/.*\.md', template.name ):
            layout = 'md-class.j2'
        else:
            layout = 'md-default.j2'

    layout = os.path.join( 'layouts', layout )
    post_template = site.get_template(layout)

    site._ensure_dir( template.name )
    post_template.stream(**context).dump( filepath, site.encoding)

# was markdown_get_context
def get_context( site, template):
    """ Convert markdown to html and read into context variables """

    dst = site.get_out_filename( template.name )
    if not site.needs_rendering( template, dst ):
        return None

    # Directly convert to markdown
    #f = open(template.filename):
    #    md = site.md.convert( f.read() )

    context = site.inject_name_vars(
            site.md.read_yaml_meta( template.filename ), template )
    md = site.md.mdconvert( template.render(**context),
            current_template=template )

    context.update({
        'content': md.html,
        'toc': md.toc,
    })
    if site.md.math_re.search( md.html ):
        context['needs_mathjax'] = 1

    # In case template.render() caused the yaml block to change, update the
    # metadata again.
    context.update( md.Meta )
    
    return context
