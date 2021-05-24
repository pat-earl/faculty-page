infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})
* [Linux Fundamentals](https://linux-training.be/linuxfun.pdf) by Paul Cobbaut
    * Supplemental textbook
* [CS&IT Documentation Standard](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [Slides]({{get_link('lectures.md')}})

All lectures and video recordings are posted on D2L under *Content*. 

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
            <td scope='row'>Week 1</td>
            <td>
                Introduction<br>
                The Utilities<br>
                The Shell
            </td>
            <td>
                <ul>
                    <li>Chapters 1, 2, 3, 5</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>Week 2</td>
            <td>
                File System
            </td>
            <td>
                <ul>
                    <li>Chapter 4</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>Week 3</td>
            <td>
                BASH Shell Scripting<br>
                Processes
            </td>
            <td>
                <ul>
                    <li>Chapters 8, 10</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>Week 4</td>
            <td>
                System Administration<br>
                Text Processing
            </td>
            <td>
                <ul>
                    <li>Chapters 14, 15</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>Week 5</td>
            <td>
                Python Scripting<br>
                <strong>NOTE:</strong><br>There will be a weekly quiz AND Final Exam for Friday this week.
            </td>
            <td>
                <ul>
                    <li>Chapter 12</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

