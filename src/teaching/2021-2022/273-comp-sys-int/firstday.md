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
: Tues/Thur 1:30PM - 2:50 PM OM159

**Format:** 
: In-Person

## Materials

### Recommended Textbooks

*Modern Systems Analysis and Design*, 9th Edition. Joseph S Valacich, Joey F. George. Pearson. *ISBN*: 9780135172759

## Description

This course focuses on the integration of information systems in organizations, which is the process by which different computing systems and software applications are interconnected. It examines the strategies, methodologies, and implementation for combining interdependent systems, enabling two or more applications to interact and exchange data seamlessly. The course will explore various trends in computing system integration, including Enterprise Resource Planning (ERP) software, cloud computing, and mobile integration. 


## Course Prerequisites

CSC237 or CSC253

## Grading 

Your final course grade will be made up of the following:

* Assignments: 50%
* Exams (2) : 30%
* Final Exam: 15%
* Class Participation: 5%

The standard [University Grading Policy](http://app.kutztown.edu/policyregister/Policy/ACA-048) will 
be used to calculate your final letter grade. 

*NOTE: Even though the university uses the 4.0 GPA scale in it's policy, 
grades will be displayed and reported on a typical 100 point scale.*

**Class Participation:**
: Grade is based off regular class attendance and participation in discussions.

**Exams**

: Exams will be announced during class and must be taken during their scheduled time/location.
: Missed exams will be handled on a case-by-case basis. For a list of approved reasons review the *Class Absence* section from the [Class Attendance](http://app.kutztown.edu/policyregister/Policy/ACA-016) University policy. Please contact the instructor to discuss the possibility of making up an exam. Be aware that you may be asked to provide evidence supporting an approved absence reason.  

**Homework (Assignments/Projects):**
: All homework submissions must include the following information:
Your Name(s), The Course, Semester, Year, and Assignment/Project Number or Name.
Homework can be submitted up to two days late, with a 10% penalty applied
each day.

# Course Policies

**Healthy Practices and Mask Information:**
: Students should take reasonable action to reduce the possibility
of transmission of communicable illnesses, such as COVID-19. Proactive
actions include washing hands frequently, using wipes to clean personal
classroom seating area, covering coughs and sneezes with a tissue or 
elbow, and staying home when feeling ill. It is appropriate to contact the
instructor (before class if possible) and to ask a classmate for notes when 
missing class due to illness. In the event of a medical emergency and/or
hospitalization that prevents a student from attending class or being on 
campus for five (5) days or more, including a positive COVID test from an
off-campus medical facility, Health and Wellness/Clinical Services should be
contacted at 610-683-4082 or <health@kutztown.edu>

: **Masks are required inside all university buildings for all individuals,
regardless of vaccination status.**

* Individuals are required to wear masks indoors, including all classrooms, 
meeting rooms, common areas in residence halls and indoor events. 
* Masks are not required outdoors. CDC recommends that people who are not 
fully vaccinated wear a mask in crowded outdoor settings. The university
supports all members of the campus community who choose to wear a mask outdoors.
* Mask must cover the nose and mouth

: **Masks will remain required while the CDC advises that they be worn in our
area.** Should the situation improve, the university will adjust its 
protocols to align with current CDC guidance, and all individuals will
be strongly encouraged to wear a mask while indoors. 


**Attendance:**
: Regular and timely class attendance is expected and highly encouraged. Students are responsible for materials covered during class time. Students
who will be missing class for extended periods of time, due to illness,
university excused reasons, etc., should contact the instructor as soon as
possible. 

**Attendance Verification:**
: Attendance status will be submitted to University Administration
during the following periods: 

* 1st Period: Wed 2/02 - Tues 2/08
* 2nd Period: Mon 3/21 - Fri 3/25

: Attendance will not be tracked otherwise and students should refer to the
general guidelines above. 
: For more information, please refer to [University Policy ACA-090](https://apps.kutztown.edu/SZ_001_POLICY_REGISTER/Policy/ACA-090))

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
