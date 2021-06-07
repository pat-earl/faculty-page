title: Homework #3

## File Commands

**Due:**
: Monday, June 14 by 11:59PM

**Purpose:**
: Writing BASH scripts
: Use of BASH control structures

## Description

Write a bash script to find and print a long listing for all files that are over a specified size
**AND** files that were modified more than a specified number of days ago. Each section of files
should be preceded by a heading indicating what follows (i.e. *These are the files over X size*). 

If the user passes too many arguments (more than 3), your script should output this usage message:

`name_of_script.bash [starting directory] [minimum file size in KB] [age for files in days]`

Note that *all* command-line arguments are optional. If no arguments are included, use the following
as default values:

* Directory - User's Home Directory
* Minimum File Size - 2KB
* Age for Files - 30 Days

Other requirements for your script:

* Must have a usage cause
* Must be able to accept zero (0) arguments up to all three (3).
* Must use a case statement for assignment CLAs/default values to variables
* Must use the *find* command without the *-exec* or *-ls* options
* Must use a for loop to process files returned by find

## Submission
Turn the file in using `submit.bash`. Your script **must** be in a directory called *hw3_FirstLast*,
replacing First & Last with your first and last name. 

Submissions with any other directory name *will be ignored*. Similarly make sure to make your bash
script executable by *all*. 

Name your bash script appropriately. Scripts that don't follow the requirements will receive a grade of zero.

## Grading

Grade out of 50 Points

* 5 Points - Appropriate File Name
* 5 Points - Correct Sha-Bang Line
* 30 Points - Functionality
    * 5 Points - Correct defaults/Usage statement
    * 5 Points - Accepts 0-3 arguments
    * 5 Points - Uses a `case` statement to handle positional arguments
    * 15 Points - Correct implementation of `find` and outputting the found files.
* 10 Points - Thoughtful comments in script.