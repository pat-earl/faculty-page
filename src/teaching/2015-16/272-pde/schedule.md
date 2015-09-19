{%- from get_file('course_info.j2') import course -%}
title: Lecture Schedule
breadcrumb: index.html|{{course.title}}

Here is a lecture by lecture list of topics covered in class, with references for further reading.

## Introduction <small>(Lectures 1 -- 7, 8/31 -- 9/16)</small>
* [Introduction, and model PDE's.](http://wiki.math.cmu.edu/iki/2014-372/intro.html)
* Derivation of model PDE's from physical principles.
  *(Strauss 1.3, [372-wiki](http://wiki.math.cmu.edu/iki/2014-372/model-pdes.html).)*
    * Transport equation
    * Heat equation
    * Wave equation
    * Laplace and Poisson equation
* Boundary conditions *(Strauss 1.4, [372-wiki](http://wiki.math.cmu.edu/iki/2014-372/boundary-conditions.html).)*
* Uniqueness via Energy methods
    * Energy decay for the heat equation *([372-wiki](http://wiki.math.cmu.edu/iki/2014-372/heat-1d/010-energy.html))*
    * Conservation of energy for the wave equation *(Strauss 2.2)*

## A glimpse at Numerical Methods
* Approximating derivatives
* The explicit Euler scheme for the heat equation
    * Stability analysis
