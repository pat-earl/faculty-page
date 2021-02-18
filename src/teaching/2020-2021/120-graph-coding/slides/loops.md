---
title: "Loops"
subtitle: "CSC120"
author: Patrick Earl
date: 02/16/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Repeating of code

* *Iteration* - Repeating a set of rules (or steps) over and over (...and over)
* Drawing lots of "legs"   
  * **Example 6-1**
  * **Example 6-2**

## Control Structures - Loops

* Similar to conditionals
  * "yes or no question" to determine how many times
* Loop Types
  * **while**
  * do-while
  * for

## While loops

* A conditional test
  * As long as the test evaluates to *True* continue the loop
* **Example 6-3**

## Infinite Loops

* "exit" condition
* Infinite Loops
  * The "exit" condition can never be meant
* **Example 6-4**
* **Example 6-5**

## For Loops

* Initialization, Boolean Test, Iteration Expression
* **Example 6-6**

## Variable Scope

* Global v Local Scope
* *Local* variables are only available to that code block

## Variable Scope

```
int num = 0;
int display_width = 200;
int display_height = 200;

void setup() {
    size(display_width, display_height);
    num = num + 1;
    // This isn't "local" to the setup block of code.
    num2 = 2;
}

void draw() {
    int num2 = 0;
    ...
    // More code here
    ...
}
```
* **Example 6-7**
* Exercise 6-4

## Loop in draw()

* The display isn't updated until the end of *draw()*
* **Example 6-8**
* **Example 6-9**

## Zoog w/ Loops

* **Example 6-10**
* **Example 6-11**