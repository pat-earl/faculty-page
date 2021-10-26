title: Program 4
breadcrumb: ../index.md

**Due:**
: Friday, Nov. 5

**Purpose:**
: Effectively use C++ repetition control structures (loops).

## Description

**Program \#4 -- Loops (Restaurant Bill)**

Write a C++ program that calculates amount owed by customers in a restaurant. 
Start by asking for the number of people seated at the table. Then 
the program will ask the user for the price of each meal purchased at the table 
(you may assume that each person orders 1 all inclusive meal). The program will 
output a bill showing the subtotal, the sales tax, the tip, and the final 
total for the bill. Make sure the output is neat, clear, and clearly looks
like money. 

Your program should continue accepting new tables until a value of zero (0) is
entered for a table. 

Sales tax is calculated on the subtotal and is 7%. You should also calculate the 
tip based off the subtotal. The tip is 20% if the number of people at the table
is six (6) or less. The tip 25% if there are more than six people.


Example Input:

```
3
10 20 15

4 
7.99 8.25 10.00 9.99

0
```

Example Output:

```
Table 1:
Subtotal:   $45.00
Tax:        $3.15
Tip:        $9.00
Total:      $57.15

Table 2:
Subtotal:   $36.23
Tax:        $2.54
Tip:        $7.25
Total:      $46.02
```

## Setup and Submission

Copy the setup directory from here, `~earl/public/csc135/projects/project4/`, and
place your code in the project4.cpp

Submit using `make submit`.