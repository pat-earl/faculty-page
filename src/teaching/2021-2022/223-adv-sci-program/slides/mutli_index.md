---
title: "Pandas - Hierarchial Indexing"
subtitle: "CSC223"
author: Patrick Earl
date: 03/31/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Hierarchical Indexing
* Pandas supports higher-dimensional data through the use of `Panel` & `Panel4D`.
* More common to use Hierarchical Indexing.
    * aka *multi-indexing*
* Higher-Dimensional Data can be represented within a 1D *Series* or *DataFrame* object.

---

## Multiply Indexed Series
* Using tuples as keys

```

index = [(1, 'A', 2, 'A', 1, 'B', 2, 'B')]
s1 = pd.Series([1.0, 2.0, 3.0, 4.0], index=index)

```

* Selecting data could be done like so

```
s1[[i for i in s1.index if i[0] == 2]]
```

## Pandas MultiIndex
* *MulitIndex* object allows for more operations than basic tuple indexing
    * Contains multiple levels of indexing and labels for each data point.

```
index = pd.MultiIndex.from_tuples(index)

s1 = s1.reindex(index)
```

* Blank values in the index columns represent the same value above it
* Accessing data in a specific column becomes easy

```
s1[1, :]
```

---

## MultiIndex as a Dimension
* This series could be stored as a *DataFrame*.
* Using the `unstack()` method can easily convert this series to one.
* `stack()` will do the opposite.


```
s1_df = s1.unstack()
```

---

* With this flexibility it is easy to add another column and put data in the correct spot

```
s1_df = pd.DataFrame({'data1': s1, 'data2': [5.0, 6.0, 7.0, 8.0]})
```

---

* All standard Pandas operations will work on multi-indexed data

```

x = s1_df['data1'] + s1_df['data2']

x.unstack()
```

---

## Creating MutliIndexes
* Pass a list of two or more index arrays to the constructor. 

```

df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])

df
```

* A dictionary with appropriate tuples as keys:

```
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)
```

---

* `from_arrays()`

```
pd.MultiIndex.from_arrays([['A','A','B','B'], [1,2,1,2]])
```

* `from_tuples()`

```
pd.MultiIndex.from_tuples([('A',1),('A',2),('B',1),('B',2)])
```

* Cartesian Product

```
pd.MultiIndex.from_product([['A','B'],[1,2]])
```

---

## MutliIndex Level Names
* Levels of a multi-index can be named

```
s1.index.names = ['one', 'two']
```

---

## MultiIndex as Columns

```

# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data
```

---

* Get medical records for a specific person:  

```

health_data['Bob']

health_data['Sue', 'HR']

```