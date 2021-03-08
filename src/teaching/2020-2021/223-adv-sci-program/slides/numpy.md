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
* Default Python Implementation is *slow* 
  * Looping over arrays for operations on each element
* `%timeit`
* *Vectorized Operations* - UFuncs
  * Functions performed on the entire array
  
---

* Array Arithmetic
  * Pythons *native* arithmetic operators can be used
  * `add`
  * `subtract`
  * `negative`
  * `multiply`
  * `divide`
  * `floor_divide`
  * `power`
  * `mod`

## Aggregations

* *Numpy Built-ins*
* Sum
* Min & Max
* Any - Any elements are True
* All - All elements are True
* Std - Standard Deviation
* Mean - Mean of elements
* argmin, argmax - Find index of min & max values

---

* Multi-Dimensional Aggregation
  * *axis* - Dimension of the array that will be collapsed.
  * Aggregations can be performed along a row, column, or the whole array
* Example:
```M = np.array([[1,2,3], [4,5,6]])
M.sum(axis=0)
M.sum(axis=1)
```
---

## Broadcasting

* Rules for applying ufuncs on arrays of different sizes
* The Rules:
   1. If two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side
   2. If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape
   3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised

---

## Boolean Arrays

* Comparison
  * `less or <`
  * `less_equal or <=`
  * `greater or >`
  * `greater_equal or >=`
  * `equal or ==`
  * `not_equal or !=`

---

## Working with Boolean Arrays

* `count_nonzero`
* `np.sum`

---

## Boolean Masks
* Masking operations
* `x[x < 5]`
* Return a 1D array filled with the values that meet the condition. 

## Fancy Indexing

* Allows for passing of an array of indices, in place of single scalars
* `idx = [3, 7, 4]`
* `x[idx]`

## Sorting
* `np.sort` - Returns a new array with the values sorted
  * Use `x.sort()` to sort in-place
* `np.argsort` - Return the indices of the sorted elements.