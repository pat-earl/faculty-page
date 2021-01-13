title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "UNIX History", "file": "slides/history.md"}
) %}

## Course Lectures

These are the lecture slides used in the course. You can view them in 
their slide form or as a "printable" PDF, with each slide on a separate page

{% for lec in lectures %}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }}) - [PDF Form]({{ get_link(lec['file']) ~ "?print-pdf"}})
{% endfor -%}

## Marked up Versions

Lecture slides may be annotated during the course. Saved version can be found below.