{%- from get_file('../course_info.j2')  import course -%}
title: Solutions
breadcrumb: ../index.md|{{course.title}}

## Homework

{% for f in glob( 'sol[0-9]*.pdf' ) | sort( reverse=True ) -%}
* [[{{f}}|Assignment {{ sub( f, '^sol|\..*$', '' ) }}]]
{% else %}
No homework solutions have been posted yet...
{% endfor %}
