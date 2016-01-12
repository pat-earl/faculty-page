{%- from 'teaching/courses.j2' import courses, old_teaching, md_current_courses_long -%}
{%- from 'teaching/sections.j2' import secs -%}
title: Teaching

## {{secs.courses}}

### {{secs.current_courses}}

{{ md_current_courses_long() }}

### {{secs.previous_courses}}

These are websites from all courses I have taught at CMU.
The homework, exams and syllabus should be accessible to anyone.
Solutions of more recent courses should be accessible to CMU faculty.

<dl class='dl-horizontal'>{# {{{ #}
  {% for (cn, ct, rest) in courses %}
    <dt>{{(cn ~ ': ') if cn else ''}}{{ct}}</dt>
    <dd>
      <ul class='list-inline'>
        {% for (cy, cs, cl) in rest %}
          <li>
            <a href='{{cl}}'>
              {{ 'Spring' if cs == 's' else
                  ( 'Fall' if cs == 'f' else cs ) }}
              {{cy}}
            </a>
          </li>
        {% endfor %}
      </ul>
    </dd>
  {% endfor %}
</dl>{# }}} #}

## {{secs.lecture_notes}}

*   [Undergraduate PDE](http://wiki.math.cmu.edu/iki/2014-372/)
    (See also the [class website]({{old_teaching}}/2013-14/372-pde/) for
    problems and references. I have LaTeX solutions to all problems, which I
    can share with instructors who are interested.)

    These notes are a "free and open source" wiki.
    If you'd like to modify them heavily and use them in your own course, you can
    [clone the repository](http://wiki.math.cmu.edu/gitweb-pub/?p=2014-372-wiki.git;a=summary)
    (or ask me to host a cloned copy for you).

## {{secs.student_projects}}

### {{secs.student_lecture_notes}}

These lecture notes have been <span class='text-primary'>written entirely by students</span> while taking courses taught by me.
My only contribution is teaching the course and setting up the websites to host them.

You are free to edit, modify and redistribute these notes (under the terms stated in the respective licenses).

* Measure Theory:

    * [Lecture notes by Eugene Choi (2013/14)]({{old_teaching}}/2013-14/720-measure/pdfs/eugenes-notes.pdf)

    * [Lecture notes by Adam Gutter (2014/15)]({{old_teaching}}/2014-15/720-measure/pdfs/adams-notes.pdf)

    * [The LaTeX source for both notes](http://wiki.math.cmu.edu/gitweb-pub/?p=201312-measure.git;a=summary)

    * [Class website]({{old_teaching}}/2014-15/720-measure/)

* Stochastic Calculus:

    * [Lecture notes wiki](https://lecturenotes.math.cmu.edu/mediawiki/index.php/Stochastic_Calculus_(Fall_2012))
      by Ryan Murray, Jimmy Murphy and others.

    * [Class website]({{old_teaching}}/2013-14/880-scalc/)

### {{secs.masters_thesis}}

* [James T. Murphy III](http://intfxdx.com/),
  *Resolving the one-dimensional autonomous flow-free explosion problem*
  (Published in [SIURO](http://www.siam.org/students/siuro/vol7/index.php)
  [here](http://www.siam.org/students/siuro/vol7/S01319.pdf).)
