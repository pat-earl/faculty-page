title: Homework #2
breadcrumb: ../index.md

## Basic Linux Commands

**Due:**
: Friday, Feb 25, 2022

Create a bash script that will run commands based on the requirements below.
Each bullet **must be** a separate command.

Please include an echo statement on the line before the command. For example:

```bash
echo 1a.
command # You'd replace command with the proper one to complete the assignment
```

1. Information about your current login using the `id` command.
    * username
    * user ID
    * group ID
    * Name of each group your user is part of
2. Display information about the current system.  
    * The current operating system
    * Hostname
    * Kernel name, release, and version
3. Use the `date` to do the following:  
    * The date September 5, 2019 in MM/DD/YYYY format
    * Current weekday name, month day, year (For Example: Sunday, January 10, 2020)
    * The current date and time in RFC 3339 format


### Submission:

**Place your script in a directory named hw2_FirstLast**. For Example: hw2_PatrickEarl.
The name of the script doesn't matter, but put `.bash` as the file extension. `main.bash` would be fine.
Make sure you include the proper sha-bang line at the top of the script (`#!/bin/bash`) and make
your file executable. 

Submit by running `~earl/bin/submit csc252 hw2`. 