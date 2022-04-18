---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
title: "Pandas Combining Data"
---

# **Pandas - Combining Data**

CSC223 - Advanced Scientific Programming

Prof. Patrick Earl

Spring 2022

---

## Combining Data
- Data Science/Analysis requires combining of data from a similar or different sources.
- Pandas provides functionality to combine the `Series` and `DataFrame` objects.
- Concatenation/Appending
- Merging/Joining

---

## Concatenation
- Pandas provides the `concat` function to concatenate `Series` or `DataFrame` objects.
- `concat` takes a sequence or mapping of `Series` or `DataFrame` objects.

---

## Concatenation 
- The Pandas `concat` function has additional keyword arguments that effect the concatenation
- Some examples:
  - `axis`: Which axis to concatenate on.
  - `ignore_index`: If True, do not use the index values along the concatenation axis
  - `verify_integrity`: If True, raises an exception when there are duplicate indices.
  - `keys`: Construct a hierarchical index using the key values
  - `join`: Specify an inner or outer join

---

## Concatenation Examples
- Function for quick creation of DataFrames
```python
In [2]: def make_df(cols, ind):
   ...:     data = { c: [str(c) + str(i) for i in ind]
   ...:             for c in cols}
   ...:     return pd.DataFrame(data, ind)
   ...:

In [3]: make_df('ABC', range(3))
Out[3]:
    A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
```

---

- Concat on default axis

```python
In [4]: df1 = make_df('AB', [1, 2])

In [5]: df2 = make_df('AB', [3, 4])

In [6]: pd.concat([df1, df2])
Out[6]:
    A   B
1  A1  B1
2  A2  B2
3  A3  B3
4  A4  B4
```

---

- On a different axis
```python
In [7]: df3 = make_df('AB', [1, 2])

In [8]: df4 = make_df('AB', [1, 2])

In [10]: pd.concat([df3, df4], axis=1)
Out[10]:
    A   B   A   B
1  A1  B1  A1  B1
2  A2  B2  A2  B2
```

---

- Duplicate Indices

```python
In [11]: x = make_df('AB', [0, 1])

In [12]: y = make_df('AB', [2, 3])

In [13]: y.index = x.index

In [14]: pd.concat([x, y])
Out[14]:
    A   B
0  A0  B0
1  A1  B1
0  A2  B2
1  A3  B3
```

---

- Catching duplicates

```python
In [15]: pd.concat([x, y], verify_integrity=True)

ValueError: Indexes have overlapping values: Int64Index([0, 1], dtype='int64')
```

---

- Ignore the index

```python
In [18]: pd.concat([x, y], ignore_index=True)
Out[18]:
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
3  A3  B3
```

---

- Using MutliIndex Keys
```
In [19]: pd.concat([x, y], keys=['x', 'y'])
Out[19]:
      A   B
x 0  A0  B0
  1  A1  B1
y 0  A2  B2
  1  A3  B3
```

---

## Merging
- Relational algebra provides a formal set of rules for manipulating relational data.
- Pandas' `merge` function provides an interface to perform these operations.
- Categories of joins:
  - *one-to-one*
  - *many-to-one*
  - *many-to-many*

---

## One-to-one
- Using one-to-one joins is similar to column-wise concatenation.
- This example works when at least one column has the same values in both DataFrames.

```python
df1 = pd.DataFrame([['Bob', 'Alice', 'Eve'], ['A', 'B', 'B']], columns=['name', 'group'])
df2 = pd.DataFrame([['Eve', 'Alice', 'Bob'], [1, 2, 3]], columns=['name', 'number'])

In [10]: pd.merge(df1, df2)
Out[10]:
    name group  number
0    Bob     A       3
1  Alice     B       2
2    Eve     B       1
```

---

## Many-to-one
- One of the two key columns contains duplicate entires.
  - The *key* being the shared column between the datasets

```python
df3 = pd.DataFrame([['A', 'B', 'C'], ['math', 'programming', ['biology']], columns=['group', 'skill'])

In [13]: pd.merge(df1, df3)
Out[13]:
    name group        skill
0    Bob     A         math
1  Alice     B  programming
2    Eve     B  programming
```

---

## Many-to-many
- The key column in both the *left* and *right* data sets contain duplicate values.

```python
df4 = pd.DataFrame({'group': ['A', 'B', 'B'], 'leaders': ['Jack', 'John', 'Jill']})

In [19]: pd.merge(df1, df4)
Out[19]:
    name group leaders
0    Bob     A    Jack
1  Alice     B    John
2  Alice     B    Jill
3    Eve     B    John
4    Eve     B    Jill
```

---

## Merge Options
- Merge also has other key arguments
  - `on`: Which column should be the key.
  - `left_on` and `right_on`: Specify a key column with different names in each table
  - `left_index` and `right_index`: Merge on index instead of column
  - `how`: Specify inner, outer, left, or right join
  - `suffixes`: Append a suffix to any conflicting column names.