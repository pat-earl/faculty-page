title: Markdown escaping tests

## Test rendering of `a _b c_ d` 

* Normal text: a _b c_ d

* With `$`: $a _b c_d$.

* With `$$`: $$a _b c_d$$

* With `\begin{equation}`: \begin{equation}a _b c_d\end{equation}

* With `\begin{equation*}`:
  \begin{equation*}
    a _b c_ d
  \end{equation*}

## Code blocks

* `$x^y$`

## Test escaping of dollar symbol

* Inline code <code>\`\$...\$\`</code> renders as `$...$`

* Escaped dollars `\$text\$` render as \$text\$

* Un-escaped dollars `$math$` render as $math$

* Single dollar escaped `\$5.00` renders as \$5.00.

* Single dollar not escaped `$5.00` renders as $5.00.

* this shouldn't be math.$
