title: Homework #4

## Pandas DataFrames

**Due:**
: Friday, March 26

Purpose of this assignment to work with selecting data from a Pandas DataFrame.

## Description
Make a Jupyter notebook named `main.ipynb` that reads in the file toycars.csv
into a Pandas DataFrame. More information about the file can be found here: 

<https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/toycars.html>

[Click here to download the file](https://vincentarelbundock.github.io/Rdatasets/csv/DAAG/toycars.csv)

Create a new DataFrame that satisfies the following criteria:

* Distance measurements must be in centimeters.
* The angle values are the index.
* The DataFrame row are sorted in ascending order based on the index.
* There is a column for each car
* There is a column that is the mean of the distance measurements.
* There is a column that is the standard deviation of the distance measurements.

The standard header information must be in a markdown cell. The code must 
be in a code cell. You must only use **basic** Pandas array operations to
implement your solution. The use of the following functions will result
in a grade of zero for the assignment: `groupby, pivot, pivot_table`.

## Submission
You must turn in a file named `main.ipynb`. Submit the program source file to the appropriate folder on D2L. 

## Grading Criteria

Out of 100 Points:

* 20 Points - Correct Jupyter notebook Criteria
* 20 Points - Correct Index
* 20 Points - Correct Distance Conversion
* 20 Points - Correct Car Columns
* 10 Points - Correct Mean Column
* 10 Points - Correct Standard Deviation Column