title: CSC105 - Lectures

{% set lectures = (
    {"name": "Graphical Excellence", "file": "slides/introduction.pdf"},
    {"name": "Asking the Right Questions", "file": "slides/questions.pdf"},
    {"name": "Statistics", "file": "slides/stats.md"},
    {"name": "Data Fundamentals", "file": "slides/Data Fundamentals.pptx"},
    {"name": "Connecting to Data w/ Tableau", "file": "slides/Tableau - Connecting to Data.pptx"},
    {"name": "Preparing Data in Tableau", "file": "slides/Preparing Data in Tableau.pptx"},
    {"name": "Charts and Chart Types", "file": "chart_types.pdf"},
    {"name": "Field Types and Variables in Tableau", "file": "fields_and_variables.pptx"},
) %}

## Course Lectures

Below are the PowerPoint slides from class in PDF form.

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Tableau Information

See the D2L course content page for information on how to access your student license for Tableau.
