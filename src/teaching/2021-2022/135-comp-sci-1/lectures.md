title: CSC135 - Lectures
breadcrumb: index.md

{% set lectures = (
    {"name": "Chapter 1 - Introduction", "file": "slides/ch01.pdf"},
    {"name": "Chapter 2 - Elements of C++", "file": "slides/ch02.pdf"},
    {"name": "Chapter 3 - Input/Output ", "file": "slides/ch03.pdf"},
    {"name": "Chapter 4 - Selection", "file": "slides/ch04.pdf"},
    {"name": "Chapter 6 - Functions", "file": "slides/ch06.pdf"},
) %}

## Course Lectures

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}
