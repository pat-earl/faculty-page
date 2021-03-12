title: Lectures

{% set lectures = (
    {"name": "Introduction", "file": "slides/intro.md"},
    {"name": "Python Types", "file": "slides/types.md"},
    {"name": "Python Control Flow", "file": "slides/control.md"},
    {"name": "Python Functions", "file": "slides/functions.md"},
    {"name": "Python Errors & Exceptions", "file": "slides/errors.md"},
    {"name": "Python Modules", "file": "slides/modules.md"},
    {"name": "Python Iterators", "file": "slides/iterators.md"},
    {"name": "NumPy", "file": "slides/numpy.md"},
    {"name": "Pandas - Data Types", "file": "slides/pandas_types.md"},
) %}

## Course Lectures

These are the lecture slides used in the course.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor %}

## Marked up Versions

Lecture slides may be annotated during the course. Saved versions will be posted
below when they become available.

* 1/22
    - Section 10:
        + [Annotated Slides](./pdfs/intro_10.pdf)
        + [Zoom Recording for using Anaconda Python](https://kutztown.zoom.us/rec/play/fIrQb2tFORPFvK3sxl_kBQ2T2HBRdqJlilAor_uwHWf3YakpRWP7qybFg89T86emxWSjkuo7nYgYXaAV.rz5HQidnZWd_N8OL?continueMode=true&_x_zm_rtaid=S0qnO1Y7RIuVOQu3DjIqXg.1611338626418.620167ba512ba1df0ce389db98b3b464&_x_zm_rhtaid=927)
    - Section 20:
        + [Annotated Slides](./pdfs/intro_20.pdf)
        + [Zoom Recording for using Anaconda Python](https://kutztown.zoom.us/rec/share/VF1f6OFnv1sebvZsi49D80U_NpA8slcWQTrUZdsYQfYAHTSBVIMfGUquKw8PBBLo.9vi5lqQe4CaC2VLo)
* Future Stuff