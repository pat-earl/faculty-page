---
title: "Chapters 11 & 12"
subtitle: "CSC120"
author: Patrick Earl
date: 04/15/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: fade
---

## Debugging
* General Tips
    * Take a break
    * Ask a friend.
    * Simplify
        * Added a new feature recently? Start taking stuff out until things work again
    * Use `println()` 
        * Check the value of a variable as things go on. 
        * Or better, use the *Debug* menu. 

---

## Libraries
* Code written by others.
    * Sometimes referred to as *helper* code. 
* Processing does an `import` statement by default
  
```
import processing.core.*;
```

---

## The Built-Ins
* Processing provides some libraries that don't require additional installation steps. 
    * Serial
    * Network
    * PDF
    * Video
    * Sound
* If you wanted to import the Network library:

```
import processing.net.*
```

---

## Contributed Libraries
* Known as *Third-Party* libraries. 
* Code written by parties outside of the *Processing* foundation.
* Can be searched and installed by going to *Sketch* &#8594; *Add Library*.
* You have the ability to write your own libraries as well, but that's outside our scope. 
