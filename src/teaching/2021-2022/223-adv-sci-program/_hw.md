{% from get_file('assignments.j2') import assignments %}
{% for hw in assignments %}
  {%- if hw['show'] == false -%}
  {%- else -%}
* [{{ hw['name'] }}]({{ get_link('./hw/' ~ hw['file'])}})
  {%- if hw['duedate'] != "" %}
    * **Due:** {{ hw['duedate'] }}
  {%- endif %}
  {% endif -%}
{% endfor %}