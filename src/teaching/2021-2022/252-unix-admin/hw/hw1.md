title: Homework #1
breadcrumb: ../index.md

**Due:** 
: Friday, February 2

**Purpose:**
: Demonstrate the ability to create a basic shell script
: Learn about placing commands inside a shell script

## Description

This assignment is to get you familiar with creating *BASH* shell scripts and using
the assignment submitter. 

*NOTE*: If you haven't done so already, it's recommended that you create a `csc252` directory in your home
directory on CSITRD and store this assignment and all future assignments there. 

### Assignment Setup:

1. Create a new directory called `hw1_bash` (in the csc252 directory if you created it) and change into
it. The submit script you'll be using creates an archive of your current working directory, so
make sure you're in the right one!
2. Within this directory you should create a new shell script called `hw1.sh`. You can use
whatever command line text editor you're most familiar with (nano, vim, emacs, etc.). 
3. Make sure you add the SHA-BANG (`#!`) on the *first* line of the shell script. 
    1. This tells Linux which interpreter to use when executing the script. 
    2. Since it's a *BASH* script, you should put `#!/bin/bash`.
4. **After** the SHA-BANG line, make sure you put your documentation header and include all
the information as required by the [CS&IT Department's Documentation Standards](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/DocumentationStandard.pdf)
5. Now you are ready to start creating the script.

### Requirements:

Your shell script should achieve the following requirements in-order:

***NOTE***: For each step, please display the step number you are achieving. Refer to this example:

```bash
# DOCUMENTATION HEADER END

echo 1.
# Command to fullfil requirement 1 goes here

echo 2.
# Command for requirement 2

echo N.
# etc.
```

1. Write a command that will output a quote/lyric from one of your favorite movies, shows, artists, etc.
2. Write a command that will output your current login name. 
3. Write a command that will print the current working directory

That's it

## Submission:

In order to submit this assignment, you'll run the following command inside the assignment directory
you created earlier:

`~earl/bin/submit <course> <assignment_name>` 

*You don't need the arrows `<` `>`, they are used to show where you'll be put your information*

Replace `<course>` with the class's course code, `csc252`, and `<assignment_name>` with `hw1`. 
Confirm that you want to submit the assignment by typing `y` or `Y` and hitting enter. Upon successful submission 
you should receive an email receipt. If you run into any errors, please e-mail the instructor and 
be sure to include *ALL* the output from the `submit` command.

*CSC252 - Spring 2022*