---
title: "Pandas - String Operations"
subtitle: "CSC223"
author: Patrick Earl
date: 04/14/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: slide
---

## Pandas String Operations
* NumPy doesn't have the ability to generalize string operations like arithmetic. 
  
```
x = np.array([2, 3, 5, 7, 11, 13])
x * 2

>>> array([4, 6, 10, 14, 22, 26])
```

---

## Pandas String Operations

* Without the access to this generalization with NumPy, we have to use verbose loops:

```
data = ['Elfo', 'Shocko', 'speako', 'LEaVo', 'Pops']
[w.capitalize() for w in data]

>>> ['Elfo', 'Shocko', 'Speako', 'Leavo', 'Pops']
```

* However, if one is missing this will break. 

```
data = ['Elfo', 'Shocko', 'speako', None, 'Pops']
[w.capitalize() for w in data]

...
>>> AttributeError: 'NoneType' object has no attribute 'capitalize'
```

---

## Pandas String Operations
* Pandas includes features to address the need for vectorized string operations

```
elves = pd.Series(data)
elves.str.capitalize()
```

* Often times when dealing with real-world string data, it's going to be messy.
* i.e User-Entered Data:
  * Names
  * Street Address
  * City
  * State

---

## Pandas String Methods

* Most of Python's built in str methods are reflected in the Pandas str 

| len | lower | translate | islower |
| ljust | upper | startswith | isupper |
| rjust | find | endswith | isnumeric |
| center | rfind | isalnum | isdecimal |
| zfill | index | isalpha | split |
| strip | rindex | isdigit | rsplit |
| rstrip | capitalize | isspace | partition |
| lstrip | swapcase | istitle | rpartition |

## Regular Expressions

| Method | Description |
| -- | -- |
| `match()` | Call `re.match()` on each element, returning a boolean. |
| `extract()` | Call `re.match()` on each element, returning matched groups as strings | 
| `findall()` | Call `re.findall()` on each element |
| `replace()` | Replace occurrences of pattern with some other string |
| `contains()` | Call `re.search()` on each element, returning a boolean |
| `count()` | Count occurrences of pattern |
| `split()` | Equivalent to `str.split()`, but accepts regexps |
| `rsplit()` | Equivalent to `str.rsplit()`, but accepts regexps |

---

* Example: Find all elf names that end with 'o'.

```
elves.str.findall(r'.*o$')

0      [Elfo]
1    [Shocko]
2    [speako]
3        None
4          []
dtype: object
```

---

* Using regexp on different phone number formats:
  * Doesn't handle *every* format

```
phones = pd.Series(['484-555-1234', '(484) 555 1234', '484 555-1234', '+1 484-555-1234'])
```

---

## Other useful methods

| Method | Description | 
| -- | -- |
| `get()` | Index each element |
| `slice()` | Slice each element |
| `splice_replace()` | Replace slice in each element with passed value |
| `cat()` | Concatenate strings |
| `repeat()` | Repeat values | 
| `normalize()` | Return Unicode form of string| 
| `pad()` | Add whitespace to left, right, or both sides of strings |
| `wrap()` | Split long strings into lines with length less than a given width |
| `join()` | Join strings in each element of the Series with passes separator | 
| `get_dummies()` | Extract dummy variables as a DataFraame |

---