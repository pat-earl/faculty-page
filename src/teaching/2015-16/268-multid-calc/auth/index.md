{%- from get_file('../course_info.j2')  import course -%}
title: Solutions
breadcrumb: ../index.md|{{course.title}}

## Scanned Student Homework Solutions
{% for f in glob( 'sol[0-9]*.pdf' ) | sort( reverse=False ) -%}
* [[{{f}}|Assignment {{ sub( f, '^sol|\..*$', '' ) }}]]
  {% if f == 'sol11.pdf' -%}
    *(Note: The solution to Q3(d) has a fatal mistake.)*
  {% endif -%}
{% else %}
No homework solutions have been posted yet...
{% endfor %}

## Various Other Solutions

* [[sol-3-5-young.pdf|Youngs inequality and limits (HW 3, Q5)]]
