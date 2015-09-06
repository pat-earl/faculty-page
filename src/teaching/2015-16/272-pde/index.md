{%- from dirname ~ '/course_info.j2' import course -%}
{%- from 'includes/macros.j2' import course_info_table -%}
title: {{course.title}}

{{ course_info_table(course) }}

## Course Description

A Partial Differential Equation (PDE for short), is a differential equation
involving derivatives with respect to more than one variable. These arise in
numerous applications from various disciplines. A prototypical example is the
heat equation, governing the evolution of temperature in a conductor.

This course will serve as a first introduction to PDE's, and will focus on the
simplest model equations that arise in real life. It will study both
analytical methods (e.g. separation of variables, Greens functions), numerical
methods (e.g. finite elements) and the use of a computer to compute and
visualize solutions. Time permitting, it will touch upon the mathematical
ideas behind phenomenon observed in real life (e.g. speed of wave propagation,
and or shocks in traffic flow).

### Tentative Syllabus

* Physical motivation of PDE's
    - Transport, heat, wave and Laplace equations.
    - Initial data, boundary conditions and classification of PDE's.
* Separation of variables and Fourier series.
    - Heat, wave and Laplace equations.
* Numerics and computation.
    - Ideas behind finite differences and finite elements.
    - Using software to compute (e.g. MATLAB)
* Newton potentials and Greens functions.
    - Computation in standard domains.
    - Harmonic functions: Maximum principle and mean value property.
* Heat kernel.
* Wave equation and finite speed of propagation.
* Burgers equation, characteristics and traffic flow.

### Prerequisites

Before taking this course you should have a good knowledge of ODE's and multi-variable calculus.
Few courses that cover these in sufficient detail are:

* **ODE's**: 33-232, 21-260 or 21-261.
* **Multi-variable calculus**: 21-259, 21-268 or 21-269.

It isn't imperative you have taken these courses; but it is imperative that you have a good understanding of the material in these courses.

### References

* [372 Lecture Notes Wiki](http://wiki.math.cmu.edu/iki/2014-372)
* *Introduction to Partial Differential Equations with MATLAB Corrected Edition*
  by Jeffery M. Cooper.
* *An Introduction to Partial Differential Equations 1st Edition*
  by Yehuda Pinchover, Jacob Rubinstein.
* *Introduction to PDE* by Walter Strauss.

## Class Policies

### Lectures

* If you must sleep, <span class='text-danger'>don't snore!</span>
* Be courteous when you use mobile devices.

### Homework

<div markdown='1' class='alert alert-warning' role='alert'>
**Note:**
As of 2015-08-30, we do not yet have a grader for this class.
If we are not assigned a grader, I might change the homework model completely.
</div>

* Homework must be turned in **at the beginning of class** on the due date.
* <span markdown='1' class='text-danger lead'>Late homework will **NEVER** be accepted. Really!</span>
* To account for unusual circumstances, the bottom 20% of your homework will not count towards your grade.
* Working in groups is encouraged, but solutions must be written up on your own.
* Nearly perfect student solutions may be scanned and hosted here, with your identifying information removed. If you don't want any part of your solutions used, please make a note of it in the margin of your assignment.


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
* <span class='text-danger'>Between 25% and 50% of your exams will consist of homework questions.</span>
* Your *better* midterm will count as 30% of your grade.
  (Your *worse* midterm will not count at all.)
* Your final will count as 50% of your grade.
