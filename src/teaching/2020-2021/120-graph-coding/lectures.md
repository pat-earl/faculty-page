title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Chapters 2 & 3", "file": "slides/2_and_3.md"},
    {"name": "Chapter 4: Variables", "file": "slides/variables.md"},
    {"name": "Chapter 5: Conditionals", "file": "slides/conditionals.md"},
    {"name": "Chapter 14: Translation & 3D", "file": "slides/translation.md"},
    {"name": "Chapter 6: Loops", "file": "slides/loops.md"},
    {"name": "Chapter 7: Functions", "file": "slides/functions.md"},
    {"name": "Chapter 8: Objects", "file": "slides/objects.md"},
    {"name": "Chapter 9: Arrays", "file": "slides/arrays.md"},
    {"name": "Chapter 17: Text", "file": "slides/strings.md"},
    {"name": "Chapter 10: Algorithms", "file": "slides/algorithms.md"},
    {"name": "Chapters 11 & 12", "file": "slides/debugging.md"},
    {"name": "Chapters 13: Mathematics", "file": "slides/mathematics.md"},
    {"name": "Chapters 15: Images", "file": "slides/images.md"},
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Marked up Versions

Lecture slides may be annotated during the course. Saved versions will be posted
below when they become available.

* Week 1
    - 1-19
        - [Lecture](./pdfs/intro.pdf) 
        - [Graphical Planes](./pdfs/graphical-planes.pdf)
* Week 2
    - [Variables Lecture](./pdfs/variables-full.pdf)