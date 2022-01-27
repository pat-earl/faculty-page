title: Lectures
breadcrumb: ./index.md

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "General Information", "file": "slides/basic_commands.md"},
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}

