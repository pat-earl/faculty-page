{% set assignments = [
    {"name": "Homework #1", "file": "hw1.md", "duedate": "02/11", "show": true},
    {"name": "Homework #2", "file": "hw2.md", "duedate": "02/18", "show": true},
    {"name": "Homework #3", "file": "hw3.md", "duedate": "03/04", "show": true},
    {"name": "Homework #4", "file": "hw4.md", "duedate": "03/26", "show": false},
    {"name": "Homework #5", "file": "hw5.md", "duedate": "04/05", "show": false},
    {"name": "Final Project", "file": "final.md", "duedate": "05/05", "show": false},
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