title: Using custom labels with the `alpha` BibTeX style
summary: The `alpha` BibTeX style produces citation labels of the form `[Ken90]` or `[XYZ94]`. While it usually does the right thing, sometimes it doesn't get the label right (e.g. the label is too long when the authors have multiple / hyphenated last names). Here is how you can provide a custom label with the `alpha` style.

{{summary}}

The simplest method would be to download my [[20171114-bibtex-doi/halpha-abbrv.bst|style file]].
(This also hyperlinks DOI/URLs correctly as described [[20171114-bibtex-doi.md|here]].)
Save the file in the same directory as your `tex` file and use it by putting the following in your `tex` file:

```tex
\bibliographystyle{halpha-abbrv}
\bibliography{refs}
```

Now if you want to cite your entries with a custom label (e.g. `A17` instead of the default `Aut17`), then provide the label you want in the `label` field.
For example:
``` bib
@Article{     foo,
  label         = {A17},
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
This entry will be cited as `[A17]`.

If you are using a different style file, and need to get a similar effect, then you will have to edit the `calc.label` function of your style file.
Here are the changes I made:

``` diff
diff --git a/halpha-abbrv.bst b/halpha-abbrv.bst
index a960aa9..4408167 100644
--- a/halpha-abbrv.bst
+++ b/halpha-abbrv.bst
@@ -17,6 +17,7 @@ ENTRY
   { address
     author
     booktitle
+    label
     chapter
     edition
     editor
@@ -41,7 +42,7 @@ ENTRY
     year
   }
   {}
-  { label extra.label sort.label }
+  { cite.label extra.label sort.label }
 
 INTEGERS { output.state before.all mid.sentence after.sentence after.block }
 
@@ -93,7 +94,7 @@ FUNCTION {output.check}
 FUNCTION {output.bibitem}
 { newline$
   "\bibitem[" write$
-  label write$
+  cite.label write$
   "]{" write$
   cite$ write$
   "}" write$
@@ -1125,24 +1126,28 @@ FUNCTION {editor.key.organization.label}
 }
 
 FUNCTION {calc.label}
-{ type$ "book" =
-  type$ "inbook" =
-  or
-    'author.editor.key.label
-    { type$ "proceedings" =
-	'editor.key.organization.label
-	{ type$ "manual" =
-	    'author.key.organization.label
-	    'author.key.label
-	  if$
-	}
+{ label empty$
+    { type$ "book" =
+      type$ "inbook" =
+      or
+        'author.editor.key.label
+        { type$ "proceedings" =
+            'editor.key.organization.label
+            { type$ "manual" =
+                'author.key.organization.label
+                'author.key.label
+              if$
+            }
+          if$
+        }
       if$
+      duplicate$
+      year field.or.null purify$ #-1 #2 substring$
+      *
     }
+    { label duplicate$ }
   if$
-  duplicate$
-  year field.or.null purify$ #-1 #2 substring$
-  *
-  'label :=
+  'cite.label :=
   year field.or.null purify$ #-1 #4 substring$
   *
   sortify 'sort.label :=
@@ -1311,10 +1316,10 @@ FUNCTION {reverse.pass}
     { "a" 'extra.label := }
     'skip$
   if$
-  label extra.label * 'label :=
-  label width$ longest.label.width >
-    { label 'longest.label :=
-      label width$ 'longest.label.width :=
+  cite.label extra.label * 'cite.label :=
+  cite.label width$ longest.label.width >
+    { cite.label 'longest.label :=
+      cite.label width$ 'longest.label.width :=
     }
     'skip$
   if$
```

You will have to do something similar to your style file.

**Note:** There is a minor bug with sorting when you provide a custom citation label.
Custom labels are sorted according to the whole label and the four digit year.
The other labels are sorted according to the author initials and the four digit year.
So if your custom label includes a year already, there could theoretically be a small change in the sort order.
