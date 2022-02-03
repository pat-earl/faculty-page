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

- **Working Directory** - When in command-line environments, you will always be in an associated directory. Referred to ask your working directory. 
- **Home Directory** - Your working directory when first logging into a command-line environment.
  - Typically used to hold `start-up` files.

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

# File Permissions

*TODO*

---

# `chmod`

*TODO*

---

