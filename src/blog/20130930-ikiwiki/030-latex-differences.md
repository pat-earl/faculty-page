title: Differences from LaTeX when typing Math
breadcrumb: /{{dirname}}.md

{% raw %}
There are a few things to watch for which are different in the ikiWiki/MathJAX setup than traditional LaTeX.
I list a couple that have tripped me up here.

* Underscores near braces cause trouble:
  `${{a}_{1}}^{{b}_{1}}$` renders incorrectly.

    Fix: Add spaces, or remove braces.
  E.g. write `${{a} _{1}}^{{b} _{1}}$` instead which renders correctly as ${{a} _{1}}^{{b} _{1}}$.

* Some smileys might cause problems:
  `$ {x} $` renders incorrectly as $ {x} $.
  (On the other hand `${x}$` renders correctly as ${x}$.)

* In the `align` or `gather` environments linebreaks via `\\` won't work.  

    Instead try `\\\\` or `\cr` instead.
  For example:
  \begin{align*}
    a &= b + 1 \cr
    b + c &= d \\\\
    e + 1 &= f + g.
  \end{align*}

* Quotes: Open quotes in LaTeX must be escaped, otherwise they're treated as CODE blocks.

Some miscellaneous rendering tests can be found [[files/tests.md|here]].
{% endraw %}
