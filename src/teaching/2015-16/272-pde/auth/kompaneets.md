title: Project: Numerical study of Bose-Einstein Condensation
{%- from get_file('../course_info.j2') import course %}
breadcrumb: ../index.html|{{course.title}}

In low density (or high energy) plasmas energy transport is modelled by the *Kompaneets* equation:
\begin{gather*}
  \partial_t n + \partial_x F = 0,\\
  F = F(x, n) = (2x - x^2)n - n^2 - x^2 \partial_x n
\end{gather*}
Note $n$ is a function of $x$, so $\partial_x F = \partial_1 F + \partial_2 F \partial_x n$.
Here $x > 0$ is proportional to the magnitude of the wave vector (and hence the energy) of a photon, and $n(x, t)$ represents the number density of photons with energy $x$.

Under the assumption $F \to 0$ as $x \to 0$ and $x \to \infty$, it is easy to see that the total photon number
\begin{equation*}
  N(t) \defeq \int_0^\infty n(x, t) \, dx
\end{equation*}
is constant as a function of time.
However, all nonnegative equilibrium solutions are given by
\begin{equation*}
  n_\mu(x) = \frac{x^2}{e^{x + \mu} - 1},
\end{equation*}
and hence the maximum photon number in equilibrium is
\begin{equation*}
  N_\text{max}
    \defeq \sup_{\mu \geq 0} \int_0^\infty n_\mu \, dx 
    = \int_0^\infty \frac{x^2}{e^{x+\mu} - 1} \, dx
    < \infty.
\end{equation*}

Thus if we start with initial data that has a photon number higher than $N_\text{max}$, the photon number can not be conserved.
It is believed that there is an "outflux" of photons at $0$, which form a Bose-Einstein condensate.
Our aim is to study this numerically.

## Step 1: A naive numerical scheme

Write down a simple minded finite difference scheme for this equation, and implement it.
It is well known that this scheme **IS NOT** effective in studying the formation of the condensate.
Our first aim is to see numerically the failure of the simple minded approach and understand where exactly things break.
