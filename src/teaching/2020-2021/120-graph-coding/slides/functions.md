---
title: "Functions"
subtitle: "CSC120"
author: Patrick Earl
date: 02/23/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

# Functions
* Moving from the simple programs to complex 
    * Writing a paragraph to writing an essay
* *Functions* allow a program to be broken down into parts and make modular pieces
    * *Modularity* - Break large code down into smaller, more manageable parts. 
    * *Reusability* - Allow for reuse of code without re-writing it.

# User-Defined Functions
* `line()` is a function and most of the code so far has been *function calls*
    * These are bits of code written by someone else, defined.

# User-Defined Functions
* Defining a function
    * Return Type
    * Function Name
    * Arguments

# User-Defined Functions
```
type function_name(arguments) {
    // block of code
}
```

# Modularity
* Rewrite *Example 5-6* using functions
    * Move the ball
    * Bounce the ball
    * Display the ball
* Modularity helps with reading, writing, and testing programs!

# Arguments
* *Arguments* are values "passed" into a function
* *Parameters* are the variable declaration inside the function definition. 
* Drawing Cars

# Passing Values
* When a value is passed as an argument, a "copy" of the value is created
    * Meaning: Changes to the parameter in a function don't affect it outside the function
    * *They're local to the function*
* `return` type
    * sum three numbers