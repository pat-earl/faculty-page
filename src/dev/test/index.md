title: Test directory

This directory has various tests and temporary files.

## All files

<div class='alert alert-warning' markdown='1'>
This is all files in the **source directory**. Not all might be rendered, so there will be broken links.
</div>

{% for f in glob( dirname ~ '/*') | sort -%}
* [[/{{f}}|{{f[9:]}}]]
{% endfor %}

## Markdown files

{% for f in glob( dirname ~ '/[0-9A-Za-z]*.md') | sort -%}
* [[/{{f}}|{{f[9:]}}]]: {{get_meta( f, 'title' ) | default( 'No Title, or not markdown', true ) }}
{% endfor %}

## Html files

No meta-data for these, of course. To get Jinja2 variables, consider including it instead.

{% for f in glob( dirname ~ '/*.html') | sort -%}
{%- from f import title as ftitle -%}
* [[/{{f}}|{{ftitle|default(f)}}]] 
{% endfor %}
