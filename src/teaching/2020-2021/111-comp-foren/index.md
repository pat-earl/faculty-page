infotable: 0
stylesheet: local.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})

# See Course on D2L.

Any assignments, course context, etc. will be posted on the D2L page linked above. 
