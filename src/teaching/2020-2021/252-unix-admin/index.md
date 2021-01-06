infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})
* [Linux Fundamentals](https://linux-training.be/linuxfun.pdf) by Paul Cobbaut
    * This is only meant to supplement the main textbook. Please let me know if
    the link goes down.

## Tentative Schedule

*Schedule is subject to change and is only provided for guidance*

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
                <ul>
                    <li>Course Intro</li>
                    <li>What is UNIX/Linux?</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>Chapter 1 (All)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>2 (01/25 - 01/29)</td>
            <td>
                <ul>
                    <li>Getting Help! (For Linux)</li>
                    <li>Directories and Files</li>
                    <ul>
                        <li>File Paths</li>
                        <li>File Permissions</li>
                    </ul>
                </ul>
            </td>
            <td>
                <ul>
                    <li>Chapter 2 (Pages 33-41)</li>
                    <li>Chapter 4 (Pages 84-88, <br>
                        90-95, <br>
                        100 "Access Permissions" - 106)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>3 (02/01 - 02/05)</td>
            <td>
                <ul>
                    <li>Directories and Files (cont.)
                    <ul>
                        <li>Links (Hard & Symbolic)</li>
                    </ul>
                    <li>The Shell</li>
                    <ul>
                        <li>Shells</li>
                        <li>I/O Redirection/li>
                        <li>Piping</li>
                    </ul>
                </ul>
            </td> 
            <td>
                <ul>
                    <li>Chapter 4: (Pages 112-122)</li>
                    <li>Chapter 5 (All)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>4 (02/08 - 02/12)<br>(<strong>WD:</strong> 02/11)</td>
            <td>
                <ul>
                    <li>The Shell (cont.)</li>
                    <ul>
                        <li>Utilities</li>
                        <li>Variables and User Environment</li>
                    </ul>
                    <li>File System
                </ul>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>5 (02/15 - 02/19)</td>
            <td>
                <ul>
                    <li>Exam #1 (TBD)</li>
                </ul>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>6 (02/22 - 02/26)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>7 (03/01 - 03/05)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>8 (03/08 - 03/12)<br>(<strong>WD:</strong> 03/10)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>9 (03/15 - 03/19)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>10 (03/22 - 03/26)</td>
            <td>
                <ul>
                    <li>Exam #2 (?)</li>
                </ul>
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>11 (03/29 - 04/02)<br>(<strong>WD:</strong> 04/02)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>12 (04/05 - 04/09)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>13 (04/12 - 04/16)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>14 (04/19 - 04/23)<br>(<strong>WD:</strong> 04/20)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>15 (04/26 - 04/30)</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>16<br>(05/03 - 05/07)</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
<p>WD - Wellness Day</p>
