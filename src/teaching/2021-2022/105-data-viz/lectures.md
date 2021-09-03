title: CSC105 - Lectures

{% set lectures = (
    {"name": "Graphical Excellence", "file": "slides/introduction.pdf"},
) %}

## Course Lectures

Below are the PowerPoint slides from class in PDF form.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Tableau Information

See the D2L course content page for information on how to access your student license for Tableau.
