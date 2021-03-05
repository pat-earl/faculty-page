---
title: "NumPy"
subtitle: "CSC223"
author: Patrick Earl
date: 03/03/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Using NumPy
* `import numpy`
* `import numpy as np`

---

## Python Integer 

```
struct _longobject {
    long ob_refcnt;
    PyTypeObject *ob_type;
    size_t ob_size;
    long ob_digit[1];
};
```
* Flexibility comes at a cost.
* Since lists can contain any object, there is more overhead

---

## Fixed-Type Arrays

* Python provides the built-in `array` module
* Provides effective storage of array-based data, but not the *operations*
* `import array; L = list(range(0)); A = array.array('i', L)

---

## NumPy Arrays

* `np.array` can be used to create arrays from Python lists
* NumPy arrays must be of the same type.
    * `dtype` argument

--- 

## Creating arrays
* `np.zeros`
* `np.ones`
* `np.fill`
* `np.arange`
* `np.linspace`

--- 

## NumPy Data Types
* Contains data types similar to C
    * *NumPy is written in C*
* *int_*
* *int32* - 32 Bits
* *int64* - 64 Bits
* *uint16* - Unsigned 16 bit int
* *float_* - short hand for *float64*

--- 

## NumPy Array Basics
* Attributes of Arrays
* Indexing of Arrays
* Slicing of Arrays
* Reshaping of Arrays
* Joining and Splitting

--- 

## Attributes
* `np.random.randint(10, size=6)`
* `ndim` - Number of dimensions
* `shape` - The size of each dimensions
* `size` - The total size
* `dtype` - The data type of the array
* `itemsize` - Size in bytes of each element
* `nbytes` - Total size of the array

--- 

## Array Indexing:
* Access element *i*th value starting at zero
  * Supports negative indexing as well
* For multidimensional arrays, comma separated tuple
  * `array[0, 0]`
  * Negative indices work here
  * Can be used for modification

---

## Array Slicing
* Access a subarray
* Follows the Python Syntax
  * `x[start:stop:step]`
  * Negative Steps
    * Start and Stop get swapped
    * `x[::-1]`
* Multi-Indexing
  * Works the same, just separated with commas
  * `x[:2, :3] # Two Rows, Three Columns`

---

* Accessing rows & columns
  * Combine indexing & slicing
  * `x[:, 0] # First column of x`
  * `x[0, :] # First row of x`
* Subarrays are *views* instead of copies
* Use `.copy()` method 

---

## Array Reshape
* `.reshape`
* `np.arange(1, 10).reshape((3,3))`
  * Usually a no-copy view
* Conversion of 1D in too 2D row or Column Matrix
  * `x.reshape((1, 3))`
  * `x[np.newaxis, :]`

---

## Array concat & split
* Concatenation
  * `np.concatenate`
  * `np.vstack`
  * `np.hstack`
* Splitting
  * `np.split`
  * `np.hsplit`
  * `np.vsplit`

---

## Universal Functions

---

## Aggregations
* 1D

---
* 2D

---

## Broadcasting

---

## Boolean Arrays

---

## Fancy Indexing

---

## NumPy Sorting
