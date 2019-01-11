title: Getting DOI / arXiv links with BibTeX.
tags: bibtex
summary: Many bibliography databases supply a [DOI](http://www.doi.org/) (Digital Object Identifier) or [arXiv](https://arxiv.org/) eprint number with [BibTeX](http://www.bibtex.org/) entries. However, the standard BiBTeX style files either ignore this information or print it without hyperlinking it correctly. Here's how you can get working clickable links to both DOI and arXiv eprints.

{{summary}}

## Using my style file.

If you use `abbrv` or `alpha` as your bibliography style, then the simplest way would be for you to download my version of these style files: [[{{filesdir}}/habbrv.bst]] or [[{{filesdir}}/halpha.bst]].
(Alternately if you want abbreviated author names, and alphabetic labels you can use [[{{filesdir}}/halpha-abbrv.bst]].)
Save the appropriate file in the same directory as your `tex` file and use it by putting the following in your `tex` file:

```tex
\bibliographystyle{habbrv}
\bibliography{refs}
```

Replace `habbrv` with `halpha` or `halpha-abbrv` as appropriate.
To make the links clickable, you need to use the `hyperref` package.
Also, since some DOIs might contain evil special characters, I strongly recommend you use the `doi` package by adding the following to your preamble.

```tex
\RequirePackage{doi}
\usepackage{hyperref}
```

That's it.
Your arXiv and DOI should appear as clickable links in your PDF.
Also, if you want to add a custom URL to any of your bibliographic entries, just use the `url` field.

Here is an example bibliographic entry:
``` bib
@Article{     foo,
  author        = {Author, A},
  title         = {Example entry},
  journal       = {ArXiv e-prints},
  archiveprefix = {arXiv},
  eprint        = {1707.03780},
  primaryclass  = {physics.flu-dyn},
  doi           = {10.1010/doi-that-will-become-a-hyperlink},
  url           = {http://your.custom.url},
  year          = 2017,
}
```

**Note:** Some databases add a `url` field with the DOI link, and also a `doi` field.
To avoid duplication, the `url` field will only be displayed if the `doi` field is not present.

## Sanitizing bibliographic entries with bibtool (optional)

If you want to sanitize your bibliography and convert `url` fields with a `doi` into a `doi` field, then you can use [[20140304-bibtool.md|bibtool]] to fix it.
Put the following in your `~/.bibtoolrc`:

    rename.field {url=doiurl if url="doi"}
    rename.field {doiurl=delete if doi="10."}
    delete.field = {delete}
    rename.field {doiurl=doi}
    rewrite.rule = {doi# "https?://.*doi\.org/\(10\.[0-9]+/.+\)"# "\1"}

and filter your entry through `bibtool`.

## Hacking your own style file.

If you use a different bibliography style, you will have to edit the style file.
I created [[{{filesdir}}/habbrv.bst]] and [[{{filesdir}}/halpha.bst]] and by taking the arXiv's version of these files (available [here](https://arxiv.org/hypertex/bibstyles/habbrv.bst) and [here](https://arxiv.org/hypertex/bibstyles/halpha.bst)) and making the following changes

{% raw -%}
```
diff --git a/habbrv.bst b/habbrv.bst
index 8d4d324..dacaaff 100644
--- a/habbrv.bst
+++ b/habbrv.bst
@@ -1,3 +1,5 @@
+% 2017-11-13 Gautam Iyer: Modified to include DOI links.
+%
 % habbrv: adds eprint field (www-admin@xxx.lanl.gov)
 % an extension of:
 % BibTeX standard bibliography style `abbrv'
@@ -32,6 +34,8 @@ ENTRY
     series
     title
     type
+    url
+    doi
     volume
     year
   }
@@ -243,10 +247,27 @@ FUNCTION {format.title}
 FUNCTION {format.eprint}
 { eprint empty$
     { "" }
-    { eprint }
+    { "\burlalt{" eprint * "}{http://arxiv.org/abs/" * eprint * "}" * }
   if$
 }
 
+FUNCTION {format.url}
+{   doi empty$ not
+    url empty$
+  or
+    { "" }
+    { "\urlprefix\url{" url * "}" * }
+  if$
+}
+
+FUNCTION {format.doi}
+{ doi empty$
+    { "" }
+    { "\doi{" doi * "}" * }
+  if$
+}
+
+
 FUNCTION {n.dashify}
 { 't :=
   ""
@@ -562,6 +583,10 @@ FUNCTION {article}
   if$
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -595,6 +620,10 @@ FUNCTION {book}
   format.date "year" output.check
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -610,6 +639,10 @@ FUNCTION {booklet}
   format.date output
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -645,6 +678,10 @@ FUNCTION {inbook}
   format.date "year" output.check
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -672,6 +709,10 @@ FUNCTION {incollection}
   if$
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -707,6 +748,10 @@ FUNCTION {inproceedings}
   if$
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -744,6 +789,10 @@ FUNCTION {manual}
   format.date output
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -760,6 +809,10 @@ FUNCTION {mastersthesis}
   format.date "year" output.check
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -774,6 +827,10 @@ FUNCTION {misc}
   format.date output
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
   empty.misc.check
@@ -791,6 +848,10 @@ FUNCTION {phdthesis}
   format.date "year" output.check
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -827,6 +888,10 @@ FUNCTION {proceedings}
   if$
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -843,6 +908,10 @@ FUNCTION {techreport}
   format.date "year" output.check
   format.eprint output
   new.block
+  format.doi output
+  new.block
+  format.url output
+  new.block
   note output
   fin.entry
 }
@@ -856,6 +925,10 @@ FUNCTION {unpublished}
   note "note" output.check
   format.date output
   format.eprint output
+  new.block
+  format.url output
+  new.block
+  format.doi output
   fin.entry
 }
 
@@ -1104,6 +1177,24 @@ FUNCTION {begin.bib}
     { preamble$ write$ newline$ }
   if$
   "\begin{thebibliography}{"  longest.label  * "}" * write$ newline$
+  "\expandafter\ifx\csname url\endcsname\relax"
+  write$ newline$
+  "  \def\url#1{\texttt{#1}}\fi"
+  write$ newline$
+  "\expandafter\ifx\csname doi\endcsname\relax"
+  write$ newline$
+  "  \def\doi#1{\burlalt{doi:#1}{http://dx.doi.org/#1}}\fi"
+  write$ newline$
+  "\expandafter\ifx\csname urlprefix\endcsname\relax\def\urlprefix{URL }\fi"
+  write$ newline$
+  "\expandafter\ifx\csname href\endcsname\relax"
+  write$ newline$
+  "  \def\href#1#2{#2}\fi"
+  write$ newline$
+  "\expandafter\ifx\csname burlalt\endcsname\relax"
+  write$ newline$
+  "  \def\burlalt#1#2{\href{#2}{#1}}\fi"
+  write$ newline$
 }
 
 EXECUTE {begin.bib}
```
{% endraw %}

You will have to do something similar to your style file.
(If you need a reference for the syntax of style files, bibtex uses some weird stacking syntax.
This is described in `btxhak.pdf`, and you should be able to view it using `texdoc btxhak` or on [CTAN](http://mirrors.ctan.org/biblio/bibtex/contrib/doc/btxhak.pdf).
