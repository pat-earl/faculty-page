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
: OM159, Tues/Thurs 3:00PM - 4:20PM


**Format:** 
: Hybrid (Sync In-Person/Zoom)

## Materials

### Required Textbook

* *Computer Forensics and Cyber Crime*, 3rd Edition. Marjie Britz. **ISBN:** 978-0132677714
    * *Textbook is available through [inclusive access](https://kubstore.com/inclusive-access)*

## Description

This course is an introduction to the basic concepts of computer forensics.  It will teach the student how to identify, preserve, recover, analyze and document data on a computer or network allegedly used to commit a crime.  Topics include computer architecture, operating systems, encryption/decryption, preserve and document evidence, and analyzing computers and networks for evidence.  


## Objectives

1. Summarize the importance of security for computer and network systems.
2. Describe the role of computer forensics in an alleged crime.
3. States a basic knowledge of computers and networks.
4. Explain the ethic and social implications of technology.
5. Describe the major security threats and vulnerabilities to computers and networks, including viruses, worms, and trojans.
6. Explain basic encryption and decryption techniques.
7. Explain basic hacker techinques and how to defend against them.
8. Describe how to preserve and critical evidence in computers and networks.
9. Demonstrate the ability to perform a basic analysis for computer forensics using various tools.

## Grading 

Your final course grade will be made up of the following:

* Semi-Weekly Quizzes: 15%
* Exams: 25%
* Assignments/Projects: 40%
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

**Attendance:**
: Regular class attendance and participation is expected and highly encouraged. Students will be responsible for materials covered during class time. 

**Academic Dishonesty:**
: All course work must be your own. Any student copying or giving work to another student will recieve
a zero for that assignment and will be refered to the department chairperson. Repeat offenses will
be referred to the *Student Conduct Board*. It's the student's responsibility to be fimilar with the
Computer Science & Information Technology Department's Academic Integrity Policy and the University's
Academic Honesty Policy (ACA-027). Copies of these policies are available on the university's website.

**Classroom Etiquette:**
: Respect for your classmates, instructor, and the class is expected. Please come to class on time
and prepared to learn. Coming and going during class should be limited to unavoidable situations.
**Electronic devices should not be seen or heard**, unless being used for class activites, note taking,
etc. Using your cell phone to take pictures of lecture notes, is not a valid purpose. There should be
no classroom converstations, sleeping (with snoring), or general disruptions during class.

**Course Work / Accreditation:**
: Any coursework submitted to the instructor (included by not limited to assignments, tests, and
projects) may be photocopied and retained for the purpose of assessment, accreditation and 
quailty improvment. 

**E-Mail Correspondence:**
: The best way to contact the instructor is via e-mail (earl@kutztown.edu). You are required to use
your Kutztown University supplied e-mail for all correspondence, outside email services will be 
ignored. Your email should be professionally written and use a relevant subject line. Addtionally,
any emails relating to this course must include the course prefix and number at the beginning of the 
subject line. For Example: If you're in the course CSC101, your subject line should be similar to
these examples:

* "[CSC101] Question on Assignment 1"
* "CSC101 - Question on Assignment 1"

E-mails that follow these guidelines can expect a response within 48 business hours. 

**Students with Disabilities:**
: Students with diagnosed disabilities or special needs that require accommodations for this course
must first contact the Disability Services Office, (Office of Human Diversity at 
215 Stratton Administration Building.) Do this as soon as possible so that we may have a dialogue as
to your needs and the recommended accommodations. Accommodations cannot be given until the 
instructor has seen your letter. Accommodations cannot be retroactivly applied. 

**Gender-Based Crimes:**
: Educators must report incidents of gender-based crimes, including sexual assault, sexual harassment, 
stalking, dating violence, and domestic violence. If a student discloses such incidents to me during 
class or in a course assignment, I am not required to report the disclosure, unless the student was 
a minor at the time the incident occurred. Regardless of the student’s age, if the incident is disclosed 
to me outside the classroom setting or a course assignment, I am required by law to report the disclosure, 
including relevant details, such as the names of those involved in the incident, to Public Safety 
and Police Services and to Mr. Jesus Peña, Title IX Coordinator.

***NOTE:*** This document is subject to changes at the discretion of the instructor
