---
title: "Chapters 2 & 3"
subtitle: "CSC120"
author: Patrick Earl
date: 01/21/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Quick Review

* Computer Coordinate System
* Pixels
* Color - Grayscale
* Color - RGB

## Processing

* What is it?
* Where can you get it?
* A Programming IDE

## Useful Keyboard Shortcuts

* CTRL = CONTROL
* CTRL+C - *COPY*, CTRL+V - *PASTE*
* CTRL+Z - *UNDO*
* CTRL+S - *SAVE*
* CTRL+R - *RUN* the sketch
* CTRL+X - *DELETE*
* MAC: Use the *COMMAND ⌘* key instead

## Java

* Two major categories for computers:
    * *Hardware* - The Physical, Tangible pieces that support the computing effort
    * *Software* - A set of instructions that hardware executes one after another
* *Software* is typically written as a program and interacts with computer hardware to accept
inputs, display outputs, and process data.

## Java

* A *programming language* specifies the words and symbols that we can use to write a program
* These languages employ a set of rules that dictate how words and symbols can be put together
to form a *program statement*
* Processing is a fancy layer deployed over topic of Java

## Processing Sketches

* Processing programs are called *sketches* informally.
* One or more *sketch* can be stored in a *sketchbook*.
* Creating your first sketch.

## Coding in Processing

* Programs are made up of *program statements* or *statement* for short.
* There are three basic kinds:
    1. **Function Calls**
    2. Assignment Operations
    3. Control Structures

## Function Calls

* Functions calls have a name, followed by a set of arguments enclosed in parentheses.
* Think of functions as natural language sentences.
    - The function name is *verb* ("draw").
    - The arguments are the options ("point 0,0")
* Functions must always end with a semicolon.

## Function Calls

* Processing will execute a sequence of function calls one by one and finish 
by displaying the drawn result in a window. 
* Use `size();` to control the dimensions of the window you want to create.
    - Takes two arguments (width, height)
* `fullScreen();` will make the display take up your entire screen.

## setup function?



## Other things to know

* Why are some words highlighted?
* Displaying useful information (`println();`)
* Line Numbers
* Comments (Single-Line & Multi-Line)
    - CS&IT Documentation Standard

## Errors

* Most of the time, you'll run into problems when writing your code
    - **This is fine and part of the process!**
* Error Example

## The Processing Reference

* How do I know `rect();` takes four arguments?
* [Processing Reference](https://processing.org/reference/)
    * Name
    * Examples
    * Description
    * Syntax
    * Parameters
    * Returns
    * Related

## The Run Button

* Press the *RUN* button to start your code.
    - Processing does the hard work for you in the background.
* The steps processing takes:
    1. Translate to Java
    1. Compile into Java Byte Code
    1. Execution

## Return of Zoog

* Let's step through the Zoog Example (2-1).

## Going with the flow.

* Graphical Programs are usually interactive, over some *period of time*.
* Moving beyond static designs
    1. Set starting conditions for the program one time. ***SETUP***
    2. Do something over and over and over, until the program quits. ***DRAW***

## setup() and draw()

* Blocks of code

## setup() and draw()

* `void setup()`
* `void draw()`
* What does void mean? What are the empty parenthesis for?
    - That'll come.

## setup() and draw()

## Rewrite Zoog in this format

* Example 3-1

## Mouse Variations

* *mouseX* and *mouseY*
* Example 3-2

* What if we move background to *setup*?

## Mouse Variations

* *pmouseX* and *pmouseY*
* *Previous* mouse locations
* Example 3-4
