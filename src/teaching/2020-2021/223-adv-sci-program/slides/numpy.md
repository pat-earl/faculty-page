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

## Creating arrays
* `np.zeros`
* `np.ones`
* `np.fill`
* `np.arange`
* `np.linspace`

## NumPy Data Types
* Contains data types similar to C
    * *NumPy is written in C*
* *int_*
* *int32* - 32 Bits
* *int64* - 64 Bits
* *uint16* - Unsigned 16 bit int
* *float_* - short hand for *float64*