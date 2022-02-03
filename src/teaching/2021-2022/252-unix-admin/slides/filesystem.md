---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **The Filesystem**

CSC252 - UNIX Scripting & Administration

Prof. Patrick Earl

Spring 2022

---

# A Hierarchical System

![](./images/unix_tree.png)

---

# Filesystem Hierarchy Standard

- A standard structure for what directories should be created and their purpose. 
- Used as a guide so that OS & software creators can have a general idea on where items are located.
- [Maintained by the Linux Foundation](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

---

# Directory and Ordinary Files

- **Ordinary File** - Appears at the end of a filepath where there are no more branches
  - Simply a file. 
  - Different types of files
- **Directory File** - Appears at the end of a filepath, but can be branched into. 

---

# Special Directories

- **Working Directory** - When in command-line environments, you will always be in an associated directory. 
- **Home Directory** - Your working directory when first logging into a command-line environment.
  - Typically used to hold `start-up` files.

---

# Pathnames

- a.k.a file paths
- **Absolute** 
- **Relative** 

---

# Filesystem Commands

- `ls`
- `cd`
- `mkdir` / `rmdir` / `rm -r`
- `mv`
- `cp`

---

# Special File Types

- `info ls`

---

# Long Listing Format

- `ls -l` Long Format
- Displays the following information:
  - File Type
  - File Mode Bits
  - Number of Hard Links
  - Owner Name
  - Group Name
  - Size
  - Timestamp (Modification)
  - File Name

---

# File Permissions

- Every user *can* have the following three permissions on a given file:
  - Read - The user can view the contents of the file
  - Write - User can write to the file
  - Execute - User can execute the file (This can mean different things depending on file type)

- These 3 permissions are put into three groups:
  - Owner
  - Group
  - Other

---

# `chmod`

- Command used to change the permission bits for files
- Symbolic vs Numeric (Octal)
  - `chmod u+rw file1.txt`
  - `chmod 600 file1.txt`
  - 1 - Execute
  - 2 - Write
  - 4 - Read

---

# Special File Permissions

- `setuid` - Process runs with the file's owner
- `setgid` - Process runs with the group owner of file
- `sticky` - Protects files within a directory. File can only be deleted by owner of file, directory, or root. 

---

# Changing File Attributes

- `chown`
- `chgrp`
- `touch`

