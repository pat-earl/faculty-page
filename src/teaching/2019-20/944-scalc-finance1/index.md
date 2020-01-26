## Course Description

The first half of this course introduces martingales, Brownian motion, Itô integrals and Itô's formula, in both the uni-variate and multi-variate case.
This is done within the context of the Black-Scholes option pricing model and includes a detailed examination of this model.
The second half of the introduces exponential martingales and the Girsanov theorem.
This is done in the context of risk neutral measures and the fundamental theorems of asset pricing.

{% if false -%}
This is a first course in stochastic calculus for finance.
It assumes students have taken the courses 
[46-921: Introduction to Probability](http://tepper.cmu.edu/prospective-students/course-page/46921/mscf-probability)
{# [46-956: Introduction to Fixed Income](https://www.cmu.edu/mscf/academics/curriculum/46956-fixed-income.html) -#}
and
[46-941: Multi-Period Asset Pricing](http://tepper.cmu.edu/prospective-students/course-page/46941/multi-period-asset-pricing).
This course revisits the ideas of no-arbitrage pricing and risk-neutral probability measures
{#- covered in
[956](https://www.cmu.edu/mscf/academics/curriculum/46956-fixed-income.html)
and
[941](http://tepper.cmu.edu/prospective-students/course-page/46941/multi-period-asset-pricing),
#}
in a continuous-time context.

The applications in this course are primarily to equity derivatives.
In particular, the Black-Scholes partial differential equation and formula are developed in detail.
The stochastic calculus content of the course is also the foundation for fixed income, foreign exchange, commodity, and even credit derivative models.

Topics covered by the course are probability theory in general spaces, independence and conditioning, Brownian motion, Itô integrals and the Itô formula, the Black-Scholes formula, change of measure, and the Fundamental Theorems of Asset Pricing.

The sequel to this course,
[Stochastic Calculus for Finance II](http://tepper.cmu.edu/prospective-students/course-page/46945/stochastic-calculus-ii)
, discusses risk-neutral pricing in more detail, the relationship between stochastic calculus and partial differential equations, and interest rate term-structure models.
{% endif %}


### Prerequisites

* [46-921: Introduction to Probability](http://tepper.cmu.edu/prospective-students/course-page/46921/mscf-probability)
* [46-941: Multi-Period Asset Pricing](http://tepper.cmu.edu/prospective-students/course-page/46941/multi-period-asset-pricing)

### References

* [[pdfs/notes.pdf|Brief lecture notes]].
  (A tablet friendly version is [[pdfs/notes-tablet.pdf|here]], and the full TeX source is [here](https://gitlab.com/gi1242/cmu-mscf-944).)
  {#-
  <br>
  <span class='small'>
    **Note:** I am currently (Spring 2019) updating these notes.
    While the bulk of the matter and later parts of the notes should be largely unchanged, the first few chapters will be changed as the semester progresses.
    If you want to be notified of changes, you should create an account on [GitLab](http://gitlab.com), and watch the repository [gi1242/cmu-mscf-944](https://gitlab.com/gi1242/cmu-mscf-944).
  </span>
  #}
* [Stochastic Calculus for Finance II](http://www.springer.com/us/book/9780387401010) by Steven Shreve.
  *(We will cover roughly the first five chapters.)*

## Class Policies

### Lectures

* If you must sleep, <span class='text-danger'>don't snore!</span>
* Be courteous when you use mobile devices.
* **Attendance Requirement:** The steering committee has requested attendance be recorded and made a part of your grade.
  Accordingly, attendance will count as 5% of your overall grade, and will be computed as follows:
    - To account for interviews and other special circumstances, you may miss up to 4 lectures without penalty.
    - Missing more than 4 lectures will decrease the attendance portion of your grade proportionally.
    - I will only consider making exceptions to this policy for unexpected severe emergencies that require your absence for more than 12 days.

### Homework

* Homework is due **at the beginning of class** on the due date.
* <b>Late homework policy:</b> Homework turned in
  within 48 hours of the deadline will be accepted.
    - Late homework turned in within the first 24 hours of the deadline will receive a *10% penalty*.
      In particular, homework turned after class starts, will receive this penalty.
    - Late homework turned in within the next 24 hours will receive a *20% penalty*.
    - Homework more than 48 hours late will not be accepted.
    - To account for unusual circumstances, your lowest homework will not count towards your grade.
    - I will only consider making exceptions to the late homework policy for unexpected severe emergencies that require your absence for more than 12 days.
      *Following MSCF policy, I will not make exceptions on account of job interviews or career fares.*
* Solutions will usually be posted 48 hours after the homework deadline.
  Due to holidays or exams solutions to some assignments might post earlier.
  In this case, you will be notified of this in advance, and late homework **will not** be accepted after solutions have been posted.
* Your homework must be uploaded as a PDF on Canvas.
  If you use pencil and paper to write your homework, then you must scan and upload it.
  Please ensure your scans are a *high quality* PDF, as *photos of your homework will not be accepted.*
* You may collaborate on the homework, however, you may only turn in solutions which you fully understand and have written up independently.
  Violation of this policy will be treated seriously according to procedures in the [MSCF student handbook].

### Exams

* No notes, calculators, computational aids, or internet enabled devices are allowed during exams.
* You may not give or receive assistance during exams.
* Violation of these policies will be treated seriously according to procedures in the [MSCF student handbook].
* If you earn a *C+* or lower, and have at least a 70% average on the homework, you may take the makeup final.
  Your performance on the makeup final can not reduce your grade, and can only increase your grade in the course by at most a full letter, up to a maximum of *B--*.
* **Regrading Policy:**
    * Your graded exams will be with your TA for Pittsburgh students, and in the MSCF office for NY students.
      You may view them in the respective office.
      However if you take them out of the office you may not request regrading of any problems.
    * If you believe a particular question has been graded incorrectly, then you must do so in writing by leaving a post-it note on the front of the exam indicating which question you want re-graded.
      *Please do **NOT** include any explanation or message.*
      Your grade will be solely based on our interpretation of what is written on the exam, and not on any explanation you provide outside the exam.
    * We will cover up the original grade, and independently regrade the requested question.
      The new grade will replace your old grade, <span class='text-danger'>**even if it is lower**</span>.
      I strongly recommend you read and understand the solutions posted online before requesting a regrade, because **your grade could become lower**.

### Grading

* Attendance will count as 5% of your grade, and homework will count as 10%.
* The remainder 85% of your grade will be determined by your midterm and final, as the higher of:
    - Final 60% and midterm 25%.
    - **or** Final 85%, *reduced by one full letter*.
* That is, if you miss the midterm, I will count your Final as 85%, and assess a *full letter grade penalty*.
* Explicitly, your grade will be computed as follows:
    - Your performance on the homework, midterm and final will each be converted to a numerical grade between 0 and 4.5 "using a curve".
    - If $F$, $M$, $H$ and $A$ are your numerical grades on the final, midterm, homework and attendance respectively, then your overall grade $G$ will be computed by
      $$
          G = .05A + .1H + \max( 0.6 F + 0.25 M, 0.85 (F - 1) ) \,.
      $$
    - Your final letter grade will be computed from your numerical grade using [the standard scale](https://www.cmu.edu/policies/student-and-student-life/grading.html).

### Accommodations for Students with Disabilities

If you have a disability and have an accommodations letter from the Disability Resources office, I encourage you to discuss your accommodations and needs with me as early in the semester as possible. I will work with you to ensure that accommodations are provided as appropriate. If you suspect that you may have a disability and would benefit from accommodations but are not yet registered with the Office of Disability Resources, I encourage you to contact them at <access@andrew.cmu.edu>.

### Student Wellness

As a student, you may experience a range of challenges that can interfere with learning, such as strained relationships, increased anxiety, substance use, feeling down, difficulty concentrating and/or lack of motivation. These mental health concerns or stressful events may diminish your academic performance and/or reduce your ability to participate in daily activities. CMU services are available, and treatment does work. You can learn more about confidential mental health services available on campus [here](http://www.cmu.edu/counseling). Support is always available (24/7) from Counseling and Psychological Services: 412-268-2922.


### Faculty Course Evaluations

At the end of the semester, you will be asked to fill out faculty course evaluations.
Please fill these in promptly, I value your feedback.
As incentive, if over 75% of you have filled out evaluations on the last day of class, then I will release your grades as soon as they are available.
If not, I will release your grades at the very end of the grading period.

[MSCF student handbook]: https://canvas.cmu.edu/courses/3194/pages/MSCF%20Handbooks?titleize=0
