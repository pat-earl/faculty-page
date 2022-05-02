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
    {"name": "Python Modules", "file": "slides/modules.md"},
    {"name": "Python Iterators & List Comprehension", "file": "slides/list_and_iterators.md"},
    {"name": "NumPy Introduction", "file": "slides/numpy.md"},
    {"name": "Pandas - Types", "file": "slides/pandas_types.md"},
    {"name": "Matplotlib - Intro", "file": "slides/matplotlib.md"},
    {"name": "Statistics Review", "file": "slides/stats.md"},
    {"name": "Pandas - Multi-Index", "file": "slides/multi_index.md"},
    {"name": "Pandas - Combining Data", "file": "slides/combine.md"},
    {"name": "Pandas - Aggregation & Grouping", "file": "slides/agg.md"},
    {"name": "Pandas - Time-Series", "file": "slides/time.md"}
) %}


{% for lec in lectures -%}
* {{ lec['name'] }} - [Slides]({{ get_link(lec['file']) }})
{% endfor %}
