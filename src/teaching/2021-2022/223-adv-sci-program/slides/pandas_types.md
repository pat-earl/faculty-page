---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Pandas - Types**

CSC223 - Advanced Scientific Programming

Spring 2022

Prof. Patrick Earl

---

## Pandas
- Package built on top of NumPy
- Provides implementation of DataFrames
  - Multidimensional arrays with row & column labels
- `import pandas`
- Same convention as NumPy
- `import pandas as pd`


---

## Pandas Objects
- Series
- DataFrame
- Index

---

## Series
- One-Dimensional array of *indexed* data.
- Can be created from a list or np.array
  - `data = pd.Series([0.25, 0.5, 0.75, 1.0])`
- `data.values`
- `data.index`

---

- Data can be accessed by the associated index
- `data[1]`
- `data[1:3]`

---

- NumPy arrays have a *implicitly* defined integer index
- Panda Series provide *explicitly* defined indexes associated with values
  - Default index is *zero-based* numeric
  
```python
data = pd.Series([0.25, 0.5, 0.75, 1.0],
    index=['a', 'b', 'c', 'd'])

print(data['a'])
```

---

## Series Attributes
- index: an index object
```
In [5]: s1 = pd.Series([4, 5, 6 )
In [6]: s1.index
Out[6]: RangeIndex(start=0, stop=3, step=1)
In [7]: s2 = pd.Series({100: 1, 200:3, 400:5}
In [8]: s2.index
Out[8]: Int64Index([100, 200, 400], dtype='int64')
```
- values: The NumPy Array
```
In [9]: s1.values
Out[9]: array([4, 5, 6], dtype=int64)
In [10]: s2.values
Out[10]: array([1, 3, 5], dtype=int64)
```

---

## Pandas DataFrames
- DataFrames is an analog of two-dimensional arrays with flexible row indices and flexible column names
  - Or a sequence of aligned *Series* objects, sharing a similar index
- Each column in a *DataFrame* is a *Series*
- *DataFrames* can be constructed from:
  - Single Series
  - List of Dicts
  - Dict of Series
  - 2-D NumPy Array

---

## Pandas DataFrame Examples
```
In [11]: df = pd.DataFrame([[1,2,3], [4, 5, 6]])
In [12]: df
Out[12]: 0  1  2 
      0  1  2  3
      1  4  5  6
In [13]: df.index
Out[13]: RangeIndex(start=0, stop=2, step=1)
In [15]: df.columns
Out[15]: RangeIndex(start=0, stop=3, step=1)
```

---

```
In [20]: pd.DataFrame(np.ones((4,2)),
        columns=['one', 'two'],
        index=['a', 'b', 'c', 'd']) 
Out[20]: one  two
      a  1.0  1.0
      b  1.0  1.0
      c  1.0  1.0
      d  1.0  1.0
```

---

- Adding Columns
  - `df[new_column] = [new, values]`
- Removing Columns
  - `df.pop()`
  - `del df['column']`

---

## The Index Object
- *Index* object can be considered an *immutable* array or *ordered set* (Can contain dups though)
- `ind = pd.Index([2, 3, 5, 7, 11])`
- As an array:
  - `ind[1]`
  - `ind[::2]`

---

## Data Indexing
- Series as a Dictionary
  - Data Selection and Modification via the Key
- Array-Style Interface (*slices, masking, and fancy indexing*)

---

- Indexers
  - `data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])`
  - `data.loc[1]` - Indexing and Slicing always reference these explicit index
  - `data.iloc[1]` - Referencing the implicit indexing
  
---

## DataFrame Summary

| Operation | Syntax | Result Type |
| -- | -- | -- |
| Select a column | df[col] | Series |
| Select row by label | df.loc[label] | Series |
| Select row by integer location | df.iloc[loc] | Series |
| Slice Rows | df[5:10] | DataFrame |
| Select rows by boolean vector | df[bool_vec] | DataFrame |

---

## UFuncs
- Indices are preserved with ufuncs
- Indices are aligned when performing binary ufuncs
- Alignment is preserved when performing operations between *DataFrame* and *Series* objects

---

## Missing Data
- `None` and `NaN` - Null (missing) values
- Functions for missing data:
  - `isnull()`
  - `notnull()`
  - `dropna()` - Filter out missing values
  - `fillna()` - Fill NaNs with specified value