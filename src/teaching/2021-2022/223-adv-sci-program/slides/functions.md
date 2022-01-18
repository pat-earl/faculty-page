---
title: "Python Functions"
subtitle: "CSC223"
author: Patrick Earl
date: 02/01/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Using Functions

- Groups of code with a name
- `print('abc')`
  - The function *print* with *'abc'* as the function's argument
- Keyword Arguments
  - Arguments specified by name
  - `sep`

## Creating Functions

- `def` keyword
- No *type*
- Can return multiple items as a tuple

## Function Arguments

- Default Values
  - Optional argument with default value
- Flexible Arguments
  - `*args` & `**kwargs`

## Anonymous Functions

- `lamba`
- Useful for one-off functions
- Sorting a dictionary
- `add = lambda x, y: x + y`

### Lambda

* `sorted([2, 4, 3, 5, 1, 6])`
  
```
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]

sorted(data, key=lambda item: item['first'])
```


