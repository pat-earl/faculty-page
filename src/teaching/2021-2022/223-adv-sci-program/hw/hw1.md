title: Homework #1
breadcrumb: ../index.md

**Due:**
: Friday, Feb. 11

## Purpose:

* Solve a problem using the *Python* programming language
* Demonstrate the ability to declare variables and use control structures in *Python*

## Description:

You are to write a program that will process employees and their pay. For each employee the program
will read in an employee's name and hourly pay rate. It should also read in the number of hours
worked each day for 5 days and calculate their total number of hours worked. You must read the 
hours using a loop. The program should output the employee's name, gross pay, total withholding
amount and net pay.

Withholding is made up of state tax, federal tax, and FICA. The following tax values will be used:

* **State Tax**: 3.07%
* **FICA**: 8.86%
* **Federal Tax:**
    * If gross pay is *under* $5000.00: 15%
    * Otherwise: 25%

You don't know how many employees there are, so the program should run until `done` is entered for 
an employee's name. All money output should look like money.

## Submission

Your program should be in a file named `hw1_payroll.py`. Submit it to the correct assignment dropbox
on D2L by the due date.

*Remember to document your program according to the CS&IT Documentation Standards!*

## Grading

Assignment is worth 100 points. 

- *Correct File Name* - 5 Points
- *User Input* - 45 Points
    - Program reads in employee name, pay, and hours worked correctly. Stops accepting input when `done` is entered.
- *Program Output* - 50 Points
    - Program outputs the required information as specified and money looks like money. 

