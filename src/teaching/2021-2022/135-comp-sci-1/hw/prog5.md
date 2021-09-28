title: Program 5
breadcrumb: ../index.md

**Due:**
: TBD

**Purpose:**
: Demonstrate understanding of passing by value and reference. 
: Effectively read contents of a file using C++.
: Make changes to an existing code based on new requirements. 

## Description

Program \#5 -- Ref Params & Files (Restaurant Bill)

You are to rewrite program \#4 (Restaurant bill program). To begin, you
can copy program \#4 to program \#5. To do this, assuming you named
program \#4 *restaurant.cpp*, you would do the following:

*cp restaurant.cpp restaurant2.cpp*

Now edit restaurant2.cpp for program \#5.

You will rewrite this program to use reference parameters and files. Do
the following:

* You must add a function to your program that will ask the user for
    the name of the data file. The function will then attempt to open
    the file. If the open fails, the program should report this fact and
    quit.
* Read in the number of people at each table from the file using a
    function (if you haven't already done this).
* Change the function that reads and sums the costs so that the costs
    are now read from the file.
* Change the calculation functions so that there is now only one
    function that will do all three calculations (tax, tip and total).
* There is no longer a sentinel of 0 people. The program should now
    process data until it reaches the end of the file.

Each table is associated with two lines in the data file. The first line
contains the number of people at the table. The second line contains all
the costs for that table. You do not know how many tables are there.
There is no sentinel.

Additionally, you must include the following requirements for this
project:

1.  Analysis and Design
    - Problem statement
    - Program inputs and outputs
    - Formulas
    - Program design -- either in pseudocode format
    - Test cases -- include at least three test cases, with at least one consisting of invalid values/results.
2. Code documentation
    - Variable declarations
    - Arrays
    - Complex formulas
    - User-defined functions
    - System functions
    - Parameters
    - Each logical block of code explaining decisions and code functionality