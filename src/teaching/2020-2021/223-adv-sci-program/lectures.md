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
    {"name": "Matplotlib", "file": "slides/matplotlib.md"},
    {"name": "Pandas - MultiIndex", "file": "slides/mutli_index.md"},
    {"name": "Pandas - Combining Data", "file": "slides/combine.md"},
    {"name": "Pandas - Aggregation & Grouping", "file": "slides/agg.md"},
    {"name": "Pandas - String Operations", "file": "slides/strings.md"},
    {"name": "Pandas - Time Series", "file": "slides/time.md"},
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
* Week 9
    - Homework #3 Example with Pandas
        * *For the notebooks, right click and do a "Save As". Import them into your own notebook environment.* 
        * Use the *HTML* view to see the code and output in your browser
        * Section 10: [Notebook](./pdfs/hw3_pandas_10.ipynb) [HTML](./pdfs/hw3_pandas_10.html)
        * Section 20: [Notebook](./pdfs/hw3_pandas_20.ipynb) [HTML](./pdfs/hw3_pandas_20.html)

* Week 11
    - Flights 
        * Section 10: [Notebook](./pdfs/flights/flights_demo_10.ipynb) [HTML](./pdfs/flights/flights_demo_10.html)
        * Section 20: [Notebook](./pdfs/flights/flights_demo_20.ipynb) [HTML](./pdfs/flights/flights_demo_20.html)

