title: VM Assignment

**Due:**
: Friday, April 23.

**Purpose:**
: Perform basic system administration tasks on a virtual machine

## Description

You and your team are to work together and complete the following tasks outlined below. Each
task is split into smaller parts, so be sure to read each step carefully. 

*If you are currently not assigned to a group, reach out to me ASAP.*

Team assignments can be under the "VM Groups" section of the D2L Course Content. 

The main tasks are as followed:

1. Add a new user
2. Partition and format a newly added hard drive on your VM.
3. Install an application using the system's package manager.

Your virtual machines are running *Ubuntu 20.04 LTS* which is a debian-based Linux distribution. 
The login name for the machines is *csc252*. The password for the VM is included in the team handouts. 

You should change the account's password to something only your team knows. 

**For Off-Campus access:**

* You can first ssh into ACAD and then into your team's VM. -or-
* Login into the VPN client and directly ssh into the machine. 

Be sure to document which *successful* commands you used. Each section explains what supporting 
documentation you should include to prove you completed the task. 
Be sure to read the submission section below as well.

### Task 1 - New Account
You will need to create a new user account following these requirements. You can use whatever
login name you see fit, but keep it appropriate. 

* The user's primary group should be the same as their login name.
* The UID should be 2000
* The user should have a home directory in `/home/<login>`. (Replace login with the name you choose).
* Set a password for the user's account. Make sure you document the user's password in your submission materials.
* The user's password should be set to expire at next login. 

After the user has been created, make sure a group of the same name is created. This group ID should
be 4000. Make sure the user is part of the group.

Run a command (or commands) to document that this new user and group has been created. 
Include the commands and screenshots of their output in your submission materials.

### Task 2 - New Hard Drive
A spare virtual hard drive (About 256MB in size) is attached to your machines. You'll need to partition,
format and mount the drive using the requirements outlined below. You should follow these steps in order.

1. Partitioning
    1. Clear any previous partition tables off the disk
    2. Create a new partition that uses the entire size of the disk. 
    3. Write the changes to the disk
2. Formatting
    1. Format the newly created partition using the ext3 file system. 
3. Mounting
    1. The drive will be mounted at `/media/disk` on the file system. (*NOTE:* You may need to create these directories)
    2. You will need to add this disk to the `/etc/fstab` file so that it is mounted at boot. 

Run and screenshot the output of commands you feel document your completion of this task. Please sure
to include the screenshots in your submission. 


### Task 3 - Software Package Manager
This machine will be used by software engineers testing feature updates to an application written in 
C++. By default, the required software to build the application is not included with Ubuntu. Use the system's
package manager to install the new software listed below:

* gcc (Latest Version) - The GNU C/C++ Compiler
* make (Latest Version) - Allows for automation of the C++ compiler. 

Run the commands without any arguments and screenshot their outputs. 
Include this documentation in your submission. 


## Submission
Your submission should be in a `.docx` or `.pdf` format file, other file types will not be accepted.

At the top of your document be sure to include your team member names, the course, assignment, and instructor name.

Split the document into sections based on the tasks. The first part of the section should include a brief description 
of what commands you needed to complete the tasks and why. The second part should be the requested documentation
from the end of each part. 

Upload your completed document to the correct dropbox on D2L. Only one member of your team needs to do so. 