---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Input/Output**

CSC223 - Advanced Scientific Programming

Spring 2022

Prof. Patrick Earl

---

# **String format() Method**

- The display of a string can be changed using the `.format()` method.
- Basic Example: `print("Good news, {}!".format("everyone!"))`
- Positional: 
    - `print("{0} and {1}".format('spam', 'eggs'))`
    - `print("{1} and {0}".format('spam', 'eggs'))`
- Using Keyword Args: 
    - `print("Most common pets are {cats} and {dogs}".format(cats='cats', dogs='dogs'))`

---

# Working with Numbers

- Formatting ints or floats:
    - `'{:d}'.format(42)`
    - `'{:f}'.format(3.14159265)`
- Padding:
    - `'{:5d}'.format(42)`
    - `'{:06.2f}.format(3.14159265)`
    - `'${:.2f}.format(9.99999)`
- More: <https://pyformat.info/>

---

# Manual Formatting

- `str.rjust()` 
- `str.center()`
- `str.ljust()`
- `str.zfill()`

---

# **Reading and Writing Files**

- File objects are created using the `open(filename, mode)` function 
- Mode describes how the file will be interacted with:
    - `r` - Read Only
    - `w` - Write Only (Deletes an already existing file)
    - `a` - Append (Writes to the end of the file)
    - `r+` - Open file for both reading and writing
    - `x` - Create a file, only if it doesn't exist. 
- Files are normally opened in "text" mode. 
- `f.close()` - To close a file

---

# Reading from files

- `f.read(size)` - Read *size* of data, or if omitted read the entire file.
- `f.readline()` Read a single line from a file
- Using a for loop.
- `list(f)` or `f.readlines()` - Creates a list with each line as an element of it.

---

# Writing to files

- `f.write()`
- `f.tell()` - Current position (Returns an opaque number in text mode)
- `f.seek(offset, whence)` - Move the position.

---

# Context Manager

- The recommended approach for interacting with files is the use the `with` keyword. 
- Once leaving the context, the file will be closed automatically. 

```python

with open('workfile') as f:
    read_data = f.read()

f.closed
```

---

# Common File Formats

- These are some common file formats found when working with scientific data. Python provides modules to work with them.
    - **CSV** - Comma Separated Values (there are also T(ab)SV, etc.)
    - **JSON** - JavaScript Object Notation
    - **SQLite** - A light-weight SQL database engine.
    - **HTML** - Hypertext Markup Language
    - **XML** - Extensible Markup Language