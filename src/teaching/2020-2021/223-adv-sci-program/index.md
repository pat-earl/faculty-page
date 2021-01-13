infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Prerequisites 

(C or better in CSC123) *OR* (C or better in CSC135)

## Course Resources

* [First Day Handout]({{get_link('firstday.html')}})
* [CS&IT Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)

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
                Python Setup - Miniconda<br>
                Intro to Python
            </td>
            <td>
                <ul>
                    <li>WTP - Chapters 1 - 4</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>2 (01/25 - 01/29)</td>
            <td>
                Python Data Types & Control Flow
            </td>
            <td>
                <ul>
                    <li>WTP - Chapters 6 - 8</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>3 (02/01 - 02/05)</td>
            <td>
                Python Functions and File I/O
            </td> 
            <td>
                <ul>
                    <li>WTP - Chapter 9</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>4 (02/08 - 02/12)<br><strong>WD:</strong> 02/11</td>
            <td>
                Python Errors and Modules
            </td>
            <td>
                <ul>
                    <li>WTP - Chapter 10</li>
                    <li>WTP - Chapter 14</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>5 (02/15 - 02/19)</td>
            <td>
                Python Iterators and List Comprehensions
            </td>
            <td>
                <ul>
                    <li>WTP - Chapters 11-13</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>6 (02/22 - 02/26)</td>
            <td>
                <strong>Exam #1</strong> - TBD
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td scope='row'>7 (03/01 - 03/05)</td>
            <td>
                NumPy
            </td>
            <td>
                <ul>
                    <li>DSH - Chapter 2</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>8 (03/08 - 03/12)<br><strong>WD:</strong> 03/10</td>
            <td>
                Pandas - Data Types<br>
                <strong>NO CLASS WEDNESDAY</strong> - Wellness Day
            </td>
            <td>
                <ul>
                    <li>DSH - Sections 3.1 - 3.3</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>9 (03/15 - 03/19)</td>
            <td>
                Data Visualization and Matplotlib
            </td>
            <td>
                <ul>
                    <li>DSH - Sections 4.1-4.5</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>10 (03/22 - 03/26)</td>
            <td>
                Pandas - Combining Data
            </td>
            <td>
                <ul>
                    <li>DSH - Sections 4.5-4.7</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>11 (03/29 - 04/02)<br><strong>WD:</strong> 04/02</td>
            <td>
                Pandas Aggregation & Grouping<br>
                <strong>NO CLASS FRIDAY</strong> - Wellness Day
            </td>
            <td>
                <ul>
                    <li>DSH 4.8 - 4.9</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>12 (04/05 - 04/09)</td>
            <td>
                <strong>Exam #2</strong> - TBD
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>13 (04/12 - 04/16)</td>
            <td>
                Regular Expressions<br>
                Pandas String Processing
            </td>
            <td>
                <ul>
                    <li>WTP - Chapter 15</li>
                    <li>DSH - Section 4.10</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td scope='row'>14 (04/19 - 04/23)<br><strong>WD:</strong> 04/20</td>
            <td>
                Flexible Topics
            </td>
            <td></td>
        </tr>
        <tr>
            <td scope='row'>15 (04/26 - 04/30)</td>
            <td>
                Flexible Topics
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

<br>

* **WD** - Wellness Day  
* **WTP** - [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
* **DSH** - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)