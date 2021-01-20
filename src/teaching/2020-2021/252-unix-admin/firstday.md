title: CSC252-020 First Day Handout
stylesheet: ../../firstday.css
{%- import 'includes/site.j2' as site -%}
{% from 'includes/macros.j2' import office_hours_table with context -%}
{% from get_file('course_info.j2') import course %}



# Course Information

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
: <https://csit.kutztown.edu/~earl/s>

**Office Hours:**
{% for day,time in site.office_hours.items() -%}
: <strong>{{day}}:</strong> {{time}}
{% endfor %}

Always refer to my website for the latest office hours.

**Meetings:** 
: OM 159, Tues/Thurs 4:30 PM - 5:50 PM

**Format:** 
: Hybrid (Sync In-Person/Zoom)

## Materials

**Required Textbook:**
: *A Practical Guide to Linux: Commands, Editors, and Shell Programming*, 4<sup>th</sup> Edition.
Mark G. Sobell. **ISBN:** 978-0134774602. (3<sup>rd</sup> edition is fine as well).  


## Description

This course deals with the study of the UNIX operating system, particularly, systems programming and administration.  Under the former, such topics as UNIX commands, filters, shell scripts, system security, user accounts, system backup and rebooting, and associated utilities are studied.  In addition, software procurement, and installation will be illustrated.  Meaningful applications, which illustrate the topics, will be given.

## Objectives

1. Define basic terminology used in UNIX and converse in terms commons to UNIX.
1. Explain the tasks associated with UNIX system administration.
1. Demonstrate the ability to find, download, and install appropriate software, e.g. compilers, specialized servers, editors, and other utilities for the users. 
1. Understand the use of signals and pipes.
1. Solve practical problems using various UNIX utilities. 
1. Demonstrate effective oral communication by presenting a UNIX topic.

## Grading 

Your final course grade will be made up of the following:

* Assignments/Projects: 50%
* Exams: 25%
* Final Exam: 20%
* Class Participation: 5%

