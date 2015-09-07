title: Test directory

This directory has various tests and temporary files.

## Markdown files
{% for f in glob( dirname ~ '/*') | sort -%}
* [[/{{f}}|{{f[9:]}}]]: {{meta( f, 'title' ) | default( 'No Title, or not markdown', true ) }}
{% endfor %}

## Html files

No meta-data for these, of course. To get Jinja2 variables, consider including it instead.

{% for f in glob( dirname ~ '/*.html') | sort -%}
{%- from f import title as ftitle -%}
* [[/{{f}}|{{ftitle|default(f)}}]] 
{% endfor %}
