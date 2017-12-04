title: Adjusting the space between references in the bibliography.
tags: latex
summary: If you use LaTeX and want to adjust the spacing between each item in your bibliography, then here are two ways to do it.

If you use LaTeX and want to adjust the spacing between each item in your bibliography, then download [[{{filesdir}}/bibspacing.sty]] and put the following in your document:
```tex
\usepackage{bibspacing}
\setlength{\bibitemsep}{.2\baselineskip plus .05\baselineskip minus .05\baselineskip}
```

Change the spacing to whatever you desire of course. This works even if you use BibTeX.

## Alternate approach.
**Alternately,** if you don't want to download [[{{filesdir}}/bibspacing.sty]], you can just include it's contents into the **preamble** of your LaTeX source:
{% raw %}
```tex
\newlength{\bibitemsep}\setlength{\bibitemsep}{.2\baselineskip plus .05\baselineskip minus .05\baselineskip}
\newlength{\bibparskip}\setlength{\bibparskip}{0pt}
\let\oldthebibliography\thebibliography
\renewcommand\thebibliography[1]{%
  \oldthebibliography{#1}%
  \setlength{\parskip}{\bibitemsep}%
  \setlength{\itemsep}{\bibparskip}%
}
```
{% endraw %}

This method also works if you use BibTeX.

## References

This was adapted from [here](http://tex.stackexchange.com/questions/93859/condense-the-space-between-bibliographic-entries).
See an alternate approach [here](http://dcwww.camd.dtu.dk/~schiotz/comp/LatexTips/LatexTips.html#bibspace).
