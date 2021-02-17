---
title: "Errors & Exceptions"
subtitle: "CSC223"
author: Patrick Earl
date: 02/15/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Error Types

* **Syntax Errors** - Invalid Python Code
* **Runtime Errors** - Syntactically valid code that fails for some reason
* **Semantic Errors** - Errors in logic

## Runtime Errors

* Python will provide an *Exception* type
* `try` & `except`
* *FileNotFoundError*

## Raising Exceptions

* `raise`
* Fibonacci Sequence (Non-Negative Numbers)

## Exception Message

* Capture the Exception message
* `except Error as message:`

## try...except

```
try:
    print("try something here")
except:
    print("this happens only if it fails")
else:
    print("this happens only if it succeeds")
finally:
    print("this happens no matter what")
```