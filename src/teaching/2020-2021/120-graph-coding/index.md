infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Links

* [First Day Handout]({{get_link('firstday.html')}})
* [Lectures]({{get_link('lectures.html')}})
* [Resources]({{get_link('resources.md')}})

## Tentative Schedule

*Schedule is subject to change and only provided for guidance*

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
                Software Requirements<br>
                Pixels, Processing, Interaction (Lesson 1)
            </td>
            <td>
                <ul>
                    <li>Chapter 1</li>
                    <li>Chapter 2</li>
                    <li>Chapter 3</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>2 (01/25 - 01/29)</td>
            <td>
                Variables<br>
                Conditionals
            </td>
            <td>
                <ul>
                    <li>Chapter 4</li>
                    <li>Chapter 5</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>3 (02/01 - 02/05)</td>
            <td>
                Transformations & 3D<br>
                <strong>Quiz</strong> - Chpts. 1 - 4
            </td> 
            <td>
                <ul>
                    <li>Chapter 14</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>4 (02/08 - 02/12)<br><strong>WD:</strong> 02/11</td>
            <td>
                Transformations & 3D<br>
                Assign Project #1<br>
                NO CLASS THURSDAY - Wellness Day
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td scope='row'>5 (02/15 - 02/19)</td>
            <td>
                Loops<br>
                Functions
            </td>
            <td>
                <ul>
                    <li>Chapter 6</li>
                    <li>Chapter 7</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>6 (02/22 - 02/26)</td>
            <td>
                Objects
            </td>
            <td>
                <ul>
                    <li>Chapter 8</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>7 (03/01 - 03/05)</td>
            <td>
                Arrays<br>
                <strong>Quiz</strong> - Chpts. 5 - 8
            </td>
            <td>
                <ul>
                    <li>Chapter 9</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>8 (03/08 - 03/12)<br><strong>WD:</strong> 03/10</td>
            <td>
                Arrays<br>
                Assign Project #2
            </td>
            <td>
                <ul>
                    <li>Chapter 9</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>9 (03/15 - 03/19)</td>
            <td>
                Text
            </td>
            <td>
                <ul>
                    <li>Chapter 17</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>10 (03/22 - 03/26)</td>
            <td>
                <em>Review Week</em>
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td scope='row'>11 (03/29 - 04/02)<br><strong>WD:</strong> 04/02</td>
            <td>
                Algorithms<br>
                Assign Project #3
            </td>
            <td>
                <ul>
                    <li>Chapter 10</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>12 (04/05 - 04/09)</td>
            <td>
                Algorithms<br>
                <strong>Exam #1</strong> - Chpts. 1 - 10
            </td>
            <td>
                <ul>
                    <li>Chapter 10</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>13 (04/12 - 04/16)</td>
            <td>
                Debugging<br>
                Libraries<br>
                Mathematics<br>
                Assign Project #4
            </td>
            <td>
                <ul>
                    <li>Chapter 11</li>
                    <li>Chapter 12</li>
                    <li>Chapter 13</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>14 (04/19 - 04/23)<br><strong>WD:</strong> 04/20</td>
            <td>
                Video<br>
                NO CLASS TUESDAY - Wellness Day
            </td>
            <td>
                <ul>
                    <li>Chapter 16</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>15 (04/26 - 04/30)</td>
            <td>
                <em>Flexible Topics/Lab Session</em>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>16 (05/03 - 05/07)</td>
            <td>
                FINAL EXAMS WEEK
            </td>
            <td></td>
        </tr>
    </tbody>
</table>


**WD** - Wellness Day