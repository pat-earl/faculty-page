title: Homework #2

## File Commands

**Due:**
: Saturday, Feb 27, 2021

Using the file commands discussed & presented in class, write a command that 
fulfills the requirements below.
You can also choose to use several commands with a "pipe." Display an echo above each command. 
For question 1 do an echo (i.e. "echo 1a" or "echo 1-1") for each sub question.

For questions 3 & 4, please put your responses to the last part of those questions as a comment in your script.

1. Copy the *students2.dat* file from my public csc252 directory. Use this file for the following commands. (*NOTE:* You don't have to include the command to copy this file in your script, but make sure it is in your directory when submitting):
     * Display the contents of the file sorted by last name. Ignore any leading whitespace. Column 1 is the first name and column 2 is last name.
     * Display lines, *with line numbers*, of records of Computer Science majors.
     * Display lines, *with line numbers*, for students whose first or last name is John.
     * Display all ECE majors sorted in descending order by GPA. 
     * Display all lines but show only the last name and GPA, sorted by an ascending GPA.
2. Search your home directory and display pathnames of all C++ program files. Terminate your command with `2>/dev/null` to ignore any error messages.
2. Remove the file *newFile.hard* if it exists. Create a hard link to students2.dat named *newFile.hard*. Display a long listing of that new link file and compare it's attributes with that of student2.dat. How would you confirm that students2.dat and *newFile.hard* are two names of the same file. 
3. Remove the file *newFile.soft* if it exists. Create a soft link to students2.dat and name the link file *newFile.soft*. Display a long listing of the new link file and compare it's attributes with that of students2.dat. How would you confirm that student2.dat and *newFile.soft* are different files? 
4. Display the inode/filename pairs for *ALL* the files in ~earl/public/csc135, sorted by inode number.

*You should only use the utility commands we've talked about so far in the semester. awk & sed are advanced commands and using them will result in a major grade penalty. 

## Submission

These commands should be placed within a bash script. Remember to use the sha-bang line and make your bash script executable. 

The directory for this assignment should be named *hw2_FirstLast* (i.e. hw2_PatrickEarl)

Use *~earl/bin/submit.bash* to submit your assignment.

## Grading 

TBD
