title: Scanned lecture notes

## Document camera scans from lectures

These are scans of everything written on the documents camera each lecture and recitation.
If the handwriting is illegible in places, I recommend correlating it with the video or the typed notes.

{% for f in glob('pdfs/lec/20*-?[0-9]*.pdf') | sort -%}
    {% set fn = f | replace( 'pdfs/lec/', '') | replace( '.pdf', '') -%}
    {% set date = fn[0:8] -%}
    {% set type = fn[9:] -%}
    * [[{{f}}|
        {%- if type[0] == 'r' -%}
            Recitation
        {%- elif type[0] == 'h' -%}
            NY Problem Session
        {%- elif type[0] == 'o' -%}
            Office hours
        {%- else -%}
            Lecture
        {%- endif -%}
      {{' ' ~ type[1:]}} ({{date[0:4]}}-{{date[4:6]}}-{{date[6:8]}})]]
{% else -%}
    * *Notes will be posted as the semester progresses.*
{% endfor %}

## Other resources

* [[auth/shreve-scalc-prep.pdf|Scanned notes]] from preparatory lectures by Steve Shreve. (Available to current students only.)
