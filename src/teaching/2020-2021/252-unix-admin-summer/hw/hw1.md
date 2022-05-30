title: Homework #1

## Basic Linux Commands

**Due:**
: Monday June 6th by 11:59PM

**Purpose:**
: Use basic UNIX utilities, create a BASH script. 

## Description

Create a BASH script that will run *one* command that outputs the information as requested below. You **must** use UNIX commands and your command should **only** output the requested information. 
Failure to follow those guidelines will result in lost points.
Chapter 3 of the textbook will give more information about the commands needed to complete this assignment. 

Precede each of your commands with an echo followed by the number. 

For example, before running the command to display your username you'd do:
`echo 1a` -OR - `echo 1.1`
followed by the command to show your username.


1. Information about your current login.  
    * username
    * user ID
    * group ID
    * Name of each group your user is part of
2. Find the file location of the *ls* command. 
3. Do a directory listing of this file path: `~earl/public/`
4. Display the *number of lines* for this file: `~earl/public/students2.dat`
5. Display information about the current system.  
    * Hostname
    * Kernel name, release, and version
6. Use the `date` to do the following:  
    * The date September 5, 2019 in MM/DD/YYYY format
    * Current weekday name, month day, year (For Example: Sunday, January 10, 2020)
    * Current date and time in RFC 3339 format


## Submission

**Place your script in a directory named hw1_FirstLast**. For Example: hw1_PatrickEarl.
The name of the script doesn't matter, but put `.bash` as the file extension. `main.bash` for example would be acceptable. 

Make sure you are in the directory you created and then run this command,

`~/earl/bin/submit csc252 hw1`

to submit your assignment.

## Grading 

The assignment is worth 25 points. 
