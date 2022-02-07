title: CSC252 - Lectures
breadcrumb: ./index.md

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "General Information", "file": "slides/basic_commands.md"},
    {"name": "Filesystem", "file": "slides/filesystem.md"},
) %}

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}

