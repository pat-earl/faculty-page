---
title: "Chapter 4 - Variables"
subtitle: "CSC120"
author: Patrick Earl
date: 01/26/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Variables

* A metaphorical bucket
* Computers have memory, allowing you to story information for later use
* *Variables* are pointers to a location in computer's memory
* Return of Graph Paper
* Variable values can be altered or *vary*
* [What information do you need for a game of pong?](https://en.wikipedia.org/wiki/Pong)

## Variables

* Variables hold *primitive* values or *references* to *objects* and *arrays*.
* *Primitive* variables usually refer to holding a singular pice of information, like:
  * Whole numbers (1, 2, 3, 4)
    * Referred to as an *integer*, with ***int*** as the keyword.
  * Decimal Numbers (3.45, 2.5)
    * *Floating-Point Values*, with ***float*** as the keyword.
  * Characters (Single letters like "a", "b", "c")
    * Stored with *char* and using single quotes (`'`)
  
## Primitive Types

* *boolean*: true or false
* *char*: a character
* *byte*: a small number, -128 to 127
* *short*: larger number, -32,768 to 32,767
* *int*: a big number, -2,147,483,648 to 2,147,483,647
* *long*: huge numbers
* *float*: a decimal number
* *double*: decimal numbers with more decimal places

## Variable Assignment

* Once a variable is created, it can be assigned a value.
  * Known as *initializing*
* `int count;`  
* `count = 50;` 
* One-Line:
  * `int count = 50;`

## Creating Variables

* Variables need a *type* and a *name*.
* Rules for naming:
  - One Word (no spaces)
  - Must start with a letter
  - Can include numbers, just not at the start
  - No punctuation, except the underscore `_`


## Naming Variables

* Avoid using words that appear else where in Processing (like *setup* or *mouseX*)
* Use names that describe what the variables is storing.
  * If you're going to keep track of a player's score, name the variable `score`, not `cat`.
* Start variables with a lowercase letter and join words with capitals. janesScore. 
  * This willBecome second nature withSome experience. 
  * This known as *camelCase* if you're curious

## Using Variables

* *mouseX* and *mouseY* are variables!
  * Built-in into Processing
* **Example 4-2**

## Questions

* Things to think about before writing a sketch
  * *What data I need to remember for the sketch?*
  * *How do I use that data to draw shapes on the screen?*
  * *How do I alter that data to make my sketch interactive and animated?*

## Many Variables

* Using variables for every possible thing?
* **Example 4-4**
* *mouseX* / *mouseY*
  - What are they?

## System Variables

* Commonly used *built-in* variables
* **width**
* **height**
* **frameCount** 
* **framerate**
* **displayWidth**
* **displayHeight**

## System Variables (more)

* **key**
* **keyCode**
* **keyPressed**
* **mousePressed**
* **mouseButton**
* *Avoid overwriting these variables.*
  * You can replace them and will no longer work as expected.
* **Example 4-5**

## Random

* *Incremental Development*
* `random();`
* **Example 4-6**
* Random returns float, fill expects integers?
  * ***casting***
* **Example 4-7**

## Variable Zoog

* **Example 4-8**

## Translation

* **Example 3-7**
* So far, all shapes have been drawn relative to the origin point
  - *(0, 0)* - Top Left of the Display
* `translate();`
  - You can change the offset of drawing *or*
  - The relative point*
* *Chapter 14*, more on that next week