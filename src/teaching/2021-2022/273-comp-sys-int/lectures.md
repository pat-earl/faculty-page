title: CSC273 - Lectures
breadcrumb: index.md

{% set lectures = (
    {"name": "Course Introduction", "file": "slides/introduction.md"},
) %}

## Course Lectures

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}
