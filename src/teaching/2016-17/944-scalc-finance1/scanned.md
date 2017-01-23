title: Scanned lecture notes

These are scans of everything I write on the document camera each lecture.
If the handwriting is illegible in places, I recommend correlating it with the video or the typed notes.

{% set j = 0 %}
{% for f in glob('pdfs/lec/20*.pdf') -%}
{% set j = j + 1 -%}
{% set date = f | replace( 'pdfs/lec/', '' ) | replace( '.pdf', '' ) -%}
* [[{{f}}|Lecture {{j}} ({{date[0:4]}}-{{date[4:6]}}-{{date[6:8]}})]]
{% endfor %}
