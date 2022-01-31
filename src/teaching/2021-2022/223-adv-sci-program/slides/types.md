---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
size: 16:9
---

# **Python Data Types**

CSC223 - Advanced Scientific Programming

Prof. Patrick Earl

Spring 2022

---

# Python Simple Types
- *Scalar* types - One Dimensional 
- *int* - `x = 1`
- *float* - `x = 1.2`
- *complex* - `x = 1 + 2j`
- *bool* - `x = True`
- *str* - `x = 'abc'`
- *NoneType* - `x = None`

---

# Integers

- Basic Numerical Type
- Numbers without decimal points
- Can handle larger numbers than typical languages
  - `2 ** 200`
- Division up-casts to floating point

---

# Floating-Point

- Used to store fractional numbers
- Can be defined in two ways:
  - Standard: `x = 0.0000005`
  - Exponential Notation: `y = 5e-6`
- *Precision*

---

# Complex Numbers

- `complex(1, 2)`

---

# String Type

- Strings are created with single or double quotes
- Useful methods:
  - `len()`
  - `.upper()`
  - `.capitalize()`
  - `'test string' + 's'` - ***concatenation***
  - `"test" * 5` - ***concatenation*** by multiplication 
  - `message = 'hello'; message[0]`

---

# NoneType

- Default function return 
- Only one type of value `None`

---

# Boolean Type

- Two Values: `True` or `False`
- *case-sensitive* 

---

# Data Structures

- Python has built-in compound types
  - Lists
  - Tuples
  - Dictionaries
  - Sets

---

# Lists

- Basic ordered and mutable data collection
- `l = [1, 2, 3, 4]`
- Useful methods, properties:
  - `len()`
  - `.append()`
  - Concatenation - `+`
  - `.sort()`
- Python lists can contain objects of any type

---

# List Indexing

- Access a single element through *indexing*
- `l = [2, 3, 5, 7, 11]`
- Zero-Based indexing
- Negative Indexing

---

# List Slicing

- Slicing allows for accessing multiple values in a sub-list
- Inclusive start point, Non-inclusive end point
- `l[0:3]`
- `l[:3]; l[3:]`
- `l[::2]`
- `l[1:3] = [55, 66]`

---

# Tuples

- Similar to lists, but *immutable*
- Once created, size and contents cannot be changed

---

# Dictionaries

- Key:Value pairs
- `numbers = {'one':1, 'two':2}`
- Access via key in dictionary
  - `numbers['two']`
- Add via Indexing

---

# Sets

- Unordered Collections of Unique Items
- Defined using brackets
  - `evens = {2, 4, 6, 8, 10}`
  - `odds = {1, 3, 5, 7, 9}`
- Operations
  - Union `|` - Items appearing in either
  - Intersection: `&` - Items appearing in both
  - Difference: `-` - Items in left, not right
  - Symmetric Difference `^` - Items only appearing in one set

---  

# Multidimensional Lists

- Python supports 2D, 3D, etc. lists
- List in a List
- Type Mixing
