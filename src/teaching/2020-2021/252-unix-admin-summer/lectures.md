title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Getting Help", "file": "slides/chapter2.md"},
    {"name": "The Utilities", "file": "slides/chapter3.md"},
    {"name": "The Shells", "file": "slides/shell.md"},
    {"name": "Filesystem (PowerPoint)", "file": "slides/files.pptx"},
    {"name": "The BASH Shell & Scripting", "file": "slides/bash.md"},
    {"name": "UNIX Processes", "file": "slides/processes.md"},
    {"name": "System Administration", "file": "slides/sysadmin.md"},
    {"name": "Text Processing", "file": "slides/text_processing.md"},
    {"name": "Python", "file": "slides/python.md"}
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor -%}

