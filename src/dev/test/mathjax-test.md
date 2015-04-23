title: MathJax tests
active: dev/test

## Some Math Imported from the 372 media-wiki page.

### Rotational Symmetry of the Laplacian

Let $T:\R^2 \to \R^2$ be a rotation, and $u$ be any function.
Then
$$
    \lap (u \circ T) = (\lap u) \circ T
$$
This is also true in higher dimensions.

Given that the Laplacian has this rotational symmetry, one might expect a nice cancellation / compact formula for the Laplacian in polar coordinates.
We try this next.

### The Laplacian in Polar Coordinates

Let $\hat x$, $\hat y$ be the unit vectors in the $x$ and $y$ direction respectively, and let $\hat r$ and $\hat \theta$ be the unit vectors in the $r$ and $\theta$ direction respectively.
Explicitly,
$$
  \hat x = \begin{pmatrix}1\cr 0\end{pmatrix},\quad
  \hat y = \begin{pmatrix}0\cr1\end{pmatrix},\quad
  \hat r = \frac{1}{r}\begin{pmatrix}x\cr y\end{pmatrix},\quad
  \hat \theta = \frac{1}{r}\begin{pmatrix}-y\cr x\end{pmatrix}.
$$

First we compute that
$$
  \grad u = \partial_x u \hat x + \partial_y u \hat y = \partial_r u \hat r + \frac{1}{r} \partial_\theta u \hat \theta.
$$
Now we compute
\begin{multline*}
  \lap u
    = \dv \grad u
    = (\grad \partial_r u) \cdot \hat r + \partial_r u (\dv \hat r) + (\grad \frac{1}{r} \partial_\theta u) \cdot \hat \theta + 0
  \\
    = \partial_r^2 u + \partial_r u (\dv \hat r) + \frac{1}{r^2} \partial_\theta^2 u.
\end{multline*}

To finish the calculation, we only need to compute $\dv \hat r$.
We do this as follows
$$
  \dv \hat r = \dv \left( \frac{1}{r} \begin{pmatrix} x \cr y \end{pmatrix} \right)
    = \frac{2}{r} + \grad\left( \frac{1}{r} \right) \cdot \begin{pmatrix} x \cr y \end{pmatrix}
    = \frac{2}{r} - \frac{1}{r} = \frac{1}{r}.
$$
Substituting back gives
$$
  \lap u = \partial_r^2 u + \frac{1}{r} \partial_r u + \frac{1}{r^2} \partial_\theta^2 u.
$$

## Basic tests to check interference with markdown.

### Nested environments
\begin{equation*}
  I = \begin{pmatrix}
    1 & 0\\
    0 & 1
  \end{pmatrix}
\end{equation*}
### Sub and super scripts.

Here's a superscript without math: a^b, a_b.
Here they are with math:

1. One backslash: \( a^b, a_b \).

1. Two backslashes: \\( a^b, a_b \\).

1. Three backslashes: \\\( a^b, a_b \\\).

### Smileys

`{x}` produces {x} in normal mode.
**In math mode it will mess things up!**
However, smileys need whitespace before and after to be recognized.
So while `$ {x} $` will mess things up, `${x}$` will be OK and produce ${x}$.

### Checking if * and _ mess up math

The code

    $$
    a * b + b * c \qquad
    a_b + b_c, \qquad
    a^{b + c}
    $$

produces
$$
    a * b + b * c \qquad
    a_b + b_c, \qquad
    a^{b + c}
$$

## MathJAX equation reference test
Here is a labeled equation:
\begin{equation}
x+1\over\sqrt{1-x^2}\label{ref1}
\end{equation}
with a reference to ref1: \ref{ref1},
and another numbered one with no label:
$$x+1\over\sqrt{1-x^2}$$
This one uses \nonumber:
\begin{equation}x+1\over\sqrt{1-x^2}\nonumber\end{equation}

Here's one using the equation environment:
\begin{equation}
x+1\over\sqrt{1-x^2}
\end{equation}
and one with equation\* environment:
\begin{equation*}
x+1\over\sqrt{1-x^2}
\end{equation*}

This is a forward reference [\ref{ref2}] and another \eqref{ref2} for the 
following equation:
\begin{equation}x+1\over\sqrt{1-x^2}\label{ref2}\end{equation}
More math:
$$x+1\over\sqrt{1-x^2}$$
Here is a ref inside math: \(\ref{ref2}+1\) and text after it.

\begin{align} 
x& = y_1-y_2+y_3-y_5+y_8-\dots 
&& \text{by \eqref{ref1}}\cr
& = y'\circ y^* && \text{(by \eqref{ref3})}\cr
& = y(0) y' && \text {by Axiom 1.} 
\end{align} 

Here's a bad ref [\ref{ref4}] to a nonexistent label.

An alignment:
\begin{align}
a&=b\label{ref3}\cr
&=c+d
\end{align}
and a starred one:
\begin{align*}
a&=b\cr
&=c+d
\end{align*}

## Custom macro tests

This tests some of my predefined macros.

### Inequalities
$$
  a < b, \quad
  a \leq b \quad
  a \geq b \quad
  a > b.
$$

### Limits

Inline limits: $\dlim_{x \to a} \frac{1}{x}$, $\dlimto{a} \frac{1}{x}$, $\dmax_{0, 1}$.

Displayed `\esssup_{x \in \R}` produces
$$
  \esssup_{x \in \R}
$$

