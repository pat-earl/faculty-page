title: Videos of Lectures, and Notes

These are PDFs of everything I wrote on the screen during lectures, along with links to videos for every lecture that the recording worked.

{% set videos = dict(
  o15='https://cmu.zoom.us/rec/share/_vZ0frjT32BLBavW-V6PVoJ5O6DFaaa8gyhK-aUIyk_EyH9KeyvL5B4QLwW5IiKN',
  l23='https://cmu.zoom.us/rec/share/v_Y2KpPR5D9OfpH842GEebxiOY3DX6a80SZIqPYInx6bETusOna2YiwE71YNjGtN',
  l24='https://cmu.zoom.us/rec/share/2fBQIajNxFlLGdLp51jCfYMfDNz0aaa8g3RKr_AIyxROF0-pVPYmO7E-e200J4k',
  l25='https://cmu.zoom.us/rec/share/opdXIOvL_FtOeY314QLiYqB5XaLgT6a8gSkb_PAJyEsMRg1qQ7CCtrBS7QnRk9WJ',
  o16='https://cmu.zoom.us/rec/share/wOdvLpHc2FxJTtLDwRrBUakFMYG-aaa80HAa__JZnhllsqiilAp6x7PjVLP62mvP',
  l26='https://cmu.zoom.us/rec/share/uY98HZry1DJIcKfctn7EYqcFJ4H7aaa803cf_PQMzxmPJR5PvsYVzepxHH2IdhfR',
  l27='https://cmu.zoom.us/rec/share/uuBRd5vq3SRJfp3s5kTecbA6P9vqX6a8gXAa-acMyhmi5X6036i4f4gnuYDoKokW',
  o18='https://cmu.zoom.us/rec/share/6etfNpzy13pJZJ2X2njtC6siDpuiaaa8gSkf_fJZxE0B0H26pgMANlT4Gb4Kd0Bd',
  o19='https://cmu.zoom.us/rec/share/9e4vNeva3WhOZ6uT42X8UYIIG5XJeaa8hHAcr_JcmB00OSlCs5swVIaH9E5cCqI1',
  l28=get_link('auth/videos/20200330-l28.mp4'),
  l29='https://cmu.zoom.us/rec/share/ptR8dYDtz0ZLbpWQ5hCBZ7RxToj8aaa80CEd_6cPyUtaR4spTHYLzzQdxS2oMt7O',
  l30='https://cmu.zoom.us/rec/share/5MFPK-DAxmFJGbed1h2GXZERRoDLaaa82iQX_PUNyh0Z2kQLHxwxCiBxN9Qy_hd0',
  o20='https://cmu.zoom.us/rec/share/6etuMbTa33NOUrf0tGjwdq5_L7T5aaa8hiIdrvdezUroNoyFo4UTF_smztsTbEJG',
  o21='https://cmu.zoom.us/rec/share/xu1uMIDB00VLXJXcxx3WfZYHEIa5aaa81iAcrKZen0_yjgPAD7uH9J-OtU2fObtZ',
  l31='https://cmu.zoom.us/rec/share/tZFoD-rO9GVOYs_ywx7Bca4gEtu7T6a8h3Abr6VcmR5-DJZ9ZENiDreFGE2wXRyi',
  l32='https://cmu.zoom.us/rec/share/195KArr82D5Lb6Pds1jjS6oDOZa_T6a8hnBK-_Rfy07FJspFagc8qhmNilu5dWmz',
  l33='https://cmu.zoom.us/rec/share/2ctHHe798kdJTqvg8xvgXKIoAIDUaaa81nBK_aAJnUkA85q79lpZE5Jn4zqEnSnY',
  o22='https://cmu.zoom.us/rec/share/14tedqj37F1OEqfN0UzYRaQ7D6Hqeaa81HRNrKcIz0wIW-cHcEGI27Se5NKnHVbc',
  o23='https://cmu.zoom.us/rec/share/-fFsMZvs0z5ITI2cs3nkAoojM5bqeaa8gCUWr_MKzEinQYJItCLpE1fcDPqOpV48',
  l34='https://cmu.zoom.us/rec/share/_pxkJJPR5nJJQaPGwnrHa_Z5ENXVaaa8hyQY8vtczButJr5TefMAMJ_QRp7jarC6',
  l35='https://cmu.zoom.us/rec/share/zNZFEYvaplxIfInC1RnDY4gbE77Zeaa81iEW8qdYmh5j99qKT5GO3-AEREuuZe4C',
  l36='https://cmu.zoom.us/rec/share/4ZJ4PYHr1UpOG5Xt0X3nQZc7Mp_Ceaa81yMerKIEmU6Hm-F36cqKqCKEdx5Qk0yb',
  o24='https://cmu.zoom.us/rec/share/481QC47tr0hIXavW9BjzZZMML7Smeaa80SIY_vMLyEhjepx4rQJy6srmozVtTEgB',
  o25='https://cmu.zoom.us/rec/share/69UqcIqtxG5Ia6_PyhmDQvYtG4fPX6a81CFM-6FeyUfnNjJTdcH62zhVDuzMBBqE',
  l37='https://cmu.zoom.us/rec/share/5uZMNqnN0TNJQdboxEOcfpwCJa3_T6a8hidIqfJZyRplqQMFHM9StGK3kwxeuVW7',
  l38='https://cmu.zoom.us/rec/share/xJFzCo3W821JRs_yzRrZWZURA9n5T6a81iQZ_vsLy0m0BirrdXchGfRNCAw8HeNA',
  l39='https://cmu.zoom.us/rec/share/wswrLa3O3GhOYqPPx27PXq0FHZrMeaa8hycdrPVezU_4eQLiwk0YMJicqQ0zJ-MT?startTime=1587742126000',
  o26='https://cmu.zoom.us/rec/share/zMdPErz822JLbLPt-U_YeZ8vMY-iX6a81iJLqPRYzE1O-db678nNbYjI6gkW5mQw',
  o27='https://cmu.zoom.us/rec/share/3PxxEKDd8D9Lf8-RuF7WYI4HF7zgaaa81SlL8qVZyEx8wj4JVih3f9guWnW0UdWQ',
  l40='https://cmu.zoom.us/rec/share/w8xEDfLw72RIGM-cq2CEWZA7Gov9eaa8hihN-_VZz0z4WvAzHxtmozdWSFeLrGtA',
  l41='https://cmu.zoom.us/rec/share/yJdXJp_S10BLSbOdswLSC5UYD6DOaaa8gXQa_vsPyhy-foE7bRtZFFgzpEFL4V5j',
  l42='https://cmu.zoom.us/rec/share/5tFYD6_v71JIZ9LM9l2GQYhwRJS-eaa80XIY-fBYz0qafRc3yhOc8l_me_5apPgi',
  o28='https://cmu.zoom.us/rec/share/-JZbCaDr3E9LRoXtynPSAbANHtzJeaa8hyJL-vQEnxk2jgzw4Nl76Vr5jPbHntaL',
  o29='https://cmu.zoom.us/rec/share/_P1KP7_-_H5OUq_S40aEBIEwPK3gT6a81CYc_qJcnU7cTXoTN8r6MgwEDRIqUEfm',
  r14=get_link('auth/videos/20200505-r14.mp4'),
  o30='https://cmu.zoom.us/rec/share/64tPH7Hwp19LfNLiyUzEUPc7Gq3oX6a8hiYe8_EPyk7S1Fv7CsN8TPyUAozQjIaT',
) -%}
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
