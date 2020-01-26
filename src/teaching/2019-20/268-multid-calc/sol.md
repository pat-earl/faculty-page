title: Homework Solutions

Solutions are only available to students who are *currently* enrolled in class.
If you are currently enrolled in class and don't have access, please send me an email with your Andrew ID.

{% for f in glob( 'auth/sol[0-9]*.pdf' ) | sort( reverse=False ) -%}
* [[{{f}}|Assignment {{ f | replace('auth/sol', '') | replace('.pdf', '') }}]]
{% else %}
* *Homework solutions will be posted as the semester progresses.*
{% endfor %}
