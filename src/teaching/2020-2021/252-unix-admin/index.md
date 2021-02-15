infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})
* [Linux Fundamentals](https://linux-training.be/linuxfun.pdf) by Paul Cobbaut
    * Supplemental textbook
* [Lectures]({{get_link('lectures.html')}})

## Tentative Schedule

*Schedule is subject to change and is provided as guidance*

<table id="schedule">
    <colgroup>
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 45%;">
        <col span="1" style="width: 35%;">
    <thead>
        <tr>
            <th scope="col">Week</th>
            <th scope="col">Topic(s)</th>
            <th scope="col">Reading(s)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope='row'>1 (01/19 - 01/22)</td>
            <td>
                Course Intro<br>
                History of UNIX/Linux<br>
                Linux Reference
            </td>
            <td>
                <ul>
                    <li>Chapter 1</li>
                    <li>Chapter 2 (Pages 33-39)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>2 (01/25 - 01/29)</td>
            <td>
                Basic Commands<br>
                File and Directory
            </td>
            <td>
                <ul>
                    <li>Chapter 3 (Pages 49-68)</li>
                    <li>Chapter 4</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>3 (02/01 - 02/05)</td>
            <td>
                Files and Directories
            </td> 
            <td>
                <ul>
                    <li>Chapter 4</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>4 (02/08 - 02/12)<br><strong>WD:</strong> 02/11</td>
            <td>
                Files and Directories<br>
                NO CLASS THURSDAY - Wellness Day
            </td>
            <td>
                <ul>
                    <li>Chapter 5</li>
                    <li>Chapter 8 (Pages: 285 - 294)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>5 (02/15 - 02/19)</td>
            <td>
                Files and Directories<br>
                BASH<br>
                Shell Scripting
            </td>
            <td>
                <ul>
                    <li>Chapter 8 (Pages: 294-299)</li>
                    <li>Chapter 10</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>6 (02/22 - 02/26)</td>
            <td>
                Processes<br>
                <strong>Exam #1</strong> - Thursday
            </td>
            <td>
                <ul>
                    <li>Processes (Pages: 333 - 345)</li>
                    <li>TODO (More on Processes & VMs/Containers)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>7 (03/01 - 03/05)</td>
            <td>
                Processes<br>
                Virtual Machines & Containers<br>
                System Administration
            </td>
            <td>
                <ul>
                    <li>Appendex C</li>
                    <li>Linux Fundamentals (Pages: 274-302)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>8 (03/08 - 03/12)<br><strong>WD:</strong> 03/10</td>
            <td>
                System Administration
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>9 (03/15 - 03/19)</td>
            <td>
                Text Processing: sed & awk<br>
                <strong>Exam #2 - (TBD)</strong>
            </td>
            <td>
                <ul>
                    <li>Chapter 14 - AWK</li>
                    <li>Chapter 15 - SED</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>10 (03/22 - 03/26)</td>
            <td>
                Text Processing<br>
                Scripting Language - TBD
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>11 (03/29 - 04/02)<br><strong>WD:</strong> 04/02</td>
            <td>
                <em>Flexible Topics</em>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>12 (04/05 - 04/09)</td>
            <td>
                <em>Flexible Topics</em>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>13 (04/12 - 04/16)</td>
            <td>
                <em>Flexible Topics</em><br>
                <strong>Exam #3 ?- (TBD)</strong>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>14 (04/19 - 04/23)<br><strong>WD:</strong> 04/20</td>
            <td>
                <em>Flexible Topics</em><br>
                NO CLASS TUESDAY - Wellness Day
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>15 (04/26 - 04/30)</td>
            <td>
                <em>Flexible Topics</em>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>16 (05/03 - 05/07)</td>
            <td>
                <em>FINAL EXAMS WEEK</em>
            </td>
            <td></td>
        </tr>
    </tbody>
</table>


**WD** - Wellness Day
