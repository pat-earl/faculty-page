title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Getting Help", "file": "slides/chapter2.md"},
    {"name": "The Utilities", "file": "slides/chapter3.md"},
    {"name": "Files & Directories (PowerPoint)", "file": "slides/files.pptx"},
    {"name": "Command Presentations", "file": "slides/commands.md"},
    {"name": "The Shell", "file": "slides/shell.md"},
    {"name": "bash & Shell Scripting", "file": "slides/bash.md"}
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

