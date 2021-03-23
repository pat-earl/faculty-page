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