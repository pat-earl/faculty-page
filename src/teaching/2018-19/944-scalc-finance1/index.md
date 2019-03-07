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
  <br>
  <span class='small'>
    **Note:** I am currently (Spring 2019) updating these notes.
    While the bulk of the matter and later parts of the notes should be largely unchanged, the first few chapters will be changed as the semester progresses.
    If you want to be notified of changes, you should create an account on [GitLab](http://gitlab.com), and watch the repository [gi1242/cmu-mscf-944](https://gitlab.com/gi1242/cmu-mscf-944).
  </span>
* [Stochastic Calculus for Finance II](http://www.springer.com/us/book/9780387401010) by Steven Shreve.
  *(We will cover roughly the first five chapters.)*

## Class Policies

### Lectures

* If you must sleep, <span class='text-danger'>don't snore!</span>
* Be courteous when you use mobile devices.

### Homework

* Homework is due **at the beginning of class** on the due date.
* <b class='text-danger'>Late homework policy:</b> Homework turned in
  within 48 hours of the deadline will be accepted.
    - Late homework turned in within the first 24 hours of the deadline will receive a <b class='text-warning'>10% penalty</b>.
      In particular, homework turned in even one nanosecond after class starts, will receive this penalty.
    - Late homework turned in within the next 24 hours will receive a <b class='text-warning'>25% penalty</b>.
    - Homework more than 48 hours late will not be accepted.
    - To account for unusual circumstances, your lowest homework will not count towards your grade.
    - I will only consider making exceptions to the late homework policy for unexpected severe emergencies that require your absence for more than 12 days.
      <b class='text-warning'>Following MSCF policy, I will not make exceptions on account of job interviews or career fares.</b>
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

* Your performance on the homework, midterm and final will each be converted to a numerical grade 0 and 4.5 "using a curve".
* Your overall grade will be computed as the higher of the following:
    1. Final 60%, midterm 30% homework 10%,
    2. (Final 90%, homework 10%), reduced by one full letter.
* Explicitly, if $F$, $M$, and $H$ are your numerical grades on the final, midterm, and homework respectively, then your overall grade $G$ will be computed by
$$
    G = \max( 0.6 F + 0.3 M + 0.1 H, (0.9 F + 0.1 H) - 1.00 )\,.
$$
* Your final letter grade will be computed from your numerical grade using [the standard scale](https://www.cmu.edu/policies/student-and-student-life/grading.html).

[MSCF student handbook]: https://www.cmu.edu/mscf/portal/docs/2017-2018%20MSCF%20Handbook.pdf
