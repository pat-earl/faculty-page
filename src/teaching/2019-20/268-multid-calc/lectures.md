title: Videos of Lectures, and Notes

These are PDFs of everything I wrote on the screen during lectures, along with links to videos for every lecture that the recording worked.

{% set videos = dict(
  o15='https://cmu.zoom.us/rec/share/_vZ0frjT32BLBavW-V6PVoJ5O6DFaaa8gyhK-aUIyk_EyH9KeyvL5B4QLwW5IiKN',
  l23='https://cmu.zoom.us/rec/share/v_Y2KpPR5D9OfpH842GEebxiOY3DX6a80SZIqPYInx6bETusOna2YiwE71YNjGtN',
  l24='https://cmu.zoom.us/rec/share/2fBQIajNxFlLGdLp51jCfYMfDNz0aaa8g3RKr_AIyxROF0-pVPYmO7E-e200J4k',
  l25='https://cmu.zoom.us/rec/share/opdXIOvL_FtOeY314QLiYqB5XaLgT6a8gSkb_PAJyEsMRg1qQ7CCtrBS7QnRk9WJ',
  o16='https://cmu.zoom.us/rec/share/wOdvLpHc2FxJTtLDwRrBUakFMYG-aaa80HAa__JZnhllsqiilAp6x7PjVLP62mvP',
    )
-%}
{% for f in glob('pdfs/lec/20*-?[0-9]*.pdf') | sort -%}
  {% set fn = f | replace( 'pdfs/lec/', '') | replace( '.pdf', '') -%}
  {% set date = fn[0:8] -%}
  {% set type = fn[9:] -%}
  {% if loop.first -%}
    <table class='table'>
      <thead>
        <tr>
          <th scope='col'>Date</th>
          <th scope='col'>Event</th>
          <th scope='col'>PDF</th>
          <th scope='col'>Video</th>
        </tr>
      </thead>
  {% endif -%}
      <tbody>
        <tr>
          <td>{{date[0:4]}}-{{date[4:6]}}-{{date[6:8]}}</td>
          <td>
            {%- if type[0] == 'r' -%}
              Recitation
            {%- elif type[0] == 'o' -%}
              Office hour
            {%- else -%}
              Lecture
            {%- endif -%}
            {{' #' ~ type[1:]}}
          </td>
          <td><a href='{{get_link(f)}}'>🗐</a></td>
          {%- if videos[type] %}
            <td><a href='{{videos[type]}}'>🎥</a></td>
          {%- endif %}
        </tr>
  {% if loop.last -%}
      </tbody>
    </table>
  {% endif -%}
{% else -%}
    * *Notes will be posted as the semester progresses.*
{% endfor %}
