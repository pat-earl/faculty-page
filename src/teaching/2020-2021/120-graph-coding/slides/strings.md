---
title: "Strings"
subtitle: "CSC120"
author: Patrick Earl
date: 03/23/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Strings
* A grouping of characters. 
* An array of characters, which *could* be written like this:
    * `char[] text = {'H', 'e', 'l', 'l', 'o'};`
* This is annoying, use a `String` object instead!
    * `String text = "Hello"`
* *NOTE the use of double quotes (")*
* Strings are objects with methods and data

---

* `charAt()`
* `length()`
```
for (int = 0; i < ???; i++) {
    char c = ???
    println(c);
}
```

## Display Text
* Text can be *rendered* on screen
* Steps to display text on screen:
    * Create a *PFont* variable: `PFont f;`
    * Specify a font: `f = createFont("Georgia", 16);`
    * (Optionally) Change the font size: `textFont(f, size);`
    * Specify a color: `fill(color);`
    * Use the text function to display: `text(<text to show>, x, y);`

---

## Other Text Operations
* The *String* object is a Java Programming Language feature
* `toUpperCase()`
* `toLowerCase()`
* `equals`
* `+` Operator - Concatenation

---

## Fonts
* Not every computer has the same selection of fonts
* `loadFont()` - *vlw* formatted font
* *Create Font* Tool
  * Allows for exporting a font on your computer to be packaged with the sketch

---

## Exercise 17-5
* Take the bouncing ball and display it's coordinates as text next to the ball
* Modify the ball object

---

## Text Animation
* Alignment - `textAlign() RIGHT, LEFT, CENTER`
* Width - `textWidth()` - Returns the width of any character or text string
* A scroll headline. `textWidth` allows us to know the position of the last text of character
* **Example 17-3**

---

## Rotating Text
* Rotate Text around it's center by translating to an origin point and using `textAlign(CENTER)` before showing the text
* **Example 17-5**
* **Exercise 17-8**

---

## Character by Character
* Sometimes we need to split a string into smaller chunks
  * Different Sizes
  * Colors
* **char_by_char**
* **Example 17-6**

---