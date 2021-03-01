---
title: "Iterators - Chapter 10"
subtitle: "CSC223"
author: Patrick Earl
date: 02/22/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Iterators
* Repeating something over and over in an automated fashion
* Python *iterator* syntax
* *range* - Produces an iterator

## List Iteration
* `for x in y:`
  * `for [each] value in [the] list
* Iterable interface
  * `iter`
* `next`
* Allows for interpreting things as a list

## range()
* Actually creates a *range* object
  * List is never created
```
N = 10 ** 12
for i in range(N):
    if >= 10: break
    print(i, end=', ')
```

## itertools count
* count() will create an infinite range
```
from itertools import count

for i in count():
    if >= 10:
        break
    print(i, end=', ')
```

## Useful Iterators
* enumeration
* zip
* *map*
* *filter*
* *Represents a higher-order function*

## Enum and Zip

* `for i, val in enumerate(L):`
* `zip`
  * "Zips" iterators together

## map and filter

* `map()` takes a function and applies it to the values in an iterator
* Type casting iterator values 
* `filter()` works similar
  * Only values that eval to *True* are returned

## Iterators as Function Args

* `*` Prefix operator can be used on any iterator
* `print(*range(10))`
* `print(*map(lambda x: x ** 2, range(10)))`
* "unzip" - `zip(*iterator)`