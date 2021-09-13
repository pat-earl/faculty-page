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

**Under Construction**

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
                Graphical Excellence
            </td>
            <td>
                Chapter 1 - <em>Visual Display of Quantitative Information</em>
            </td>
        </tr>
        <tr>
            <td>
                Asking Questions
            </td>
            <td>
                <a href="https://www.sciencemuseum.org.uk/objects-and-stories/florence-nightingale-pioneer-statistician">
                    Florence Nightingale: The Pioneer Statistician
                </a>
            </td>
        </tr>
        <tr>
            <td>
                Statistics Overview/Review
            </td>
            <td>
                <a href="https://onlinestatbook.com/2/index.html">Online Statistics Book</a><br>
                Chapter 1 - Introduction
            </td>
        </tr>
        <tr>
            <td>
                Graphical Integrity
            </td>
            <td>
                Chapter 2 - <em>Visual Display of Quantitative Information</em>
            </td>
        </tr>
        <tr>
            <td>
                Data Fundamentals
            </td>
            <td>
                <a href="{{ get_link('./slides/analysis-reading.docx') }}">
                    Structuring Data for Analysis (by Lari McEdward)
                </a>
            </td>
        </tr>
        
    </tbody>
</table>