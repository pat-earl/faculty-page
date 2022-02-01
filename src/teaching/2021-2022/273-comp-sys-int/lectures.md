title: CSC273 - Lectures
breadcrumb: index.md

{% set lectures = (
    {"name": "Course Introduction", "file": "slides/introduction.md"},
    {"name": "Chapter 1 - SDLC", "file": "slides/chapter1.pdf"},
    {"name": "Chapter 2 - Origins of Software", "file": "slides/chapter2.pdf"}
) %}

## Course Lectures

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}
