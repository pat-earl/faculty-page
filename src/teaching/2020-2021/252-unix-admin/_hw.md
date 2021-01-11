{%- if glob('hw/*.md') -%}

{% for hw in glob('hw/*.md') | sort %}
  {# get the meta data for this homework file! #}
  {%- set hw_meta = get_meta(hw) -%}
  {%-  if hw_meta['hidden'] == 'true' -%}
  {%- else -%}
* [{{ hw_meta['title'] }}]({{ get_link(hw) }})
  {%- endif -%}
{% endfor %}

{% endif %}