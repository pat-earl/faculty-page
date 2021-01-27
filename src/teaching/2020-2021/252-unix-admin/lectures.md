title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Chapter 2", "file": "slides/chapter2.md"},
    {"name": "Chapter 3", "file": "slides/chapter3.md"}
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures %}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Marked up Versions

Lecture slides may be annotated during the course. Saved versions will be posted
below when they become available.