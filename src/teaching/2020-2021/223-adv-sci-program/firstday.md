title: First Day Handout
{%- import 'includes/site.j2' as site -%}
{% from 'includes/macros.j2' import office_hours_table with context -%}
{% from get_file('course_info.j2') import course %}

## Course Information

**Course:** 
: <span id='course_code'>{{course.abv_title}}</span> {{course.abv_name}} <span hidden id='semester_code'>{{course.abv_semester}}</span>

**Semester:**
: Spring 2021

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
: Section 10: GR 307 | Mon/Wed/Fri 11:00 AM - 11:50 AM
: Section 20: GR 307 | Mon/Wed/Fri 12:00 PM - 12:50 PM

**Format:** 
: Hybrid (Sync In-Person/Zoom)

## Materials

### Required Textbook

* TBD

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

## Grading 

Your final course grade will be made up of the following:

* Assignments/Projects: 50%
* Exams: 30%
* Final Exam: 15%
* Class Participation: 5%

The standard [University Grading Policy](http://app.kutztown.edu/policyregister/Policy/ACA-048) will be used to calculate your final letter grade. Your *lowest* quiz and homework grade will be dropped. 

*NOTE*: Even though the university uses 4.0 GPA scale in it's policy, grades will usually be displayed on a typical 100 point scale on D2L. 
You can convert from the 100 point scale to 4.0 GPA using the formula below, where **X** is the percentage.
$$\frac{X}{20}- 1 = GPA$$

**Exams/Quizzes:**

Exams and Quizzes times will be announced during class and must be taken during their scheduled time/location. Students who are unable to take the exam or quiz at the scheduled time for university approved reasons, **must do their best to contact the instructor before the start of it**. No make-ups will be allowed otherwise. For a list of approved reasons review the *Class Absence* section in the [Class Attendance](http://app.kutztown.edu/policyregister/Policy/ACA-016) university policy. 

**Homework (Assignments/Projects):**

Homework will be announced during class time. Most assignments will be submitted through D2L unless otherwise stated. Students will be allotted three (3) "free-late-days" during the semester. Students can use these days to submit assignments up to their remaining number of days late without penality. 

*For Example: Spike has submitted all his assignments on time, but forgot about the latest assignment. He decides to use two (2) of his "free-late-days" to work on the assignment and submit it. He'll recieve the same grade as if he had submitted it on time, but is now left with one (1) "free-late-days."*

Students without remaining "free-late-days" will no longer recieve credit on assignments submitted after the due date and time. Days are counted immediately after the due date and time. Meaning if an assignment is due at 11:59PM on Friday, an assignment submitted at 12:01AM Saturday will use one of your free days. 

*Continuing from above: Spike has once again forgotten about his assignment. He forgets that he had already used 2 of his 3 days and submits the assignment 2 days after it's due date. Since Spike only had one day left, the assignment will recieve a zero for late submission. Spike will also no longer have any "free-late-days".* 

# Course Policies

## COVID-19 Related

**Course Modularity:** This course is running a hybrid format with course content being presented simultaneously via Zoom and in the designated classroom. A rotation schedule will be provided before the start of the semester. Students can request to be allowed in the classroom everday if the room isn't at capacity. Students who have registered with the DSO and provided the instructor with their letter will be given priority. Students attending in-person are encouraged to bring a pair of wired earbuds/headphones in the case of group work on Zoom. These devices should be put away in all other cases. 

**Class Recording:** Most lectures will be recorded through the semester by the instructor. A recording consent form will be provided within the first week of class. 

**Masks:** Current research suggest that the use of face coverings helps reduce the spread of the COVID-19 causing virus. Students attending class in-person will be required to wear a mask/face covering properly (covering their nose and mouth) at all times. This policy expands to any classroom, public area, and common area on campus. Any student not wearing wearing a mask properly will be asked to leave the classroom and will still be responsible for any missed work. [Please refer to this link for more information](https://www.kutztown.edu/Departments-Offices/S-Z/StudentConduct/Documents/StudentConduct.PandemicResponseGuidelines.2020.pdf). In the case that a student refuses to wear a mask after being asked to so, the class will be moved online for that session. 

## Other Policies

### Attendance

Regular class attendance and participation is expected and highly encouraged. Students will be responsible for all materials covered during class time. 

### Collaboration

### Academic Dishonesty

### Classroom Etiquette

### Course Work / Accreditation

### E-Mail Correspondence

### Students with Disabilities

### Gender-Based Crimes

***NOTE:*** This document is subject to changes at the discretion of the instructor
