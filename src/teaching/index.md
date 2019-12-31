{%- from 'teaching/courses.j2' import courses, old_teaching, md_current_courses_long -%}
{%- from 'teaching/sections.j2' import secs -%}
title: Teaching

## {{secs.current_courses}}

{{ md_current_courses_long() }}

## {{secs.previous_courses}}

These are websites from all courses I have taught at CMU.
The homework, exams and syllabus should be accessible to anyone.
Solutions, however, are restricted to CMU faculty.

{% for (cn, ct, rest) in courses -%}
* *<span class='text-nowrap'>{{(cn ~ ': ') if cn else ''}}{{ct}}.</span>*
  {%- for (cy, cs, cl) in rest -%}
    <a class='text-nowrap' href='{{cl}}'>
      {{ 'Spring' if cs == 's' else
          ( 'Fall' if cs == 'f' else cs ) }}
      {{cy-}}
    </a>
    {%- if loop.last %}.{% else %}, {% endif %}
  {%- endfor %}
{% endfor %}

## {{secs.lecture_notes}}

All these notes are <span class='text-info'>free and open source</span>. You may modify and or use them for your own purposes, as long as you follow the licence terms.

* **Multi-variable Calculus**
    * [[2015-16/268-multid-calc/pdfs/brief-notes.pdf|Brief lecture notes]] (from Fall 2015).
    * [Class website](2015-16/268-multid-calc) for problems and references.
    * [LaTeX source](https://gitlab.com/gi1242/cmu-math-268).
      <div class='mb-2'></span>
* **Undergraduate PDE**
    * [Lecture notes wiki](http://wiki.math.cmu.edu/iki/2014-372/)
    * [Class website]({{old_teaching}}/2013-14/372-pde/) for problems and references.
      <small>
        I have typed solutions to all problems, which I can share with other <em class='text-warning'>instructors</em> who are interested.
      </small>
    * [Source code](http://wiki.math.cmu.edu/gitweb-pub/?p=2014-372-wiki.git;a=summary).
      <small>
        (These notes are hosted using [ikiWiki](https://ikiwiki.info/).)
      </small>
      <div class='mb-2'></span>
* **Stochastic Calculus for Finance**
    * [[2017-18/944-scalc-finance1/pdfs/notes.pdf|Brief lecture notes]] (from Fall 2017).
    * [Class website](2017-18/944-scalc-finance1) for problems and references.
    * [LaTeX source](https://gitlab.com/gi1242/cmu-mscf-944).
      <div class='mb-2'></span>

## {{secs.student_projects}}

### {{secs.phd_thesis}}

* Samuel Cohn,
  *[[pdfs/201808-sam.pdf|On the Homogenization of Diffusions in Periodic Comb-like Structures]]*,
  2018.
* Yuanyuan Feng,
  *[[pdfs/201908-yuanyuan.pdf|Dissipation Enhancement by Mixing]]*,
  2019.

### {{secs.masters_thesis}}

* [James T. Murphy III](http://intfxdx.com/),
  *Resolving the one-dimensional autonomous flow-free explosion problem*
  (published in [SIURO](http://www.siam.org/students/siuro/vol7/index.php)
  [here](http://www.siam.org/students/siuro/vol7/S01319.pdf)),
  2014.

### {{secs.student_lecture_notes}}

These lecture notes have been <span class='text-info'>written entirely by students</span> while taking courses taught by me.
My only contribution is teaching the course and setting up the websites to host them.

You are free to edit, modify and redistribute these notes (under the terms stated in the respective licenses).

* **Measure Theory:**
    * [Lecture notes by Eugene Choi (2013/14)]({{old_teaching}}/2013-14/720-measure/pdfs/eugenes-notes.pdf)
    * [Lecture notes by Adam Gutter (2014/15)]({{old_teaching}}/2014-15/720-measure/pdfs/adams-notes.pdf)
    * [The LaTeX source for both notes](http://wiki.math.cmu.edu/gitweb-pub/?p=201312-measure.git;a=summary)
    * [Class website]({{old_teaching}}/2014-15/720-measure/) for problems and reference.
    <div class='mb-2'></div>

* **Stochastic Calculus:**
    * [Lecture notes wiki](https://lecturenotes.math.cmu.edu/mediawiki/index.php/Stochastic_Calculus_(Fall_2012))
      by Ryan Murray, Jimmy Murphy and others.
    * [Class website]({{old_teaching}}/2013-14/880-scalc/) for problems and references.

