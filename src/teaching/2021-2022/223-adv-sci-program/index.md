infotable: 0
title: CSC223 - Advanced Scientific Programming
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Prerequisites 

(C or better in CSC123) *OR* (C or better in CSC135)

## Links

* [**Lectures**]({{get_link('lectures.md')}})
* [First Day Handout]({{get_link('firstday.html')}})
* [CS&IT Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [Class Resources]({{get_link('resources.md')}})

## Topics

*Table is provided as general guidance, topic order is subject to change as needed.*


<table id="schedule">
    <colgroup>
        <col span="1" style="width: 65%;">
        <col span="1" style="width: 35%;">
    <thead>
        <tr>
            <th scope="col" style="text-align: center;">Topic(s)</th>
            <th scope="col" style="text-align: center;">Reading(s)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2">
                <b>Section 1: Introduction to Python</b>
            </td>
        </tr>
        <tr>
            <td>
                Intro to Python - Syntax, Variables, Operators
            </td>
            <td>
                WTP - Chapters 1 - 4
            </td>
        </tr>
        <tr>
            <td>
                Python Scalar Types & Data Structures<br>
                Python Control Flow<br>
            </td>
            <td>
                WTP - Chapters 5-8
            </td>
        </tr>
        <tr>
            <td>
                Python Functions & File IO
            </td>
            <td>
                WTP - Chapter 9</li>
            </td>
        </tr>
        <tr>
            <td>
                Python Errors and Modules
            </td>
            <td>
                WTP - Chapters 10 & 14
            </td>
        </tr>
        <tr>
            <td>
                Python Iterators & List Comprehensions
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <b>Section 2: Data Science Tools</b>
            </td>
        </tr>
        <tr>
            <td>
                NumPy Intro
            </td>
            <td>
                DSH - Chapter 2
            </td>
        </tr>
        <tr>
            <td>
                Pandas - Data Types
            </td>
            <td>
                DSH - Chapter 3, Sections 1 - 3
            </td>
        </tr>
        <tr>
            <td>
                Data Visualization & Matplotlib
            </td>
            <td>
                DSH - Chapter 4, Sections 1 - 5
            </td>
        </tr>
        <tr>
            <td>
                Pandas - Combining Data
            </td>
            <td>
                DSH - Chapter 4, Sections 5 - 7
            </td>
        </tr>
        <tr>
            <td>
                Pandas - Aggregation & Grouping
            </td>
            <td>
                DSH - Chapter 4, Sections 8 - 9
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <b>Section 3: Extra Information</b>
            </td>
        </tr>
        <tr>
            <td>
                Regular Expressions & Pandas String Processing
            </td>
            <td>
                WTP - Chapter 15, DSH - Chapter 4.10
            </td>
        </tr>
    </tbody>
</table>

<br>

* **WTP** - [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
* **DSH** - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)