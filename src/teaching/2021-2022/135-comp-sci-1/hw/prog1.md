title: Program 1

**Due:**
: Friday 09/17

**Purpose:**
: Analyze a program's requirements.
: Demonstrate understanding of basic C++ program syntax.
: Demonstrate the ability to compile and run a C++ program. 

## Description

**Program \#1 -- Introduction (Monthly Sales Tax)**

A retail company must file a monthly sales tax report listing the sales
for the month and the amount of sales tax collected. Write a program
that asks for the month, the year, and the total amount collected at the
cash register (that is, product sales plus sales tax). The sales tax is
split between the state and the county. Assume state sales tax is 4
percent and the county sales tax is 2 percent.

If the total amount collected is known and the total sales tax is 6
percent, the amount of product sales is calculated using the formula:

$S = T / 1.06$

where S is the product sales and T is the total income (product sales plus sales tax)

The program should display a report similar to the one below.

```
Month: October
Year: 2008
---------------
Total Collected: $ 26572.89
Product Sales: $ 25068.76
County Sales Tax: $ 501.38
State Sales Tax: $ 1002.75
Total Sales Tax: $ 1504.13
```

## Setup & Submission

To start the assignment, copy the skelton directory:

`cp -r ~earl/public/csc135/projects/project1 ~/csc135`

This will place the files in a directory I own into your csc135 directory.
Make a file called project1.cpp and place your source code there. Complete the project plan 
in the file named `project_plan.txt`. You may also complete it in a Word Document, which 
you should submit on D2L in 'Program 1 - Project Plan Submission'.

To submit type, `make submit` and follow the prompts. You should receive an email receipt. 