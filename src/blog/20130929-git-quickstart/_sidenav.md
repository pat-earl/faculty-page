{%- from 'includes/macros.j2' import post_series -%}
{{- post_series( '/' ~ dirname ~ '.md', glob( '/'~dirname~'/[0-9]*.md' ) | sort ) -}}
{#- vim: set ft=jinja : -#}
