---
title: "Introduction"
subtitle: "CSC223"
author: Patrick Earl
date: 01/22/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Python Introduction

* *TIP: If viewing this in a web browser, press **ESC** to see a preview of all the slides.*
* Python is an *interpreted* language
* Statements can be interactively ran and tested
* 4 Ways to do this:
    1. The Python Interpreter
    2. IPython Interpreter
    3. Self-Contained Scripts 
    4. Jupyter Notebook

## The Interpreter

* Access by typing `python` in a command prompt. In this form you can type statements and execute code
* This places you in the Python ***REPL***
    1. Read the input
    2. Evaluate it
    3. Print the results
    4. Loop back to step 1
* `>>>`
* `help()` and Python reference

## IPython Interpreter

* A more advanced and feature packed version of the python
interpreter.
* IPython will use numbered commands in place of the `>>>`
* Input and Output are numbered.

## Self-Contained Scripts

* Statements can be saved to a file, much like
other programming languages (C++, Java)
* Python scripts are saved in *.py* files
* To run a script, assuming you are in the same directory as the file:
    - `python [file name].py`

## The Jupyter Notebook

Hybrid of the two environments that will be explored and explained later in the course.

## The Python Syntax

* *Syntax* - The structure of the language (incase you forgot).

## Example program

```
# set the midpoint
midpoint = 5

# make two empty lists
lower = []; upper = []

# split the numbers into lower and upper
for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
        
print("lower:", lower)
print("upper:", upper)
```

## Syntax Rundown

* Comments are marked by "#"
* End-Of-Line Terminates a Statement
* Semicolons can be used optionally used to terminate


## Syntax Rundown (Continued)

* Indenting: Whitespace matters
    - Code blocks are controlled by indents
    - 4 spaces is the preferred amount
* Whitespace *within* a line doesn't matter
* Parentheses are for grouping or calling

## Variables

* Similar to others
* Use the assignment operator
* `x = 4` assigns a value of 4 to the variable *x*

## Note on Variables

* Python is *dynamically-typed*
    - Opposed to a static-typed language like C++
* Variables are *pointers* to space in memory
* You can do this:
    - `x = 1`
    - `x = 'hello'`
    - `x = [1, 2, 3]`

## More Notes

* Python simple types (int, float) are *immutable*
* Lists on the other hand are *mutable*
* Example:
    - `x = 10` *x* points to a memory location containing the value 10
    - `x = 11` *x* points to a new memory location with
    the value 11. 

## Everything is an Object

* `type()` function
* Objects will have a type
    
## What is an Object?

* In terms of programming languages an *object* is:
    - an entity that contains data along with metadata and/or functionality.
* Python Objects will:
    - have metadata (better known as *attributes*)
    - have associated functionality (*methods*)
* dot syntax  
