title: Tips and Tricks "Blog"

This is a collection of various tips and tricks I've found useful in my interaction with the standard geek tools I use often.
They're mainly posted here as a reference for me, so don't blame me if you don't find it useful... :)

## All posts

{% for f in glob( dirname ~ "/[0-9]*.md" ) -%}
    {%- set meta = get_meta(f) -%}
    ### [[/{{f}}|{{meta.title}}]]<small> (Posted {{f | sub( '.*/20(\d\d)(\d\d)(\d\d)-.*', '20\\1-\\2-\\3' ) }})</small>

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
