title: Homework #2

<br>

## Store Statistics in Python

**Due**
: Friday Feb 12, 2021

Assignment focuses on writing basic python scripts.

## Description

A department store needs a program to calculate the sales statistics for it's various departments
each year. This store has a standard sales amount (in thousands of dollars) for each month based
on data from previous years. 

The monthly sales amount are stored in a file `sales.dat`. Each line in the file contains twelve 
sales amounts for that department. 

```
Jan	    Feb	    Mar	    Apr	    May	    Jun	    Jul	    Aug	    Sept	Oct	    Nov	    Dec
23.0	33.1	21.0	23.5	54.0	34.3	35.0	45.0	56.3	45.6	34.0	55.0
```
*The standards for each month*

Write a program to calculate statistics for each department in the store. Your program should do the 
following:

1. Prompt the user for the input file.
1. Read the file data into a list of lists - 2D List.
1. Compute the average monthly sales for each department.
1. Compare each monthly sales amount with the standard.
1. Write the statistics for the department, including the department number, average sales amount,
number of months above and below the standard, and performance to a file. The program should output
"unsatisfied" as the performance of the department if more than five months are below standard
and "satisfied" otherwise.  

Your output file must be formatted as follows:

`Department,Average,Above,Below,Performance`

and each subsequent line contains the appropriate values in the correct order separated by commas.
The average value must be output with *one* decimal point of precision. 

Your program must be composed of the following functions with the exact names, formal parameters,
and return values:

* `get_data`: takes a string representing a filename and returns a Python list of lists of floats read
from the file. The outer list has the same length as the number of rows in the files and each inner list
has a length of 12. That is, each inner list represents a single line of the file.
* `process_data`: takes a list of floats and returns a list of dictionaries. Each dictionary must have
the following key names and values where the values correspond to the respective inner list:
    * **"Department"**: (int) the department number (the inner list number where the first inner list is 1)
    * **"Average"**: (float) the average of the list
    * **"Above"**: (int) the number of entries greater than or equal to the standard. 
    * **"Below"**: (int) the number of entries less than the standard
    * **"Performance"**: (string) The department's performance based number of months above or below the standard. Only two values should be "unsatisfied" or "satisfied".
    * The standard values must be local to this function.
* `write_to_file`: takes a list of dictionaries of the form returned from `process_data` function and writes 
the values to a file. The file format is described above. This function must use at least one Python format string as part of the
implementation. The output file must be `out.dat`
* `main`: prompts the user for a filename and calls the other functions with the appropriate arguments. 

Note that you may create your own helper functions if you wish. *The last line in the script should
call the `main` function.*

The use of any of the following Python features will result in a grade of zero for this assignment:

* `import` statements
* list comprehensions
* generators
* higher-order functions



## Submission

Turn in a file named `main.py`, in the correct D2L assignment folder. 

## Grading Criteria

