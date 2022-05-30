title: Homework #5

## Text Processing

**Due:**
: July 1st, 2021 by 11:59PM
: **Due on a Friday**

**Purpose:**
: Write small awk and sed programs to process text data

## Description

Place the following in a bash script to complete the requirements.

1. Write a **gawk** program that numbers each line in a file and sends its output
to standard output. The file should be the first argument passed to the BASH script.
2. Write a **gawk** program that displays all cars priced more than $5,000 and outputs it
to standard output. The cars file can be found here: `~earl/public/csc252/text/cars`
3. Write a **sed** command that copies a file to standard output, *removing* all lines that begin with the word today.
4. Write a **sed** command that copies a file to standard output, removing any blank lines (i.e. Lines with **no** characters on them).


Use command line argument 1 (`$1`) as the file name for numbers 1, 2, and 4.

## Submission

Submit using the bash script `~earl/bin/submit csc252 hw5`.

Make sure you bash script is in a directory named hw5_FirstLast.