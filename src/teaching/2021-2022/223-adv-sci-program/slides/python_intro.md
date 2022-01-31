---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
size: 16:9
---

# **Python Language**

- *Interpreted* & *Dynamic* Programming Language
- Statements can be interactively ran and tested
- Various Ways:
  - The Python Interpreter
  - IPython Interpreter
  - Self-Contained Scripts
  - Jupyter Notebooks 

--- 

# Using the Interpreter

Can be launched in a command window by typing `python`. 

This environment is called a ***REPL*** - Read, Evaluate, Print, Loop

---

# IPython Interpreter

More featured filled version of the interpreter.

Adds the following:
- Input/Output Numbering
- History
- Syntax Highlighting
- Auto Tabs
- Much More

---

# Self-Contained Scripts

Statements are saved to a source file much like any programming language.

Python source code files end in `.py`

To run a Python file, you'd type: `python [file path]`

---

# Jupyter Notebook

Notebook system that allows for the creation of cells. Each cell can contain 
Python statements. Typically used for Data Science Purposes.

Will use these for doing Matplotlib visualizations. 

---

# **Example Program**

```python
# set the midpoint 
midpoint = 5

# make two empty lists
lower = []; upper = []

# split the numbers into lower and upper
for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)

print("lower:", lower)
print("upper:", upper)
```

--- 

# Variables

Variable type isn't explicitly stated. Variable Type will be set based
on the value stored. 

- Variables are a *pointer* to a space in memory. 
    - Why? Every thing in Python is an *object*

---

# Objects

- Entity that contains data along with metadata and/or functionality.
  - Metadata - *Attributes*
  - Functionality - *Methods*
  - Access these properties using the dot syntax (`"word".upper()`)

---

# Arithmetic Operators

| Operator | Name |
| --- | --- |
| a + b | Addition |
| a - b | Subtraction |
| a * b | Multiplication |
| a / b | Division |
| a // b | Floor Division |
| a % b | Modulus | 
| a ** b | Exponentiation |

---

# Bitwise Operations

| Operator | Name |
| --- | --- |
| a & b | Bitwise AND |
| a | b | Bitwise OR |
| a ^ b | Bitwise XOR |
| a << b | Bit shift Left |
| a >> b | Bit shift Right |
| ~a | Bitwise NOT |

---

# Others

| Operator | Name |
| --- | --- |
| = | Assignment |
| a == b | Equal To |
| a < b | Less Than |
| a <= | Less Than or Equal To |
| and, or, not | |

---

# Membership Operators

- Check for membership within compound objects
- `3 in [3, 4, 6]`
- `4 not in [2, 4, 6]`