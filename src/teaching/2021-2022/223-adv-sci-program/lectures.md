title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/introduction.md"},
    {"name": "Python Introduction", "file": "slides/python_intro.md"}
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor %}
