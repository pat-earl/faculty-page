---
title: "Arrays - Chapter 9"
subtitle: "CSC120"
author: Patrick Earl
date: 03/16/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Arrays Overview
* What is an array?
* Declaring an array
* Initializing an array
* Array operations
* Array of objects

---

## Arrays
* Allows for multiple instances of similar data
* Declaring 100 versions of the *Car* object
* Arrays point to a sequence of items in memory
    * Similarly to how a variable points to a single thing in memory

---

* This allows a program to think of an array as a *list*
    * Keep track of the *elements* in the list
    * Keep track of the *order* of elements.
* The position of an element is known as it's *index*. 
    * This is a unique *integer* that designates the position in the array
* Indices start at *zero* 
    * Start at index *zero* since the first element is *0* positions away from the start.

---

## Array Declaration 
* Arrays, like variables, **must** have a name and type.
* `int[] arrayOfInts;`
    * Declaring an array
* Arrays are of *fixed-sized*, meaning once they're initialized you can't add more than the size specified. 
    * An array of size 10, *can't hold 11 elements*.
* `arrayOfInts = new int[42];`
    * Use the *new* keyword to create an array.
    * *Make a new array of 42 integers*
* The size must be a non-negative integer.

--- 

## Array Initialization
* Filling an array with values?
* Manual Assignment:
```
int[] stuff = new int[3];
stuff[0] = 1;
stuff[1] = 2;
stuff[2] = 3;
```
* Initialize all at once:
```
int[] stuff = {1, 5, 7, 9, 11};
```
* *This is not the recommended way*
* Using iteration to work on *each* element

---

## Array Operations
* Consider the following problem:
    * Create an array with *1,000* floating-point numbers and initialize it to a random number between 0 and 10.
* What would this look like in code?

---

* Using a loop to initialize
    * while
    * for
* Array's Length
    * `array.length`

---

## Simple Example
* Drawing a snake that stores the last *N* positions of the mouse.
* Two arrays: X positions and Y positions
* Setup:
    * Init the arrays to 0
* Draw:
    * Each loop of draw, update the array with the current mouse's location
    * Store up to 50 positions which would be indices 0 to 49 
        * *-or-* `array.length - 1`
    * Problems?

---

* Draw:
    * Shift all the elements down on spot before updating the current position. 
    * Draw circles based on the array
* *Example 9-8*

---

## Arrays of Objects

---

## Interactive Objects

---

## Processing Array Functions

---

## 1001 Zoogs
