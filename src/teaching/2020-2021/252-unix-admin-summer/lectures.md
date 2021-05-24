title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Getting Help", "file": "slides/chapter2.md"},
    {"name": "The Utilities", "file": "slides/chapter3.md"},
    {"name": "The Shells", "file": "slides/shell.md"},
    {"name": "Filesystem", "file": "slides/chapter4.md"},
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}

