title: Lectures
breadcrumb: ./index.md

{% set lectures = (
    {"name": "Introduction", "file": "slides/introduction.md"},
    {"name": "Python Introduction", "file": "slides/python_intro.md"},
    {"name": "Python Data Types", "file": "slides/types.md"},
    {"name": "Python Control Structures" , "file": "slides/control.md"},
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor %}
