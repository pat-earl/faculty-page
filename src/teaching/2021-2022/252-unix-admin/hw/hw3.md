title: Homework #3
breadcrumb: ../index.md

**Due:**
: Friday, March 4th

**Purpose:**
: Demonstrate understanding of shell pipes
: Practice usage of filter commands

## Description

Using various command line utilities that have been discussed in class and videos, complete the following below. Please precede the command used in your bash script with an echo specifying what number the command is corresponding too. 

1. The following will use the `students2.dat` file. Directions how to get the file are in the **Setup & Submission** section. The contains records of students with their name, major, GPA, email, and phone number.
    1. Display the contents of the file sorted by first name, ignoring any leading whitespace. Column 1 is the First Name, Column 2 is the Last name.
    2. Display lines, *with line numbers*, of **Computer Science** majors.
    3. Display lines, *with line numbers*, of students whose first or last name is **John**.
    4. Display all **ECE** majors sorted in descending order by GPA.
    5. Display all lines but show only the last name and GPA, sorted by an ascending GPA. 
2. Search through your home directory and display filenames (pathnames) for all C++ program files. Terminate your command with `2>/dev/null` to ignore any errors.
3. Create a hard link:
    1. Write a command to remove a file named `newFile.hard`
    2. Create a hard link named `newFile.hard` pointing to the `students2.dat` file in your directory. 
    3. Answer the following question using a comment placed in your bash script: Do a long listing of the link you created and the original file. Compare the attributes, how would you confirm that they are two names referring to the same file? 
4. Create a soft link:
    1. Write a command to remove a file named `newFile.soft`
    2. Create a soft link named `newFile.soft` pointing to the `students2.dat` file in your directory
    3. Answer the following question using a comment place in your bash script: Do a long listing of the link you created and the original file. Compare the attributes, how would you confirm that they are two different files?
5. Write a command that will display the inode/filename pair for **ALL** files in `~earl/public` sorted by inode number.

Use of the following will result in a zero for the assignment:
    - Environment Variables
    - `awk`
    - `sed`


## Setup & Submission

**Setup:**

Place your bash script in a directory named `hw3_FirstLast` (Replacing first and last with your first and last name).
Inside the directory create a bash script of any name.

Also copy the `students2.dat` file into the directory you just created.
It is located here: `~earl/public/csc252/students2.dat`.

**Submission:**

Inside the directory you created earlier, run the following command:
`~earl/bin/submit csc252 hw3`