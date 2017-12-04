#! /usr/bin/python
import os, sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert( 1, os.path.join( pwd, 'ext' ) )

import re, shutil
from collections import namedtuple

import markdown
import markdown.extensions.headerid as mdx_headerid
import mdx_math, mdx_link

class mdconverter:
    def __init__(self, site):
        """
        site is a staticjinja Site object from which URL prefixes etc are extracted.
        """
        self.site = site
        self.current_context = None
        self.md = markdown.Markdown( extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.meta',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.toc',
            mdx_math.MathExtension(enable_dollar_delimiter=True),
            mdx_link.makeExtension(
                link_chars = r'][\w0-9|:._ (),/"-',
                build_url=lambda t, b, e: self.build_url( t )
            ),
        ] )
        self.md.set_output_format( 'html5' )

        self._md_meta = markdown.Markdown( extensions=[
            'markdown.extensions.meta'] )
        self._md_meta.set_output_format( 'html5' )

        self.math_re = re.compile(
                '<script\\s*type\\s*=\s*[\'"]math/tex(\\s|[\'";])',
                re.DOTALL )

        # meta[md_file] holds data from the yaml block in md_file
        self.meta = {}

    def path_exists( self, context, path ):
        (f, cdir) = self.site.get_cdir( context, path )
        if os.path.exists( os.path.join( cdir, f ) ):
            return self.get_file( context, path )
        else:
            return None

    def get_file( self, context, f ):
        """
        Get a path to file f. f can be relative to current directory (taken
        from context.dirname) or to the root directory (site.searchpath).
        """
        site = self.site

        (f, cdir) = site.get_cdir( context, f )

        return os.path.relpath( os.path.join( cdir, f ), site.searchpath )

    def get_link( self, context, f, rel=False ):
        """
        Get a link to file f. f can be relative to current directory (taken
        from context.dirname) or to the root directory (site.searchpath).
        """

        g = self.site._env.globals

        link = self.get_file( context, f )
        (l, e) = os.path.splitext( link )
        if e == '.md':
            link = l + '.html'

        if rel:
            return os.path.join( g['site_prefix'] or '/', link )
        elif re.search( '(?:^|/)auth/', link ):
            # Use https for all links with an auth in the URL.
            return os.path.join( g['site_surl'], link )
        else:
            return os.path.join( g['site_url'], link )

    def build_url( self, text ):
        """
        Build a url from text of the form "link|label". If no label is given,
        try and use the title of the file pointed to by link, or fall back to
        the given text.
        """

        sep = text.find('|')
        if( sep >= 0 ):
            link = text[:sep]
            label = text[sep+1:]
        else:
            link = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', text)
            label = os.path.basename(text)

        # Check if the path exists
        (f, cdir) = self.site.get_cdir( self.current_context, link )
        if not os.path.exists( os.path.join( cdir, f ) ):
            self.site.logger.warn( '%s WARNING: Broken link "%s"'
                    % (self.current_context['name'], link) )
        elif sep < 0:
            # Path exists and no label given.
            label = self.jinja_get_meta( self.current_context,
                        link, 'title' ) or label

        return ( self.get_link( self.current_context, link ), label)

    def mdconvert( self, context, s):
        """
            Convert a string (or list) into markdown. (context is used to get
            dirname etc, and pass to build_url when making links.)
        """
        if type(s) == list:
            s = '\n'.join(s)

        self.md.reset()
        self.current_context = context
        r = namedtuple( 'RenderedMarkdown', ['html', 'toc', 'Meta'])

        r.html = self.md.convert( s )

        r.toc = self.md.toc
        r.Meta = self.md.Meta
        for key in r.Meta.keys():
            val = r.Meta[key]
            if len( val ) == 1:
                r.Meta[key] = val[0]

        return r

    def read_yaml_meta( self, context, filename ):
        """
        Read markdown metadata from filename.

        Note: This doesn't process the file through Jinja2 first. So the
        metadata has to be a simple yaml block that is understood by the
        markdown parser.
        """

        p = os.path
        site = self.site

        (filename, cdir) = site.get_cdir( context, filename )

        real_fname = p.realpath( p.join( cdir, filename ) )
        rel_name = p.relpath( real_fname, site.searchpath )
        if not self.meta.has_key( rel_name ):
            # Read until the first blank line to get the meta-data
            meta = ""
            
            with open(real_fname) as f:
                while True:
                    l = f.readline()
                    meta += l
                    if not l.strip(): break

            # Convert meta to markdown, and read the metadata from the result
            self._md_meta.reset()
            self._md_meta.convert( meta )
            self.meta[rel_name] = \
                self._md_meta.Meta if hasattr( self._md_meta, 'Meta' ) else {}
            for key in self.meta[rel_name].keys():
                val = self.meta[rel_name][key]
                if len( val ) == 1:
                    self.meta[rel_name][key] = val[0]

        return self.meta[rel_name]

    def jinja_get_meta( self, context, filename, key=None):
        """
        Return value of "key" in the yaml block in the markdown file "fn"
        """
        meta = self.read_yaml_meta( context, filename )
        if key:
            return meta[key] if meta.has_key(key) else None
        else:
            return meta

# was site.inject_name_vars( context, template )
def get_name_vars( template ):
    p = os.path
    return {
        'name': template.name,
        'dirname': p.dirname( template.name ),
        'basename': p.basename( template.name ),
        'filesdir': p.splitext( p.basename( template.name ) )[0],
    }

# Was markdown_render
def render(site, template, **context):
    """Render a markdown file."""
    filepath = site.get_out_filename( template.name )
    if not site.needs_rendering( template, filepath ):
        return

    site.logger.info("Rendering %s..." % template.name)

    try:
        layout = context['layout']
    except:
        if( template.name.startswith( "blog" ) ):
            layout = 'md-blogpost.j2'
        elif re.match( r'teaching\/[0-9-]+\/[0-9a-z-]+\/.*\.md',
                template.name ):
            layout = 'md-class.j2'
        else:
            layout = 'md-default.j2'

    layout = os.path.join( 'layouts', layout )
    post_template = site.get_template(layout)

    site._ensure_dir( template.name )
    post_template.stream(**context).dump( filepath, site.encoding)
    shutil.copymode( template.filename, filepath )

# was markdown_get_context
def get_context( site, template):
    """ Convert markdown to html and read into context variables """

    dst = site.get_out_filename( template.name )
    if not site.needs_rendering( template, dst ):
        return {}

    # Directly convert to markdown
    #f = open(template.filename):
    #    md = site.md.convert( f.read() )

    context = get_name_vars( template )
    context.update(  site.md.read_yaml_meta( context, '/' + template.name ) )

    if context.has_key( 'raw' ) and context['raw']:
        # Don't render before passing to mdconvert
        # This still doesn't work perfectly. Better to surround document with
        # {% raw %} tags.
        with open(template.filename) as f:
            md = site.md.mdconvert( context, f.read() )
    else:
        md = site.md.mdconvert( context, template.render(**context) )

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

def slugify( s, sep='-' ):
    return mdx_headerid.slugify( unicode(s), sep )
