{%- from 'teaching/courses.j2' import courses, old_teaching, md_current_courses_long -%}
{%- from 'teaching/sections.j2' import secs -%}
title: Courses

## {{secs.current_courses}}

{{ md_current_courses_long() }}

## Independent Studies

* [Summer 2021 - CSC123](./independent/csc123.html) - Under Construction
* [Summer 2021 - CSC273](./independent/csc273.html) - Under Construction

## {{secs.previous_courses}}

Courses previously taught at KU (Some may not have links)

{% for (cn, ct, rest) in courses -%}
* *<span class='text-nowrap'>{{('CSC'~cn ~ ': ') if cn else ''}}{{ct}}.</span>*
  {%- for (cy, cs, cl) in rest -%}
    <a class='text-nowrap' href='{{cl}}'>
      {{ 'Spring' if cs == 's' else
          ( 'Fall' if cs == 'f' else cs ) }}
      {{cy-}}
    </a>
    {%- if loop.last %}.{% else %}, {% endif %}
  {%- endfor %}
{% endfor %}

#### Previous IS/IIs

* [Spring 2021 Networking IS](./independent/networking.html) (Archived)

