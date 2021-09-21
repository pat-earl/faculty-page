title: Program 2

**Due:**
: Friday, 10/01

**Purpose:**
: Analyze a program's requirements.
: Effectively use C++ control structures like if and switch statements.

## Description

**Program \#2 -- Selection (Internet Service Provider)**

An internet service provider has three different subscription packages
for its customer:

* **Package A:** For \$30.95 per month 15 GB of data is provided.
    * Additional gigabytes are \$2.00 each.
* **Package B:** For \$40.95 per month 25 GB of data is provided.
    * Additional gigabytes are \$1.00 each.
* **Package C:** For \$69.99 per month unlimited access is provided.

Write a program that calculates a customer's monthly bill. The program
should ask for the package the customer has purchased. It should accept
one character, A, B, or C. Any other character should display a message
and halt the program. If the user enter A or B, the program should then
ask for the number of gigabytes used. The program should display a bill for
the customer showing the package, gigabytes and total due.

The program MUST contains at least one if statement and at least one
switch statement.

## Setup and Submission

Copy the skelton directory similarly to how you did in Project 1.

`cp -r ~earl/public/csc135/projects/project2 ~/csc135`

*NOTE: Remember to change the target directory to whatever your directory is named (i.e: CSC135 vs csc135).*

There is a `project2.cpp` file already in the directory, you should put your code for this
assignment in there.

To submit, just type `make submit`.

