title: CSC223 - Lectures
breadcrumb: ./index.md

{% set lectures = (
    {"name": "Introduction", "file": "slides/introduction.md"},
    {"name": "Python Introduction", "file": "slides/python_intro.md"},
    {"name": "Python Data Types", "file": "slides/types.md"},
    {"name": "Python Control Structures" , "file": "slides/control.md"},
    {"name": "Python Functions", "file": "slides/functions.md"},
    {"name": "Python Input/Output", "file": "slides/io.md"},
    {"name": "Data Science File Formats", "file": "slides/file_formats.md"},
    {"name": "Python Errors & Exceptions", "file": "slides/errors.md"},
) %}


{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor %}
