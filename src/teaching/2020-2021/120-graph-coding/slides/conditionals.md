---
title: "Chapter 5 - Conditionals"
subtitle: "CSC120"
author: Patrick Earl
date: 01/25/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Boolean Expressions

* Computers work with questions of *true* or *false*.
    - *boolean* tests
* *Boolean Expressions* will evaluate to either true or false
* Some Examples:
    - *15 is greater than 20* → **false**
    - *5 equals 5* → **true**
    - *32 is less than or equal to 33* → **true**

## Boolean Expressions

* `x > 20` - *Depends on x*
* `y == 5` - *Depends on y*
* `z <= 33` - *Depends on z*

## Relational Operators

* `>` - *greater than*
* `<` - *less than*
* `>=` - *greater than or equal to*
* `<=` - *less than or equal to*
* `==` - *equal to*
* `!=` - *not equal to*

## Conditionals

* Using *boolean expressions* 
* If the answer is *yes*, then execute these instructions.
    - Other if *no*, ignore the instructions.
* *If the mouse is on the left side of the screen, draw a rectangle on the left side of the screen*
* Using the `if` keyword

## Translated to code

```
if (mouseX < width/2) {
    fill(255);
    rect(0, 0, width/2, height);
}
```

* This can be expected with other keywords, like `else`
    - "otherwise do this"

## if, else

```
if (boolean expression) {
    // execute this code if the expression is true
}
else {
    // otherwise, execute this if expression is false
}
```

## if, else if, else

* Once last new keyword, `else if`
* Conditional statements are executed in order
* Once one evaluates to `true`, the rest are ignored

## if, else if, else

```
if (boolean expression #1) {
    // code to execute if expression #1 is true
}
else if (boolean expression #2) {
    // code to execute if expression #2 is true
}
else if (boolean expression #3) {
    // code to execute if expression #3 is true
}
else {
    // code to execute if none of the above
    // expressions are true
}
```
* Exercise 5-1

## Use in Sketches

* **Example 5-1**
* `constrain();`
    - Set a limit on value's maximum and minimum. 
* **Example 5-2**
