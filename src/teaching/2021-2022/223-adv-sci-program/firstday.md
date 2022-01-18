title: First Day Handout
{%- import 'includes/site.j2' as site -%}
{% from 'includes/macros.j2' import office_hours_table with context -%}
{% from get_file('course_info.j2') import course %}

## Course Information

**Course:** 
: <span id='course_code'>{{course.abv_title}}</span> {{course.abv_name}} <span hidden id='semester_code'>{{course.abv_semester}}</span>

**Semester:**
: Spring 2022

**Instructor:**
: Mr. {{site_author}}

**Office:**
: OM252

**Office Phone:**
: {{author_office_phone}}

**E-Mail:**
: <{{author_email}}>

**Faculty Web Page:**
: <https://csit.kutztown.edu/~earl>

**Office Hours:**
{% for day,time in site.office_hours.items() -%}
: <strong>{{day}}:</strong> {{time}}
{% endfor %}

Always refer to my website for the latest office hours.

**Meetings:** 
: TBD

**Format:** 
: In-Person

## Materials

### Recommended Textbooks
* *A Whirlwind Tour of Python* by Jake VanderPlas. **ISBN:** 978-1491964644
* *Python Data Science Handbook* by Jake VanderPlas. **ISB:** 978-1491912058

*NOTE:* Both these textbooks are available on the course web page for free. You only need
to purchase the books if you want a physical copy (or support the author).

## Description

This course takes students deeper into the theory of scientific programming, building on a foundation of sound programming methodology and an understanding of the modern programming languages prevalent in scientific communities and of the specialized tools and libraries.  Thorough grounding in computer science principles will enable the student to gain knowledge and skill to best leverage these tools for scientific study and research.  Topics include basic concepts of problem analysis and program design both from a procedural and structural standpoint – algorithm development, algorithm analysis, data structures, data storage, data analysis and data visualization.  Additional topics will include applications to scientific problems.

## Objectives

1. Analyze scientific problems
1. Design and implement high level programs in scientific arena.
1. Explain scientific data manipulation techniques.
1. Employ data analysis effectively in the scientific arena.
1. Employ simulation effectively in the scientific arena.
1. Explain the process and problems of casual inference.
1. Choose and employ specialized scientific programming libraries.

## Course Prerequisites

(C or better in CSC123) OR (C or better in CSC135)

## Grading 

Your final course grade will be made up of the following:

* Assignments: 50%
* Exams (2): 30%
* Final Project: 15%
* Class Participation: 5%

The standard [University Grading Policy](http://app.kutztown.edu/policyregister/Policy/ACA-048) will 
be used to calculate your final letter grade. 

**Your exam average must be at least 60% in order to pass the course.**

**Class Participation:**
: Grade is based off regular class attendance and participation in the classroom.

**Exams/Quizzes:**

: Exams will be announced during class and must be taken during their scheduled time/location.
: Missed exams/quizzes will be handled on a case-by-case basis. For a list of approved reasons review the *Class Absence* section from the [Class Attendance](http://app.kutztown.edu/policyregister/Policy/ACA-016) University policy. 

**Homework (Assignments/Projects):**
: All homework submissions must include the following information:
Your Name(s), The Course, Semester, Year, and Assignment/Project Number or Name.
Homework can be submitted up to two days late, with a 10% penalty applied
each day.

# Course Policies

**Masks:**
: Due to the continuing pandemic and spread of the COVID delta variant, you will be required
to properly wear masks while attending class and in my office regardless of your vaccination status. 
Students who show up to class without a mask will be asked to put one on, 
go to the department's office in OM254 to get a disposable one, or leave class.

: Students who break this policy on multiple occasions will be reported to the Student Conduct Board. 

: This policy will be in effect while Berks County has a high or substantial transmission rate and/or
based on University mandates. 

: CDC County Level Map: <https://covid.cdc.gov/covid-data-tracker/#county-view>

: Reusable cloth masks and other PPE can be requested by emailing <ppesupplies@kutztown.edu>

**Attendance:**
: Regular and timely class attendance is expected and highly encouraged. Students are responsible for materials covered during class time. 

**Academic Dishonesty:**  
: Refer to to the following policies. Repeated violators will receive the maximum allowable penalty for any infraction. 
: [Computer Science & Information Technology Department's Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
: [University's Academic Dishonesty Policy](https://app.kutztown.edu/policyregister/policy.aspx?policy=ACA-027)

**Classroom Etiquette:**
: Respect for your classmates, instructor, and the class is expected. Please come to class on time
and prepared to learn. Coming and going during class should be limited to unavoidable situations.
**Electronic devices should not be seen or heard**, unless being used for class activities, note taking,
etc. Using your cell phone to take pictures of lecture notes, is not a valid purpose. There should be
no classroom conversations, sleeping (with snoring), or general disruptions during class.

**Course Work / Accreditation:**
: Any coursework submitted to the instructor (included by not limited to assignments, tests, and
projects) may be photocopied and retained for the purpose of assessment, accreditation and 
quality improvement. 

**E-Mail Correspondence:**
: The best way to contact the instructor is via e-mail (earl@kutztown.edu). You are required to use
your Kutztown University supplied e-mail for all correspondence, outside email services will be 
ignored. Your email should be professionally written and use a relevant subject line. Additionally,
any emails relating to this course must include the course prefix and number at the beginning of the 
subject line. For Example: If you're in the course CSC101, your subject line should be similar to
these examples:

* "[CSC101] Question on Assignment 1"
* "CSC101 - Question on Assignment 1"

E-mails that follow these guidelines can expect a response within 48 business hours, usually 
shorter. 

**Students with Disabilities:**
: Students with diagnosed disabilities or special needs that require accommodations for this course
must first contact the Disability Services Office, (Office of Human Diversity at 
215 Stratton Administration Building.) Do this as soon as possible so that we may have a dialogue as
to your needs and the recommended accommodations. Accommodations cannot be given until the 
instructor has seen your letter. Accommodations cannot be retroactively applied. 

**Gender-Based Crimes:**
: Educators must report incidents of gender-based crimes, including sexual assault, sexual harassment, 
stalking, dating violence, and domestic violence. If a student discloses such incidents to me during 
class or in a course assignment, I am not required to report the disclosure, unless the student was 
a minor at the time the incident occurred. Regardless of the student’s age, if the incident is disclosed 
to me outside the classroom setting or a course assignment, I am required by law to report the disclosure, 
including relevant details, such as the names of those involved in the incident, to Public Safety 
and Police Services and to Mr. Jesus Peña, Title IX Coordinator.

***NOTE:*** This document is subject to changes at the discretion of the instructor
