title: CSC311 - Lectures

{% set lectures = (
    {"name": "Chapter 1 - Introduction", "file": "slides/chapter1.pdf"},
) %}

## Course Lectures

Below are the PowerPoint slides from class in PDF form. You can also find the slides in their
original form on the Author's webpage: <https://gaia.cs.umass.edu/kurose_ross/ppt.php>

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}
