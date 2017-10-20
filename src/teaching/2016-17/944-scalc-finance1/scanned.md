title: Scanned lecture notes

These are scans of everything written on the documents camera each lecture and recitation.
If the handwriting is illegible in places, I recommend correlating it with the video or the typed notes.

{# Scope "bug". Can't use normal variables inside loops. -#}
{% set vars = {'l':0, 'r':0, 'h':0, 'o':0} -%}
{% for f in glob('pdfs/lec/20*.pdf') | sort -%}
    {% set date = f | replace( 'pdfs/lec/', '' ) | replace( '.pdf', '' ) -%}
    {% if date[-1] == 'r' -%}
        {% set _ = vars.update( {'r':vars.r + 1}) -%}
        * [[{{f}}|Recitation {{vars.r}} (
    {%- elif date[-1] == 'h' -%}
        {% set _ = vars.update( {'h':vars.h + 1}) -%}
        * [[{{f}}|NY Problem Session {{vars.h}} (
    {%- elif date[-1] == 'o' -%}
        {% set _ = vars.update( {'o':vars.o + 1}) -%}
        * [[{{f}}|Office hours {{vars.o}} (
    {%- else -%}
        {% set _ = vars.update( {'l': vars.l + 1}) -%}
        * [[{{f}}|Lecture {{vars.l}} (
    {%- endif -%}
    {{date[0:4]}}-{{date[4:6]}}-{{date[6:8]}})]]
{% endfor %}
