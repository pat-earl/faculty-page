{% from 'includes/macros.j2' import glyph -%}
title: Local Extensions and site specific details
breadcrumb: /{{dirname}}.md

A general markdown cheat sheet can be found [[markdown.md|here]].
This file only documents site specific quirks and extensions.

## Math

LaTeX can be used between `$` signs:

* `$E = mc^2$`  renders to $E = mc^2$.

* Displayed equations can be done with `$$`
  $$
    \frac{1}{2 \pi i} \oint \frac{ f(z) }{\zeta - z} \, dz = f(\zeta)
  $$

* Labeled equations using `\begin{equation}` etc. environments:
  \begin{equation}\label{eq1}
    -\lap u = 0 \quad\text{in } \Omega
  \end{equation}
  can be referred to using `\eqref{eq1}`: \eqref{eq1}.

## WikiLinks

* `[[file]]` generates a link to `file`.
* To specify the link text use `[[/index.html|Test]]`, which links to `/index.html` and says `Test`.
  This renders like this: [[/index.html|Test]]
* For `markdown` files, an extension of `.md` is replaced with `.html`.
  Also, if the link text is omitted the title of the linked file is used instead.
  E.g. `[[markdown.md]]` renders like this: [[markdown.md]].
* Links beginning with `/` will be prefixed with `site_prefix`.
* Broken links will generate a warning. E.g.: [[broken]]
* Links beginning with `auth/` will be redirected to `https://site_surl/dirname/auth/...`.
  (This is to avoid Shibboleth woes.)

## Jinja2 commands

All markdown files are rendered by `Jinja2` before being passed to a
`python-markdown`.
All `Jinja2` commands need to be escaped accordingly.

* `{{'{{title}}'}}` renders as `{{title}}`

* `{{'{{1 + 1}}'}}` renders as `{{1 + 1}}`

* `{{'{{ markdown("*hello*") }}'}}` expands to `{{ markdown("*hello*") }}`.

* Mark a block as raw using

        {{'{% raw %}'}}
        {% raw -%}
        Raw block. No Jinja commands will work here.
        {{ 1 + a }} {% hello %} world
        {%- endraw %}
        {{'{% endraw %}'}}

* Alternately, escape using `{{"{{'{{'}}"}}`.

## Metadata

* All markdown files have a YAML metadata block at the top (until the first newline).
  A few fields used in the current layouts are:
    * `title`: Document title
    * `breadcrumb`: List of navigation breadcrumbs.
    * `summary`: Summary of file (used in the index).
    * `tags`: Tags. Listed in the index, but nothing fancy is done as of now.
    * `layout`: Change the default template layout.
    * `comments`: Set to `disabled` disable comments (see [below](#comments)).

* Metadata from a file can be accessed using the function `get_meta( file_name, field)`.

## Variables and Globbing

* A few variables are injected into the Jinja2 context, and can be accessed in Jinja2 commands:
    * `name`: Path of the markdown file (e.g. `{{name}}`)
    * `dirname`: Path of directory containing current file (e.g. `{{dirname}}`)
    * `basename`: Name of markdown file (e.g. `{{basename}}`).
    * `filesdir`: Name of markdown file with extension stripped (e.g. `{{filesdir}}`). This can be used as a directory to store images, etc.
    * Anything defined in the `site.cfg`.

* A list of files can be generated using the `glob` function.
  For instance, the following will list the 5 most recent markdown files in the current directory and their titles:

        {% raw -%}
        {% set files = glob( '/blog/[0-9]*.md' ) | sort( reverse=True ) -%}
        {% for f in files[:5] -%}
        * File: {{f}}. Title: {{get_meta( f, 'title' )}}
        {% endfor %}
        {%- endraw %}

## Comments

Comments require a CGI script on the server.
This script simply takes the contents of the comment, and mails it to the webmaster as a mime attachment.
If you decide its not spam, save it (with the recommended filename) in the directory `blog/_comments` and it will appear on the right post.

If you want comments disabled use the `comments: disabled` field in the YAML meta data.

## Side panel navigation

* By default markdown files have the layout `md-default.j2` which links to `md-right-nav-affix.j2`.
  This shows the table of contents on the right on large screens, which highlights the current section and sticks to the top of the window.
  (Look [[layout.md|here]] for more information on the laoyts.)

* The layout can be changed using

        layout:  md-right-nav.j2

    as meta-data.

* The contents of `_sidenav.md` in the same directory is included below the table of contents in some layouts.

* For class pages (using `md-class.j2` layout) contents of `_hw.md` and `_handouts.md` are used in the side panel navigation.

## Macros

Various custom macros are in the `includes/macros.j2` file and can be used in markdown documents.
A few are listed here.

glyph:
: generates a glyph from [here](https://getbootstrap.com/docs/3.3/components/#glyphicons). E.g. `{{'{{glyph("thumbs-up")}}'}}` renders as {{glyph("thumbs-up")}}.

course_info_table:
: Makes a table with course information taken from the keys in the meta-data (e.g. [[/teaching/2015-16/268-multid-calc|here]].)

pubs:
: Generates a publication list (e.g. [[/|here]]).
