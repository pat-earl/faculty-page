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

## Logical Operators

* Sometimes, one logical test isn't enough
  * Events happen based on more than one condition.
* *If the mouse is on the right side of the screen **AND** the mouse is on the bottom of the screen, draw a rectangle in the bottom right corner.*
* Could use a *nested if statement*
  * The rectangle is drawn if both *if* statements result in a *true*

## Logical Operators

* The same can be achieved with a simpler *LOGICAL AND*
  * `&&` in Processing
* Others:
  * `||` - *LOGICAL OR*
  * `!` - *LOGICAL NOT*

## LOGICAL AND

| Operand | Result | 
| --- | --- |
| TRUE && TRUE | TRUE | 
| TRUE && FALSE | FALSE | 
| FALSE && TRUE | FALSE |
| FALSE && FALSE | FALSE |

The *logical AND* is only *true* if both operands are **TRUE**

## LOGICAL OR
| Operand | Result |
| -- | -- |
| TRUE \|\| TRUE | TRUE |
| TRUE \|\| FALSE | TRUE |
| FALSE \|\| TRUE | TRUE |
| FALSE \|\| FALSE | FALSE |

The *logical OR* is only *false* if both operands are **FALSE**

## LOGICAL NOT

| Operand | Result |
| -- | -- |
| !TRUE | FALSE |
| !FALSE| TRUE |

The *logical NOT* is known as a unary operator. It flips the result, therefore making
*NOT TRUE* equivalent to *FALSE*.

## Convert the example from earlier

* These *boolean* expressions are sometimes called *compound* expressions
* Remove the *nested if* and make it a *compound* expression

## Example 5-5

* Let's exam the logic of this program using pseudocode (plain English in this case)
* Setup:
  * Make the window 200 x 200 pixels.

## Example 5-5

* Draw:
  1. Draw a white background.
  2. Draw horizontal and vertical lines to divide the window in four quadrants.
  3. If the mouse is in the top left corner, draw a black rectangle there.
  4. If the mouse is in the top right corner, draw a black rectangle there.
  5. Do the same of the bottom corners...

## Boolean Variables

* `boolean` type variables can only hold two values: *true* or *false*.
* These variables can be used as a switch, *on* or *off*
* Use this to make a button
* **Example 5-4**
* **Example 5-5**

## Keeping things

* In the last *Zoog* example, the body flew off the screen to not return.
* We can use conditionals to keep items on screen
* **Example 5-6**
* **Example 5-7**
* **Example 5-8**

## Physics

* With variables and conditionals, we can simulate gravity.
* Quick Refresher: 
  * Gravity is the force of attraction between all masses.
  * When a pen is dropped, earth causes the pen to accelerate towards the earth (Which is much larger than the pen)
* *Acceleration* is caused by gravity (and many other forces which we'll ignore for simplicity)
* `speed = speed + acceleration`