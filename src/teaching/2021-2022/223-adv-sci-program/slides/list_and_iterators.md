---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Python Iterators and List Comprehension**

CSC223 - Adv. Scientific Programming

Prof. Patrick Earl

Spring 2022

---

# List Iteration

```python
for value in [2, 4, 6, 8, 10]:
    print(value + 1, end = ' ')
```
- `iter()`
- Iterator objects give access to the `next` function.
- Represents a stream of data, where each call to the object returns the next item in the stream until the end. 

---

# range

- `range` doesn't actually create a list, it returns a range object.
    - One benefit is that a full list is never *explicitly* created.

```python
N = 10 ** 12
for i in range(N):
    if i >= 10: break
    print(i, end=', ')
```

---

# enumerate 

- Python provided way to keep track of the index in a list!

```python
L = [2, 4, 6, 8, 10]
for i, val in enumerate(L):
    print("Index:", i, "| Value", val)
```

---

# map

- *Higher-Order Function* - Takes a function as a parameter and returns a function.
- Returns an iterator that applies a *function* to every item in the iterable. 

```python
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end=' ')
```

---

# filter

- *Higher-Order Function*
- Same idea as `map()`, but only return elements from which the function returns true.

```python
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')
```

---

# List Comprehensions
- Direct way to create lists, usually in the case to generate a new list where the elements are the result an operation. 
- Comparing the following:
    - Using a for loop
    - Using a map
    - List Comprehension

---

- For Loop:
```python
squares = []
for x in range(10):
    squares.append(x)
```

- Map:
```python
squares = list(map(lambda x: x**2, range(10)))
```

- List Comprehension:
```python
squares = [x**2 for x in range(10)]
```

---

# List Comprehensions
- Consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. 
- `[expr for var in iterable]`

---

# Multiple Iteration
- Build a list from two values, using an additional `for` expression.

```python
[(i, j) for i in range(2) for j in range(3)]
```

---

# Conditionals
- Additional control can be added by using a condition at the end of the expression. 

```python
# Leave out multiples of 3
[val for val in range(10) if val % 3 > 0]
# Equivalent too
L = []
for val in range(20):
    if val % 3:
        L.append(val)
```

