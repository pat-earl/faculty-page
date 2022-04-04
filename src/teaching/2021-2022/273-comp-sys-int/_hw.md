{% set assignments = [
    {"name": "Homework #1", "file": "hw1.md", "duedate": "02/10", "show": true},
    {"name": "2/8 Make-Up Assignment", "file": "makeup_assign.md", "duedate": "02/10", "show": true},
    {"name": "Homework #2", "file": "hw2.md", "duedate": "03/04", "show": true},
    {"name": "Homework #3", "file": "hw3.md", "duedate": "04/15", "show": true},
] %}

{% for hw in assignments %}
  {%- if hw['show'] == false -%}
  {%- else -%}
* [{{ hw['name'] }}]({{ get_link('./hw/' ~ hw['file'])}})
  {%- if hw['duedate'] != "" %}
    * **Due:** {{ hw['duedate'] }}
  {%- endif %}
  {% endif -%}
{% endfor %}