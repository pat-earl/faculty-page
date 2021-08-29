title: First Day Handout
{%- import 'includes/site.j2' as site -%}
{% from 'includes/macros.j2' import office_hours_table with context -%}
{% from get_file('course_info.j2') import course %}

## Course Information

**Course:** 
: <span id='course_code'>{{course.abv_title}}</span> {{course.abv_name}} <span hidden id='semester_code'>{{course.abv_semester}}</span>

**Semester:**
: Fall 2021

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
: Section 10: MWF 10:00AM - 10:50AM, GR307
: Section 20: MWF 11:00AM - 11:50AM, GR307

**Format:** 
: In-Person

## Materials

### Required Textbook

*Computer Networking: A Top-Down Approach*, James F. Kurose, Keith Ross, 7E. Pearson

You may also use the 6th or 8th editions of this textbook. 

**NOTE**: This book is part of KU Bookstore's inclusive access, the book will be charged to your tuition bill. 
You may opt-out of this program, read more here: <https://kubstore.com/inclusive-access>

## Description

Computer networks have become ubiquitous in our society. In depth understanding of their workings is an important part of the foundation of knowledge not only for a computer science student who intends to incorporate networking in their scholastic or professional endeavors, but for anyone working in the discipline, as networking concepts are applicable in many areas inside and outside the discipline. The students will learn the terminology and implementation of computer networks, and the physical components of networks, including cabling and devices, as well as how these components work. Several application layer protocols will also be studied, including HTTP, E-mail, DNS and DHCP. 

## Learning Objectives

1. Demonstrate an understanding of various hardware used to permit networks to communicate, , such as hubs, switches, access points, and routers.
2. Summarize the layers of the OSI and Internet architecture stacks.
3. Describe how several common application-layer protocols work, such as HTTP, FTP SMTP and DNS.
4. Summarize the workings of the two primary transport-layer protocols, TCP and UDP.
5. Summarize the network-layer functionality, including IP, the primary protocol for that layer
6. Employ various network tools to observe the behavior of networks.

## Course Prerequisites

(CSC237 or CSC253) AND Junior Status

## Grading 

Your final course grade will be made up of the following:

* Assignments: 50%
* Exams (2): 30%
* Final Exam: 15%
* Class Participation: 5%

The standard [University Grading Policy](http://app.kutztown.edu/policyregister/Policy/ACA-048) will 
be used to calculate your final letter grade. 

*NOTE: Even though the university uses the 4.0 GPA scale in it's policy, 
grades will be displayed and reported on a typical 100 point scale.*

**Class Participation:**
: Grade is based off regular class attendance and participation in discussions.

**Exams/Quizzes:**

: Exams will be announced during class and must be taken during their scheduled time/location.
: Missed exams/quizzes will be handled on a case-by-case basis. For a list of approved reasons review the *Class Absence* section from the [Class Attendance](http://app.kutztown.edu/policyregister/Policy/ACA-016) University policy. 

**Homework (Assignments/Projects):**
: This policy is adopted from this [first day handout](https://csit.kutztown.edu/~schwesin/fall20/csc223/syllabus.html).

: All homework submissions must include the following information: your name, the course,
semester, year, and assignment number/name. Programming assignments must follow the 
[Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf) set by the CS&IT Department. Failure to meet these 
requirements will result in a minimum 10% penalty for that assignment.

: Homework is due at the specified date and time, with a penalty of 10% for each day late.
Homework can be at most up to three (3) days late. Students have a budget of three (3) grace days
for the course. Grace days will work as followed:

* Some homework may not be eligible for these grace days and will be marked as such in the homework's
handout.
* Grace days will be automatically applied until you run out.
* If your last submission is one day late and you have at least one day remaining, then you will
receive full credit for the assignment and automatically spend one grace day.
* Once you have spent your grace days, you will start receiving the 10% penalty. 
* No submission will be accepted more than three (3) days late.


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
