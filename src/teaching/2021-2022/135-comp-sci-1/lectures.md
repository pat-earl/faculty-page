title: CSC135 - Lectures

{% set lectures = (
    {"name": "Chapter 1 - Introduction", "file": "slides/ch01.pdf"},
    {"name": "Chapter 2 - Elements of C++", "file": "slides/ch02.pdf"},
    {"name": "Chapter 3 - Input/Output ", "file": "slides/ch03.pdf"},
) %}

## Course Lectures

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}
