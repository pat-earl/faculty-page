{%- if glob('pdfs/hw.pdf') -%}
* [[pdfs/hw.pdf|Homework]]
{%- elif glob('pdfs/hw-page*.pdf') -%}
* [[{{glob('pdfs/hw-page*.pdf')[0]}}|Current Assignment]]
    {%- if glob('pdfs/hw-prev.pdf') %}
* [[pdfs/hw-prev.pdf|Previous assignments]]
    {%- endif %}
{%- else -%}
Homework and solutions will be posted here.
{%- endif -%}
{%- if glob('auth/sol*') %}
* [[sol.md]]
{%- endif %}
