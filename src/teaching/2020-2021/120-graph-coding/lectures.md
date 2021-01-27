title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Chapters 2 & 3", "file": "slides/2_and_3.md"},
    {"name": "Chapter 4: Variables", "file": "slides/variables.md"}
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures %}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Marked up Versions

Lecture slides may be annotated during the course. Saved versions will be posted
below when they become available.

* Week 1
    * 1-19
        - [Lecture](./pdfs/intro.pdf) 
        - [Graphical Planes](./pdfs/graphical-planes.pdf)

* Week 2