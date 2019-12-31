{%- from 'includes/macros.j2' import post_date -%}
title: Random Linux/Latex tricks
comments: disabled

This is a collection of various tips and tricks I've found useful in my interaction with the standard geek tools I use often.
They're mainly posted here as a reference for me, so don't blame me if you don't find it useful... :)

{# <h2>All posts</h2> #}

{% for f in glob( '[0-9]*.md' ) | sort( reverse=True ) -%}
{% set meta = get_meta(f) -%}
  <h4 class='mt-4'>
    <a href='{{get_link(f)}}'>{{meta.title}}</a>
  </h4>

  <small>Posted&nbsp;{{post_date(f)}}</small>

{% if meta.summary -%}
  {{ meta.summary  if meta.summary is string else '\n'.join( meta.summary )-}}
  <a class='text-nowrap float-right' href='{{get_link(f)}}'>More &raquo;</a>
{%- endif %}

{% if meta.tags -%}
  <div class='small' markdown='1'>*Tags:*
    {%- if meta.tags is string %} {{meta.tags}}
    {%- else %} {{ meta.tags | join( ', ' )}}
    {%- endif %}
  </div>
{% endif %}
{% endfor %}

{#- vim: set ft=jinja : -#}
