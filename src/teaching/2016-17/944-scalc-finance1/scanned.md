title: Scanned lecture notes

These are scans of everything written on the documents camera each lecture and recitation.
If the handwriting is illegible in places, I recommend correlating it with the video or the typed notes.

{% set l = 0 -%}
{% set r = 0 -%}
{% set h = 0 -%}
{% set o = 0 -%}
{% for f in glob('pdfs/lec/20*.pdf') | sort -%}
    {% set date = f | replace( 'pdfs/lec/', '' ) | replace( '.pdf', '' ) -%}
    {% if date[-1] == 'r' -%}
        {% set r = r + 1 -%}
        * [[{{f}}|Recitation {{r}} (
    {%- elif date[-1] == 'h' -%}
        {% set h = h + 1 -%}
        * [[{{f}}|NY Problem Session {{h}} (
    {%- elif date[-1] == 'o' -%}
        {% set o = o + 1 -%}
        * [[{{f}}|Office hours {{o}} (
    {%- else -%}
        {% set l = l + 1 -%}
        * [[{{f}}|Lecture {{l}} (
    {%- endif -%}
    {{date[0:4]}}-{{date[4:6]}}-{{date[6:8]}})]]
{% endfor %}
