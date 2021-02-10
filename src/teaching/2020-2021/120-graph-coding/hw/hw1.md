title: Assignment #1

**Due:**
: Friday Feb. 19, 2021

## Objectives

* Assess understanding of Processing concepts discussed up to this point.
* Creation of own Avatar
* pushMatrix and popMatrix

## Description

Make sure you're using Processing 3.X and not any older versions. If
using an on-campus machine, remember that files **must** be saved to another
location (like a flash-drive or networked student drive (S:)). You can 
change the default Sketchbook save location by opening *preferences*.

Create a new sketch and save it as **avatar** by going to *File* -> *Save As*.

Once your sketch is created, write code to achieve the following:

1. Create some immobile background scenery. (*Hint:* Plot this before the
avatar.) Keep them opaque, with differing colors
2. Create an avatar that is **not** the textbook's Zoog, sample avatar, or
another classmate's avatar. Call **pushMatrix()** before starting the avatar to 
save the window based x, y coordinate system. Call **translate** with coordinates 
for the center of the avatar's body. 0,0 is now it's reference appoint; 
use the center of it's body for this approximate reference point. Use at least one shape from *2D Primitives* (on the Processing
reference page) that Zoog *does not use*. Zoog uses *ellipse*, *line*, and *rect*.
    * Note the use of *rectMode* and *ellipseMode*, it's recommended to use **CENTER**. 
    * Use variations in color.
    * Use variations in alpha (transparency) 
    * Use *at least* 5 distinct shapes, meaning at least 5 body parts for the avatar. 
    * Call **popMatrix** before resuming display of foreground scenery; to restore origin (0,0)
    to the top left. 
    * Optional 1.5 bonus points for using **scale**, another 1.5 bonus for using **rotate** for the avatar. 
3. Create some immobile foreground scenery. (*Hint:* Plot this after the avatar.)
Keep them opaque, varying colors across time.
4. Your avatar must move horizontally and/or vertically at some rate. 
5. Your avatar *MUST* wrap back around to the other side of the window, *OR*
bounce back in opposite direction, when hitting the window's edge. 
6. Your avatar must have some "body part" that wiggles, grows/shrinks, or moves
in some manner, without becoming disconnected from the avatar. Step 6 may use the
modulo operator (`%`) which gives the remainder of division, to wrap back around
to it's starting point. You may also use an `if` statement instead. 

Use colors and alpha (*stroke()*, *file()*, and *background()*), *strokeWeight()*,
and a variety of of shapes. Get into creating a composition. Consult the [Processing Reference](https://processing.org/reference/)
and use some functions to make the animation exciting. 

## Grading

Each of the above 6 steps are worth 15% each (90% total). Half credit is available
for step 4 if warp-around doesn't work. 

The remaining 10% is for compositional effort. Which means creating a scene that
is a composition, as opposed to just a random collection of graphical features
that satisfy the above requirements. Students have done campus scenes, city scenes,
and scenes in space with a flying avatar in the past. Use your imagine and create
an actual scene. 

Reminder that there is an automatic 10% penalty for not documenting your code 
according to the CS&IT department's standards. For this assignment, place
this comment block at the top of your sketch and fill in the information.

```
/*******************************************************************************
*   Author: 
*   Creation Date: 
*   Due Date: 
*   Course: 
*   Professor: 
*   Assignment: 
*   Sketch Name:
*   Purpose: 
*******************************************************************************/
```

Also within your **setup()** and **draw()** functions, add some comments using
the `"//"`` comment delimiter to describe your avatar body part you are plotting. 
Similar to how Zoog's body parts are described in the textbook author's examples.

Sometime will be dedicated in class to work on this project. The expectation is
that you'll use this class time to work on your project and ask questions about it.

## Submission

Upload your completed file to the D2L Assignment named *Assignment 1 Avatar* 
by the due date. Reminder you have 3 budgeted grace days for the semester, see
the *Assignments/Projects* section in the first day handout for more info. Projects
**are not** accepted more than 3 days late. 