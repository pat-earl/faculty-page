infotable: 0
stylesheet: ../../course.css
title: CSC135 - Computer Science I (Fall 2021)
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Links

* [First Day Handout]({{get_link('firstday.html')}})
* [CS&IT Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [**Lectures**]({{get_link('lectures.md')}})
* References for C++
    * [cplusplus.com](https://www.cplusplus.com/)
    * [cppreference.com](https://en.cppreference.com/w/)
* [UNIXBootcamp](https://csit.kutztown.edu/UNIXbootcamp/)


## CSC135 SI Info

Patrick Perrin will be providing *Supplemental Instruction* for this course. He is scheduled to
be in OM242 during the times below:

* **Monday:** 1:30PM - 2:30PM
* **Wednesday:** 3:00PM - 4:00PM
* **Friday:** 1:30PM - 2:30PM

## Topics

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
            <td>
                Overview of Computers and Programming
            </td>
            <td>
                Chapter 1
            </td>
        </tr>
        <tr>
            <td>
                Basic Elements of C++<br>
            </td>
            <td>
                Chapter 2
            </td>
        </tr>
        <tr>
            <td>
                Input/Output
            </td>
            <td>
                Chapter 3 Sections 3.1 - 3.7
            </td>
        <tr>
            <td>
                Control Structures I (Selection)
            </td>
            <td>
                Chapter 4
            </td>
        </tr>
        <tr>
            <td>
                User Defined Functions (Part 1)
            </td>
            <td>
                Chapter 6 Sections 6.1 - 6.5
            </td>
        </tr>
        <tr>
            <td>
                Control Structures II (Repetition)
            </td>
            <td>
                Chapter 5
            </td>
        </tr>
        <tr>
            <td>
                File Input/Output
            </td>
            <td>
                Chapter 3 Section 8
            </td>
        </tr>
        <tr>
            <td>
                User Defined Functions (Part 2)
            </td>
            <td>
                Chapter 6 Sections 6.6 - 6.15
            </td>
        </tr>
        <tr>
            <td>
                User Defined Simple Data Types<br>
                Namespaces<br>
                The <em>string</em> type
            </td>
            <td>
                Chapter 7
            </td>
        <tr>
            <td>
                Arrays and Strings
            </td>
            <td>
                Chapter 8
            </td>
        </tr>
        <tr>
            <td>
                <em>TBD</em> Records (structs)
            </td>
            <td>
                Chapter 9
            </td>
        </tr>
    </tbody>
</table>

*NOTE:* This is a suggested order of topics which may change as the semester progresses.