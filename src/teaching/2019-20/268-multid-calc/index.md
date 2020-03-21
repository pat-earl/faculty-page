infotable: 0
stylesheet: local.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

<div class='alert alert-info small' markdown='1'>
In response to the Caronavirus pandemic, all classes will be conducted remotely after 2020-03-16.
Lectures and office hours will be conducted via Zoom meetings at the regularly scheduled times using the following meeting IDs:

* All lectures and Gautam's office hours:
  [852971361](https://cmu.zoom.us/j/852971361).
* Ruoyuan's recitations and office hours:
  [3459083003](https://cmu.zoom.us/j/3459083003).
* Yuepeng's recitations and office hours:
  [4295886265](https://cmu.zoom.us/j/4295886265).

All assignments, and exams must be turned in using [Gradescope](https://www.gradescope.com/courses/97183).
More information can be found <a href='https://zym.math.cmu.edu/t/information-about-virtual-lectures'>here</a>.
</div>

{{course_info_table(course)}}

## Course Description

This course is a serious introduction to multidimensional calculus that makes use of matrices and linear transformations.
Students will be expected to write proofs; however, some of the deeper results will be presented without proofs.

### Learning Objectives

* Develop familiarity and a conceptual understanding of multi-variable differential and integral calculus.
* Become comfortable with mathematically rigorous proofs in this setting.

### Pre-requisites

* One variable calculus, at the level of [21-122](http://coursecatalog.web.cmu.edu/search/?P=21-122), and its pre-requisites.
* Linear algebra at the level of
  [21-241](http://coursecatalog.web.cmu.edu/search/?P=21-241)
  or [21-242](http://coursecatalog.web.cmu.edu/search/?P=21-242).

### Tentative Syllabus

* Functions of several variables, regions and domains, limits and continuity.
* Partial derivatives, linearization, Jacobian.
* Chain rule, inverse and implicit functions and geometric applications.
* Higher derivatives, Taylor's theorem, optimization, vector fields.
* Multiple integrals and change of variables, Leibnitz's rule.
* Line integrals, Green's theorem.
* Path independence and connectedness, conservative vector fields.
* Surfaces and orientability, surface integrals.
* Divergence theorem and Stokes's theorem.

### Textbook and References

Two references at the level of this course are:

* My brief lecture notes: for [[pdfs/notes.pdf|printing]] or for [[pdfs/notes-tablet.pdf|viewing online]].
* *Multivariable Mathematics: Linear Algebra, Multivariable Calculus, and Manifolds* by Shifrin. (Roughly at the level of this course; though we will cover topics in slightly different order.)

There are plenty of other references on the subject, and you may use any of them if they resonate with you better (or you have easier access).
Here are a few excellent references, which are at a level slightly higher than we will have time for in this course.

* *Advanced Calculus of Several Variables* by C. H. Edwards, Jr (roughly chapters 2 through 5; again at a level slightly higher than we will have time for in this course.)
* Lecture notes by [[../../2017-18/268-multid-calc/pdfs/canez-calculus.pdf|Santiago Canez]] (also available on his [website](http://www.math.northwestern.edu/~scanez/courses/320/notes/lecture-notes-320-3.pdf)). (These are a bit deeper / more through than we will have time for in this course.)
* The more analytically inclined can also use any of the references used for 269 [any of the references used for 269](../../2018-19/269-vector-analysis/index.html#textbook-and-references)

Finally, here are a few references at a level at the level lower than that of this course.

* [Khan Academy](https://www.khanacademy.org/math/multivariable-calculus). (Lots of examples, pictures, intuition; but not at the level of rigor that will be expected in this course.)
* *Calculus of one and several variables* by Salas, Hille, Etgen.  (Doesn't prove some of the important results,  but provides good intuition and examples.)
* *Calculus Volume 3* by Hermann, Strang. (At a level a bit lower than this course; but available for free on [OpenStax](https://openstax.org/subjects/math).)
* *Multivariable Calculus* by Stewart. (Typically used as a textbook in courses at the level of 259. Lots of examples and good intuition, but not at the level of rigor we use in this course.)

## Class Policies

### Lectures

* If you must sleep, <span class='text-danger'>don't snore!</span>
* Be courteous when you use mobile devices.

### Homework

* Homework must be turned in **at the beginning of class** on the due date.
* **Late homework policy:**
    - Any homework turned within the first hour of the deadline will be assessed a 20% penalty.
    - Any homework turned after the first hour past the deadline will be assessed a 100% penalty (i.e. you won't receive credit for this homework, but if practical, your homework may still be graded).
    - To account for unusual circumstances, the bottom 20% of your homework will not count towards your grade.
    - I will only consider making an exception to the above late homework policy if you have documented personal emergencies lasting at least **18 days**.
* I recommend starting the homework early.
  Most students will not be able to do the homework in one evening.
* I view homework more as a learning exercise as opposed to a test.
  Feel free to collaborate, use books and whatever resources you can find.
  I recommend trying problems independently first, and then seeking help on problems you had trouble with.
* I also strongly urge you to fully understand solutions before turning them
in.
  I will usually put a few homework problems on your exams *with a devious twist*.
  A through understanding of the solutions (even if you didn't come up with it yourself) will invariably help you.
  But knowledge of the solution without understanding will almost never help you.
* Nearly perfect student solutions may be scanned and hosted here, with your identifying information removed.
  If you don't want any part of your solutions used, please make a note of it in the margin of your assignment.


### Exams

* All exams are closed book, in class.
* No calculators, computational aids, or internet enabled devices are allowed.
* The final time will be announced by the registrar
  [here](https://www.cmu.edu/hub/courses/exams/index.html).
  <span class='text-danger'>
  Be aware of their schedule before making your travel plans.
  </span>

### Grading

* Homework will count as 20% of your grade.
  Moreover, <span class='text-danger'>between 25% and 50% of your exams will consist of (possibly modified) homework questions,</span> so I advise you to really understand the homework.
* The remainder 80% of your grade will be determined by your exams weighted as the *higher* of:
    - 20% for each midterm, and 40% final,
    - **or** 30% for your *better* midterm and 50% for the final,
* If you miss a midterm for some reason, I **will not** give you a makeup.
  Instead, I will count your other midterm as 30% and final as 50% using the second option above.

### Accommodations for Students with Disabilities

If you have a disability and have an accommodations letter from the Disability Resources office, I encourage you to discuss your accommodations and needs with me as early in the semester as possible. I will work with you to ensure that accommodations are provided as appropriate. If you suspect that you may have a disability and would benefit from accommodations but are not yet registered with the Office of Disability Resources, I encourage you to contact them at <access@andrew.cmu.edu>.

### Student Wellness

As a student, you may experience a range of challenges that can interfere with learning, such as strained relationships, increased anxiety, substance use, feeling down, difficulty concentrating and/or lack of motivation. These mental health concerns or stressful events may diminish your academic performance and/or reduce your ability to participate in daily activities. CMU services are available, and treatment does work. You can learn more about confidential mental health services available on campus [here](http://www.cmu.edu/counseling). Support is always available (24/7) from Counseling and Psychological Services: 412-268-2922.


### Faculty Course Evaluations

At the end of the semester, you will be asked to fill out faculty course evaluations.
Please fill these in promptly, I value your feedback.
As incentive, if over 75% of you have filled out evaluations on the last day of class, then I will release your grades as soon as they are available.
If not, I will release your grades at the very end of the grading period.
