{%- from 'includes/macros.j2' import post_date -%}
title: Miscellaneous Tips and Tricks
comments: disabled

This is a collection of various tips and tricks I've found useful in my interaction with the standard geek tools I use often.
They're mainly posted here as a reference for me, so don't blame me if you don't find it useful... :)

{# <h2>All posts</h2> #}

{% for f in glob( '[0-9]*.md' ) | sort( reverse=True ) -%}
{% set meta = get_meta(f) -%}
  <h3>
    <a href='{{get_link(f)}}'>{{meta.title}}</a><br />
    <small>Posted&nbsp;{{post_date(f)}}</small>
  </h3>

{% if meta.summary -%}
  {{ meta.summary  if meta.summary is string else '\n'.join( meta.summary )-}}
  <a class='text-nowrap tight-float-right' href='{{get_link(f)}}'>More &raquo;</a>
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