The standard [University Grading Policy](http://app.kutztown.edu/policyregister/Policy/ACA-048) will be used to calculate your final letter grade. 

*NOTE: Even though the university uses the 4.0 GPA scale in it's policy, 
grades will be displayed and reported on a typical 100 point scale.*

**Class Participation:**
: Grade is based off regular class attendance and participation in discussions.

**Exams/Quizzes:**

: Exams and Quizzes times will be announced during class and must be taken during their scheduled time/location. Students who are unable to take the exam or quiz at the scheduled time for university approved reasons, **must do their best to contact the instructor beforehand**. 
Missed exams/quizzes will be handled on a case-by-case basis. For a list of approved reasons review the *Class Absence* section from the [Class Attendance](http://app.kutztown.edu/policyregister/Policy/ACA-016) University policy. 

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

## COVID-19 Related

**Course Modularity:** 
: This course will integrate in-person (face-to-face) and synchronous online (Zoom) learning experiences.
Students may freely select the mode of instruction in which they participate on each class meeting day.
Students who wish to attend class in-person some or all meeting days, should inform the instructor 
of their intent to do so, to prevent the classroom from going over capacity. Students attending
remotely are required to log in for synchronous instruction via Zoom during the scheduled
course meeting times. Links to the Zoom meeting room can be found on the course's webpage and 
D2L course.

**Class Recordings:** 
: Most, if not all, class lectures will be recorded for educational purposes. A consent form will
be provided to students before or during the first scheduled class meeting. Students may withdraw
their consent at anytime during the semester by informing the instructor in an email. Students who 
do not want their comments recorded may remain silent (no audio) and use private chats sent to the
instructor. Any and all questions about this policy should be sent to the instructor. Recordings will
only be available to students in the course with a documented and university excused absence. 

**Masks:** 
: Current research suggest that the use of face coverings helps reduce the spread of the COVID-19 causing virus. Students attending class in-person will be required to wear a mask/face covering properly (covering their nose and mouth) at all times. This policy expands to any classroom, public area, and common area on campus. Any student not wearing wearing a mask properly will be asked to leave the classroom and will be responsible for any missed work. [Please refer to this link for more information](https://www.kutztown.edu/Departments-Offices/S-Z/StudentConduct/Documents/StudentConduct.PandemicResponseGuidelines.2020.pdf). In the case that a student refuses to wear a mask after being asked to so, the class will be moved online for that session. 


## Other Policies

**Attendance:**
: Regular class attendance and participation is expected and highly encouraged. Students will be responsible for materials covered during class time. 

**Academic Dishonesty:**  

: You should be aware of the 
[Computer Science & Information Technology Department's Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
and the [University's Academic Dishonesty Policy](https://app.kutztown.edu/policyregister/policy.aspx?policy=ACA-027)

: The rest of this policy is adapted from these two syllabi: [1](https://csit.kutztown.edu/~schwesin/fall20/csc223/syllabus.html)
and [2](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f19/www/syllabus/syllabus.pdf). 
This policy is based on the following beliefs:

* Developing programs from scratch, or with limited starting code, requires using design
principles and logical thinking that are much deeper than what can be obtained by copying
and modifying an existing implementation. Making use of unauthorized sources diminishes the 
educational value of an assignment. 
* Although teamwork and collaboration are important real-world skills, it is important to first gain
the core competencies that enable individuals to serve as effective team members. This course is
designed to to teach and assess these core competencies. Unauthorized collaboration diminishes the 
educational experience and the reliability of assessments. 
  
: Based on these principles, here are guidelines on what forms of resource use, resource sharing,
and collaboration are permitted in this course. 

: **Exams:** Each exam must be the sole work of the student taking it. No collaboration of any form
is allowed on exams. Students may not discuss any aspect of any exam question with someone who
has not yet taken the exam.

: **Assignments and Information Sources:** As a general rule, you may not obtain any information
about an assignment from an unauthorized source. Clarifications as to which sources are authorized
and which are not are as follows:

* **Copying:**
    * You **may** use material that is explicitly provided for the assignment. No attribution is
required.
    * You **may** use other course material, including lectures and material from the course website,
but you must provide clear attribution, including the source and where the included material
begins and ends.
    * You **may** use materials from the course textbook(s). For any such use involving code you 
must provide clear attribution, including the source and where the included material begins
and ends.
    * You **may not** obtain code or other solution information from an unauthorized external source,
including web pages, code repositories, blog posts, etc.


* **Searching:** 
    * You **may** search for or refer to general information including the use of systems,
    networks, compilers, program libraries, library databases, and documentation.
    * You **may not** search the Web for solutions or for any advice on how to solve an assignment.


* **Reusing:**
    * You **may** reuse elements of general knowledge from prior courses. For example, you may use
    existing code for a linked list or to process command line arguments. For any such use involving
    code, you must provide clear attribution, including the source, and where the included
    material begins and ends.
    * If you have worked on a specific assignment in a previous semester, then you should arrange
    a meeting with the course instructor to devise a policy on which parts of your solutions you
    may use. Reuse without explicit permission of an instructor, even if it is your own code,
    is forbidden.


* **Using other’s code or documents:**
    * You **may not** look at someone else’s code (or other documents). This includes one person looking at the code and describing it to another.
    * You **may not** make use of any information about the assignment posted online except for the authorized sources listed above.


* **Assistance:**
    * You **may** get assistance on an assignment from the instructors, graduate assistants, and university tutors.
    * You **may only** get high-level strategic advice from others, including current and former students. Forbidden forms of advice include anything more detailed than a brief verbal description or block diagram, any kind of code or pseudo-code, explicit directions on how to assemble allowed blocks of code, and code-level debugging assistance.
   

: **Assignments and Collaboration:** As a general rule, you may not provide detailed help with an assignment other students. Clarifications about which forms of aid are authorized and which are not are as follows:

* **Sharing:**
    * You **may not** supply a copy of a file or document to an individual student or via a public channel, such as a blog post.


* **Providing access:**
    * You **may not** have any of your solution files in unprotected directories or in unprotected code repositories.


* **Coaching, Assisting, and Collaborating:**
    * You **may not** provide electronic, verbal, or written descriptions of code or other solution information.
    * You **may** clarify ambiguities or vague points in class handouts or textbooks.
    * You **may** help others use the computer systems, networks, compilers, debuggers, profilers, code libraries and other system facilities.
    * You **may** discuss and provide general strategic advice about an assignment. Providing anything more detailed than a brief description or block diagram is not allowed. Providing any kind of code or pseudo-code is not allowed.
    * You **may** provide suggestions of potential bugs based on high-level symptoms. Code-based debugging assistance is forbidden.


: **Enforcement:** Assignments will be closely monitored for plagiarism. All infractions will be reported to the department chair. The penalty for cheating will be determined on a case-by-case basis, **but it will always be worse than having not turned in the assignment.**

**Classroom Etiquette:**
: Respect for your classmates, instructor, and the class is expected. Please come to class on time
and prepared to learn. Coming and going during class should be limited to unavoidable situations.
**Electronic devices should not be seen or heard**, unless being used for class activities, note taking,
etc. Using your cell phone to take pictures of lecture notes, is not a valid purpose. There should be
no classroom conversations, sleeping (with snoring), or general disruptions during class.

**Zoom Etiquette:**
: Due to the hybrid nature of this course, Zoom participates are expected be professional and 
behave as if in the classroom. Below are some guidelines to keep in mind while attending on Zoom:

* Use of your webcam is not required and should be off to avoid disrupting participates with 
poor internet connections.
* Mute yourself unless you are speaking. Background noise is distracting to meeting participants.
* Be mindful of your physical and virtual surroundings. When using your mic, mute other applications
on your computer and your phone. While not always possible, make your best effort to attend class
in a quiet and distraction free environment. 
* Headphones/earbuds greatly reduce accidental feedback when using your microphone.
* Parliamentary rules always apply. If you want to participate in the discussion, you should raise
your (virtual) hand or type your question in chat and wait for the speaker to recognize you. 
You may interrupt the speaker if they do not recognize your message or raised hand in a reasonable 
amount of time. (e.g. Moving on to the next topic.)

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
