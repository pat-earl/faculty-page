{%- from get_file('course_info.j2') import course -%}
title: Lecture Schedule
breadcrumb: index.html|{{course.title}}

Here is a lecture by lecture list of topics covered in class, with references for further reading.

## Introduction{# <small>(Lectures 1 -- 7, 8/31 -- 9/16)</small> #}
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

## A Glimpse at Numerical Methods{# <small>(Lectures 8--9, 9/18--9/21)</small> #}

*Reference: Hall and Porsching, Chapters 1, 4.*

* Approximating derivatives
* The explicit Euler scheme for the heat equation
    * Stability analysis

## Separation of Variables and Fourier Series{# <small>(Lectures 10--17, 9/23--10/9)</small>#}

*References.
    Strauss: Chapters 4, 5.
    Pinchover and Rubinstein: Chapter 5.
    372-wiki:
        [Separation of Variables](http://wiki.math.cmu.edu/iki/2014-372/sepvar.html),
        [Fourier Series](http://wiki.math.cmu.edu/iki/2014-372/fourier-series.html)* 

* Series form solutions for the heat and wave equations.
* Eigenfunctions of the Laplacian
* Computing Fourier Coefficients
* Bessel's and Parseval's inequality
* Basic convergence results

## Harmonic Functions{# <small>(Lectures 18--23, 10/12--10/23)</small>#}

*References.
    Strauss: Chapter 6.
    [372-wiki](http://wiki.math.cmu.edu/iki/2014-372/harmonic.html)*

* Separation of variables in a disk.
    - Poisson Kernel
    - Poisson Formula in two dimensions
    - Mean value property, Strong Maximum Principle
    - Smoothness of solutions
    - Approximate identities, and convergence at the boundary
* Separation of variables in a square, annulus and a wedge.
* Eigenfunctions of the Laplacian
* Maximum principle with convection terms.

## Greens Functions{# <small>(Lectures 24--29, 10/26--11/9)</small>#}

*References.
    Strauss: Chapter 7,
    [372-wiki](http://wiki.math.cmu.edu/iki/2014-372/greens-functions.html).*

* Newton Potentials.
    - The Poisson equation in $\R^d$.
    - A representation formula for Harmonic functions.
    - Mean value property.
* Greens functions.
    - Existence and Uniqueness
    - Symmetry
    - Computation in half space and spheres.

## The Heat Equation{# <small>(Lectures 30--?, 11/11--?)</small>#}

*References.
    Strauss: Chapters 2,3.
    [372-wiki](http://wiki.math.cmu.edu/iki/2014-372/heat-1d.html)*

* The heat kernel on $\R^d$.
* Duhamel's principle
* Parabolic maximum principle.
* Strong maximum principle.

## The Wave Equation 

* D'Alembert's formula
* Duhamel's principle
* Kirchoff's formula
* Huygens principle

## Optional topics

*(These were covered in the last week and a half of class for interest only. No
homework will be assigned on these topics, and they will not appear on the
final.)*

### An introduction to asymptotic expansions

* Periodic divergence form equations
* Computing the effective diffusivity 

### The Fourier Transform

* Elementary Properties
* Inversion
* Applications to linear PDE's
* Uncertainty Principle

### An introduction to Fluid Dynamics

* The Euler and Navier-Stokes equations
* D'Alembert's paradox: why planes shouldn't fly.
