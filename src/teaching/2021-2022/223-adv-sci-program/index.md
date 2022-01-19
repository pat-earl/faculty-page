infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Prerequisites 

(C or better in CSC123) *OR* (C or better in CSC135)

## Links

* [First Day Handout]({{get_link('firstday.html')}})
* [CS&IT Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [Lectures]({{get_link('lectures.md')}})
* [Class Resources]({{get_link('resources.md')}})

## Tentative Schedule

*Schedule is subject to change and is provided for guidance*

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
                Python Setup<br>
                Intro to Python
            </td>
            <td>
                <ul>
                    <li>WTP - Chapters 1 - 4</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<br>

* **WD** - Wellness Day  
* **WTP** - [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
* **DSH** - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)