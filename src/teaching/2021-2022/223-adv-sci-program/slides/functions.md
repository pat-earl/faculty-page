---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Python Functions**

CSC223 - Advanced Scientific Programming

Spring 2022

Prof. Patrick Earl

---

# Using Functions

- Groups of code with a name
- `print('abc')`
- Normal Arguments
- Keyword Arguments
  - Named arguments using `key=value` pairings.

---

# Creating Functions

- `def` keyword
- No *type*
- Can return multiple items as a tuple

---

# Function Arguments

- Default Values
  - Optional argument with default value
- Flexible Arguments
  - `*args` & `**kwargs`

---

# *Flexible Arguments*

```python
def catch_all(*args, **kwargs):
  print("args=", args)
  print("kwargs=", kwargs)
```

---

# Anonymous Functions

- `lamba`
- Useful for one-off functions
- Sorting a dictionary
- `add = lambda x, y: x + y`

---

# Lambda

- `sorted([2, 4, 3, 5, 1, 6])`
  
```
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]

sorted(data, key=lambda item: item['first'])
```


