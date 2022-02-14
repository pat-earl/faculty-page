---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
size: 16:9
---

# **Errors & Exceptions**

CSC223 - Advanced Scientific Programming

Prof. Patrick Earl

Spring 2022

---

## Error Types

- **Syntax Errors** - Invalid Python Code
- **Runtime Errors** - Syntactically valid code that fails for some reason
- **Semantic Errors** - Errors in logic

## Runtime Errors

- Python will provide an *Exception* type
- `try` & `except`
- *FileNotFoundError*

## Raising Exceptions

- `raise`

## Exception Message

- Capture the Exception message
- `except Error as message:`

## try...except

```python
try:
    print("try something here")
except:
    print("this happens only if it fails")
else:
    print("this happens only if it succeeds")
finally:
    print("this happens no matter what")
```