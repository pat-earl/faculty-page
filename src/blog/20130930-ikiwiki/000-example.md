title: Example of Math Rendering
breadcrumb: /{{dirname}}.md

Here's an example of the math rendering:

> **Theorem** *(Mean Value Property).*
> Let $\Omega \subset \R^3$ be a domain, and $u$ is harmonic in $\Omega$ (i.e. $\lap u = 0$ in $\Omega$).
> Suppose $B$ is a ball of radius $R$ and center $x_0$ that is completely contained in $\Omega$.
> Then
> $$
>   u(x_0) = \frac{1}{4 \pi R^2} \int_{\partial B} u \, dS
> $$

This was produced by the following code:

```text
**Theorem** *(Mean Value Property).*
Let $\Omega \subset \R^3$ be a domain, and $u$ is harmonic in $\Omega$ (i.e. $\lap u = 0$ in $\Omega$).
Suppose $B$ is a ball of radius $R$ and center $x_0$ that is completely contained in $\Omega$.
Then
$$
  u(x_0) = \frac{1}{4 \pi R^2} \int_{\partial B} u \, dS
$$
```
