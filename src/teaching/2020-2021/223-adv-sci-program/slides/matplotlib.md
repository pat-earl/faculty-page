---
title: "Matplotlib"
subtitle: "CSC223"
author: Patrick Earl
date: 03/24/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: slide
---

## Matplotlib

* Visualization library built on Numpy Arrays
* Import Convention
  
```
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')
```

* Matplotlib was written as Python Alternative to *MATLAB*
  * A *MATLAB* style interface: pyplot
  * An object oriented interface: (Figures, Axes)

---

## Displaying Plots
* In a Script: `plt.show()`
* IPython Shell: 

```
%matplotlib # Magic Command
import matplotlib.pyplot as plt

# Use plt.draw() for updates, show isn't required
```

---

* *IPython Notebook*

```
%matplotlib notebook # Interactive Plots
%matplotlib inline # Static Images

import numpy as np
import matplotlib.pyplot as plt
```

---

## Script Example

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
```

---

## IPython Shell

```
%matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
```

---

## IPython Notebook

``` 
%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# Figures can be saved by using fig.savefig(<filename>)
fig.savefig('figure.png')
```

---

## MATLAB-Style

```
plt.figure() # Create a new figure

# Create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel #)
plt.plot(x, np.sin(x))

# Create a second panel and set the axis
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
```

---

## Object-Oriented Interface

```
# Create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)

# Call plot() method on appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
```

---

## Plot Customization Basics
* Plot Style
* Line Colors
* Line Styles
* Axes Limits
* Labels

---

## Line Color
* Use the `color` parameter in a *plot()*

```
plt.plot(x, y, color='blue') # By Name
plt.plot(x, y, color='g') # Color Code
plt.plot(x, y, color='0.45') # Gray Scale
plt.plot(x, y, color='#00FF00') # HEX
plt.plot(x, y, color=(1.0, 0.0, 0.0)) # RGB Scale 0 -> 1.0
plt.plot(x, y, color='chartreuse') # HTML Color Names
```

---

## Line Style
* Use the `linestyle` parameter to adjust the line style

```
plt.plot(x, y, linestyle='solid') 
plt.plot(x, y, linestyle='dashed') 
plt.plot(x, y, linestyle='dashdot') 
plt.plot(x, y, linestyle='dotted') 

# OR

plt.plot(x, y, linestyle='-') 
plt.plot(x, y, linestyle='--') 
plt.plot(x, y, linestyle='-.') 
plt.plot(x, y, linestyle=':')
```

---

## Axis Limits
* Limits can be set as follows:
  
```
# each axis individually
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# At Once
plt.axis([xmin, ymax, ymin, ymax])

# Automatically compute the limits
plt.axis('tight')

# Make axis units equal
plt.axis('equal')
```

---

## Labels
* Adding labels to a figure
  
```
# Title
plt.title("Plot Table")

# Axes
plt.xlabel("x")
plt.ylabel("y")

# Legend
plt.legend()
```

---

## Matplotlib Gotchas
* Most *plt* functions translate to *ax* methods
* But some to be aware of:
  * `plt.xlabel()` &#8594; `ax.set_xlabel()`
  * `plt.ylabel()` &#8594; `ax.set_ylabel()`
  * `plt.xlim()` &#8594; `ax.set_xlim()`
  * `plt.ylim()` &#8594; `ax.set_ylim()`
  * `plt.title()` &#8594; `ax.set_title()`
* `ax.set` can be used to set multiple properties at once

---

## Scatter Plots
* `plot` can take a character to use as a *marker*

```
# Example
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black')
```

---

## More plot arguments
* `plot` can take many arguments

```
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)
```

## Scatter
* Scatter plots can also be made with `scatter` method

```
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
           cmap='viridis')
plt.colorbar()
```