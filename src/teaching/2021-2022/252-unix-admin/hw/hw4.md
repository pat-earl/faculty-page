title: Homework #4

## File Commands

**Due:**
: Friday, April 1, 2022

**Purpose:**
: Writing bash scripts
: Use of bash control structures

## Description

Write a bash script to find and print a long listing for all files that are over a specified size
**AND** files that were modified more than a specified number of days ago. Each section of files
should be preceded by a heading indicating what follows (i.e. *These are the files of X size*). 
This should be the usage message for this script:

`name_of_script.bash [starting directory] [minimum filesize in KB] [age for files in days]`

Note that *all* command-line arguments are optional. If no arguments are included, the following
should be the defaults used in the script:

* Directory - Current Directory
* Minimum Filesize - 10KB
* Age for Files - 180 Days

Other requirements for your script:

* Must have a usage cause.
    * Show this when the user uses too many arguments or *(for EC)* types *-h* with no other CLAs.
* Must be able to accept 0-3 command line arguments.
    * 0 - Use Defaults
    * 1 - Set the directory
    * 2 - Set the directory & Minimum Filesize
    * 3 - Set the directory, min. filesize, & age for files
* Must use a case statement for assignment CLAs/default values to variables
* Must use the `find` command without the *-exec* or *-ls* options
* Must use a for loop to process files returned by find

## Submission
Your script **must** be in a directory called *hw4_FirstLast*,
replacing First & Last with your first and last name. 

Submissions with any other directory name *will be ignored*. Similarly make sure to make your bash
script executable by *all*. 

Name your bash script appropriately. Scripts that don't follow the requirements above will result in zero for the assignment.

Submit using: `~earl/bin/submit csc252 hw4`.

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
* (**EC** 5 Points *all or nothing*) - Handles *-h* option argument