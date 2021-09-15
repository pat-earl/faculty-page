infotable: 0
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Links

* [First Day Handout]({{get_link('firstday.html')}})
* [CS&IT Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [**Lectures**]({{get_link('lectures.md')}})

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
            <td>Introduction to Networking</td>
            <td><em>Top-Down Approach</em> - Sections 1.1, 1.2, 1.5</td>
        </tr>
        <tr>
            <td>Networking Devices</td>
            <td><em>Top-Down Approach</em> - Sections 4.2 (pgs 311-314), 6.43</td>
        <tr>
            <td>Circuit and Packet Switching</td>
            <td><em>Top-Down Approach</em> - Sections 1.3 & 1.4</td>
        </tr>
        <tr>
            <td>Application Layer - Overview</td>
            <td><em>Top-Down Approach</em> - Section 2.1</td>
        </tr>
        <tr>
            <td>Application Layer - HTTP</td>
            <td>
                <em>Top-Down Approach</em> - Section 2.2<br>
                (Optional)<a href="https://robertheaton.com/2014/03/27/how-does-https-actually-work/">
                    How does HTTPS actually work? - Robert Heaton
                    </a><br>
                (Optional)<a href="https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/">
                    How Browsers Work
                    </a>
            </td>
        </tr>
        <tr>
            <td>Application Layer - FTP</td>
            <td>TBD</td>
        </tr>
        <tr>
            <td>Application Layer - E-Mail</td>
            <td><em>Top-Down Approach</em> - Section 2.3</td>
        </tr>
        <tr>
            <td>Application Layer - DNS</td>
            <td><em>Top-Down Approach</em> - Section 2.4</td>
        </tr>
        <tr>
            <td>Application Layer - Misc.</td>
            <td><em>Top-Down Approach</em> - Sections 2.5 - 2.6</td>
        </tr>
        <tr>
            <td>Transport Layer - Overview</td>
            <td><em>Top-Down Approach</em> - Sections 3.1, 3.2, 3.3, 3.5</td>
        </tr>
        <tr>
            <td>Network Layer - Overview</td>
            <td><em>Top-Down Approach</em> - Sections TBD</td>
        </tr>
        <tr>
            <td>Link Layer - Overview</td>
            <td><em>Top-Down Approach</em> - Sections 6.1 & 6.2</td>
        </tr>
        <tr>
            <td>Wireless Technology</td>
            <td><em>Top-Down Approach</em> - Sections 7.1 & 7.2</td>
        </tr>
    </tbody>
</table>