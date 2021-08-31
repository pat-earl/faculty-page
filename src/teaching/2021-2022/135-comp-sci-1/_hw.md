{% from get_file('assignments.j2') import assignments %}
* [Homework Guidelines]({{get_link('./hw/homework_guidelines.md')}})
* [Project 0]({{get_link('./hw/proj0.md')}})
{% for hw in assignments %}
  {%- if hw['show'] == false -%}
  {%- else -%}
* [{{ hw['name'] }}]({{ get_link('./hw/' ~ hw['file'])}})
  {%- if hw['duedate'] != "" %}
    * **Due:** {{ hw['duedate'] }}
  {%- endif %}
  {% endif -%}
{% endfor %}