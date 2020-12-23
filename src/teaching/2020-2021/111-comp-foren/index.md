infotable: 0
stylesheet: local.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Course Description

This course is an introduction to the basic concepts of computer forensics.  It will teach the student how to identify, preserve, recover, analyze and document data on a computer or network allegedly used to commit a crime.  Topics include computer architecture, operating systems, encryption/decryption, preserve and document evidence, and analyzing computers and networks for evidence.  

## Resources

* [First Day Handout](./111-fdh.pdf)
* More will come as needed

## Lecture PowerPoints

## Homework Handouts