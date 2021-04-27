---
title: "Python"
subtitle: "CSC252"
author: Patrick Earl
date: 04/22/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: fade
---

## Other Scripting Languages

* Most \*NIX distros ship with some default "scripting" languages. 
* *Perl* was one of the original scripting languages to come about outside of the shell.
    * Main design principle was for working with text files to find and extract information from them to generate some report. 
    * Follows many syntax features from *awk*, *sed*, *C*, *BASH*, etc.

---

* *Python* has also become popular for use in automating Sys. Admin tasks. 
    * Has a massive standard library, with many providing hook-ins to \*NIX.
    * Two major versions 2 and 3. 

---

## Running Python
* Python can be ran interactively or using a source code file. 
    * `python` without any arguments
    * `python <file>` to run a script file
    * `#!/usr/bin/env python` for script file with sha-bang line

---

## Python Basics

* Variables
    * Python is a dynamic language, you do not need to define a data type, as they will be inferred based on the value. 
    * `num = 20` - int
    * `floating = 6.7` - floating-point number
    * `word = "Hello World!"` - A string (can use single or double quotes to enclose the string)
* Depending on the type, various functions will be available 
* Comments
    * Comments are denoted using the pound sign *#*. 
    * Any text the follows it will be ignored by the interpreter.

---

## Python Basics

* Input/Output
    * Python in it's basic form provides input/output capabilities. 
    * `print` - Will allow you to print expressions, values, variables to standard output
    * `input` - Allows for reading from standard input with an optional prompt line. 

```
print("Hello World!")
print("Hello", "World", "!")
print(2+2)

msg = input()
print(msg)

msg2 = input("Please enter some text: ")
print(msg2)
```

---

## Arithmetic

| Operator | Meaning | 
| -- | -- | 
| + | Addition | 
| - | Subtraction |
| \* | Muplication | 
| / | Division | 
| // | Floor Division | 
| % | Modulus (Remainder) | 
| \*\* | Exponential | 

---

## Boolean Values/Expressions
* Python offers a boolean type just like most languages. A boolean variable can be *True* or *False*
    * Note the capitalization of the T and F. It does matter. 
* Boolean variables are created from assigning a T/F value or through a boolean expression such as `3 > 5` which would evaluate to *False*.
* The relational operators are similar to those found in C++

---

## Comparison Operators

| Operator | Meaning | 
| -- | -- | 
| < | Less Than | 
| > | Greater Than | 
| <= | Less than or equal to | 
| >= | Greater than or equal to | 
| == | Equal to |
| != | Not equal to |

---

## Logical Operators
| Operator | Meaning | 
| -- | -- |
| *and* | Returns *True* if both statements are true |
| *or* | Returns *True* if ONE of the statements is true |
| *not* | Inverts the result. False if True, True if False |

---


## Python Control Structures
* Python provides controls structures similar to most programming languages
    * If..else
    * for
    * while

--- 

## *if* statements
* *if* statements allow for controlling the flow of a program. The general syntax is:
* Syntax: `if boolean-expression:`
* Note that the *if* statement ends with a colon. Python does not rely on brackets to define blocks of code, but instead uses consistent whitespace. 

```
num = input("Please enter a number: ")

if int(num) > 3:
    # If the input is greater than 3, output the message below
    print("You entered a number greater than 3!")
```

--- 

## *while* statements
* Repeat one or more statements as long as the condition is true.
* Syntax: `while conditional:`

```
i = 0
while i < 10:
    print(i)
    i++
```

--- 

## *for* statements
* Repeat one ore more statements 
* Syntax: `for var in seq`

```
for i in range(10):
    print(i)
```

---

## Functions
* Functions accept parameters and can return one more values. 
* User-Defined functions can be created using the syntax: `def funcName(parameter, list)`

```
def add(x, y):
    return x + y

print(add(2, 2))
```

---

## Sequences
* Python provides many types of data structures to hold sequences of data, but we'll focus on three here.
* Lists/Tuples
* Strings
* Dictionaries

---

## Lists
* Lists are the basic implementation of arrays in Python. They are mutable and use zero-based index
* Lists are created by using square brackets and separating elements 
* Tuples are similar to lists, but are considered immutable. Once set, values can't be changed, removed, or added.

```
l = [1, 2, 3, 4]
print(l[0]) # Prints out 1 to stdout
l.append(l[0] + l[2]) # Appends a value of 4 by adding 1 + 3 (index 0 & 2)
```

## Strings
* Strings are sequences of characters and Python's standard library provides many features to interact with them.
* Most functions are not going to effect the string themselves, but will return a new copy. 

| Operation | Meaning | 
| -- | -- |
| len(string) | Will return the number of characters in a string |
| string.upper() | Returns the upper case version of a given string | 
| `string + "Hello"` | Concatenates the two strings together and returns a new one |
| `string[0]` | Will return the first character of a given string |

--- 

## Dictionaries
* Data Structure that provides a Key/Value pair mapping.
* Created by using curly braces

```
d = {
    'key': 'value',
    1: 'one',
    'person': 'Johnny'
}

d["person"] # Would give the value Johnny
```

## Libraries
* Python comes with many additional modules/packages
* os
* sys
* subprocess

## *os* library
* Provides many utilities for operating with the host's operating system and file tree. 
    * The `os.path` sub-module has the file tree methods

```
import os

if not os.path.isdir('./logs'):
    os.mkdir('./logs')

if os.path.isfile("config.txt"):
    f = open("config.txt")
```

---

## *sys* module
* Used for interacting with the Python Interpreter.
* Two properties to note: 
    * `sys.argv` - List of command line arguments passed to a script.
    * `sys.exit` - Cause the Python Interpreter to exit on the spot.

---

## Subprocess
* Will start here on Thursday