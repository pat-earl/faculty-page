title: Homework #1

<br>

## Pre-req Review

**Due:**
: Friday 01/29, 2021

**No grace-days can be used for this assignment**

This assignment is used to demonstrate that you meet the prerequiste programming skills required
for this course. The skills tested, but not limited to, are: 

* Read data from a file.
* Process the read data.
* Print the results.

### Description

A store needs a program to calculate the sales statistics for each department this year. 
The store has standard sales amount (in thousand dollars) for each month based on data in previous years.

```
Jan	    Feb	    Mar	    Apr	    May	    Jun	    Jul	    Aug	    Sept	Oct	    Nov	    Dec
23.0	33.1	21.0	23.5	54.0	34.3	35.0	45.0	56.3	45.6	34.0	55.0
```
The monthly sales amounts for departments are stored in a file “sales.dat.” 
Every line in the file contains 12 sales amounts for that department. 
Write a program to calculate statistics for each department in the store. 
Your program should do the following:

1.	Store the standard sales amount in an array
2.	Read the sales amount for each department into a (second) parallel array
3.	Compute the average monthly sale for each department
4.	Compare each monthly sales amount with the standard and store the result in another (third) array of Boolean. The program will store true in the third array if the amount is larger than or equal to the standard and false otherwise. 
5.	Use the third array to find out how many months are below standard and how many are above. 
6.	Output the statistics for the department, including department number, average sales amount, numbers of months above and below standard, and performance. The program should output “unsatisfactory” as the performance of the department if more than four months are below standard and “satisfactory” otherwise. 
7.	Keep processing each department until the end of the file.

Your program must include a single function for each of the following. You may use more functions
or break these into multiple functions as needed or desired. 

* Given the array of sales amount, return the average sales amount.
* Given the array of sales amount, compare with the standard array and enter comparison results in the third array.
* Given the third array of Boolean, return the number of months in which the sales amounts are above standard.
* Output a final statistics for each department.

**sales.dat**
```
23 33.5 21 23 25 56 54 43 34.2 35.4 34 69.5
24 35.2 24 26 43 56.7 54 32 43 34 34 57.9
24 42 43 35 52 56 67 54 56 45.3 32 32
20 32 45 72 45.4 63.2 45 56 52 65 53 65
34 35 37.5 32 23 45 31 43 52 43 76 65
35 56 63.4 45.2 45.6 56 67.3 45 56.3 67 78 76
34.2 45 62 19 45 39 38 37 82 74 45 58.4
```

### Example output

```
Enter file name: sales.dat

Store  Statistics
Dept    	Average 	Above   		Below   		Performance
---------------------------------------------------------------------------------------------
1       	37.6   		 7       		5       		unsatisfied
2       	38.6    	 8       		4       		satisfied
3       	44.9       	 7       		5       		unsatisfied
4       	51.1    	 8       		4       		satisfied
5       	43.0    	 7       		5       		unsatisfied
6       	57.6    	 11      		1       		satisfied
7       	48.2    	 9       		3       		satisfied
```

## Submission

You must turn in a file named main.X where X is the file extension following the convetion of your
choosen programming language. Meaning that if you chose to use Java for this assignment, your file
would be named `main.java`. Submit the file via D2L. 

## Grading Criteria

Out of 50 Points:

* 5 Points - Correct File Name & Documentation
* 15 Points - Reading the file data and placing in an appropriate data structure. 
* 10 Points - Correct "average" Output
* 5 Points - Correct "above" Output
* 5 Points - Correct "below" Output
* 10 Points - Correct "performance" output
