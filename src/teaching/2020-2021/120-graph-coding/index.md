infotable: 0
stylesheet: local.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})

## Tentative Schedule

<table class="table">
    <thead>
        <tr>
            <th scope="col">Week</th>
            <th scope="col">Topic(s)</th>
            <th scope="col">Reading(s)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope='row'>1<br>(01/19 - 01/22)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>2<br>(01/25 - 01/29)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>3<br>(02/01 - 02/05)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>4<br>(02/08 - 02/12)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>5<br>(02/15 - 02/19)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>6<br>(02/22 - 02/26)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>7<br>(03/01 - 03/05)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>8<br>(03/08 - 03/12)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>9<br>(03/15 - 03/19)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>10<br>(03/22 - 03/26)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>11<br>(03/29 - 04/02)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>12<br>(04/05 - 04/09)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>13<br>(04/12 - 04/16)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>14<br>(04/19 - 04/23)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>15<br>(04/26 - 04/30)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>16<br>(05/03 - 05/07)</td>
            <td>Final Exam</td>
            <td></td>
        </tr>
    </tbody>
</table>

