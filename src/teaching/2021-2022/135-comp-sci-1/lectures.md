title: CSC135 - Lectures
breadcrumb: index.md

{% set lectures = (
    {"name": "Chapter 1 - Introduction", "file": "slides/ch01.pdf"},
    {"name": "Chapter 2 - Elements of C++", "file": "slides/ch02.pdf"},
    {"name": "Chapter 3 - Input/Output ", "file": "slides/ch03.pdf"},
    {"name": "Chapter 4 - Selection (If/Switch)", "file": "slides/ch04.pdf"},
    {"name": "Chapter 5 - Repetition (While/For/Do While)", "file": "slides/ch05.pdf"},
    {"name": "Chapter 6 - Functions", "file": "slides/ch06.pdf"},
    {"name": "Chapter 7 - User-Defined Types, Namespaces, and String", "file": "slides/ch07.pdf"},
    {"name": "Chapter 8 - Strings & Arrays", "file": "slides/ch08.pdf"}
) %}

## Course Lectures

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}

## Other Materials
* [Program Trace]({{ get_link('slides/tracing_10_19_21.pdf') }}) - From Thursday Oct. 10 Class