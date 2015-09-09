{%- from 'includes/macros.j2' import post_date -%}
title: Tips and Tricks "Blog"

This is a collection of various tips and tricks I've found useful in my interaction with the standard geek tools I use often.
They're mainly posted here as a reference for me, so don't blame me if you don't find it useful... :)

## All posts

{% for f in glob( '[0-9]*.md' ) | sort( reverse=True ) -%}
  ### [[{{f}}]] <small>(Posted {{post_date(f)}})</small>

{% set meta = get_meta(f) %}
{{ meta.summary | markdown }}

{% if meta.tags -%}
  <div class='small' markdown='1'>*Tags:*
    {%- if meta.tags is string %} {{meta.tags}}
    {%- else %} {{ meta.tags | join( ', ' )}}
    {%- endif %}
  </div>
{% endif %}
{% endfor %}

{#- vim: set ft=jinja : -#}
