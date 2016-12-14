title: A few benefits of using Git
breadcrumb: /{{dirname}}.md

Here are a few benefits you get when using `git`.

## You can easily see changes made by co-authors

You can display word by word changes made in a form that looks like this:

<pre>
<span style="color:teal;">@@ -3045,12 +3045,15 @@</span> \section{Proof of Proposition~\ref{ppnCLTFirstHitShort}}
We finally define the function $g$ <span style="color:red;">that appears</span><span style="color:green;">appearing</span> in Property (6)<span style="color:red;">.
For</span><span style="color:green;">for</span> $x = (q,\xi) \in \CM$, <span style="color:red;">let</span><span style="color:green;">by setting</span> $g((q,\xi)) = \xi \in \mathbb{Z}^2$.
</pre>

Or inspect changes line by line:
```
diff --git a/refs.bib b/refs.bib
index 349c0c3..65b8321 100644
--- a/refs.bib
+++ b/refs.bib
@@ -5556,7 +5585,7 @@
   pages                = {2636--2647}
 }

-@Book{           Rozovski90,
+@Book{           Rozovskii90,
   author       = {Rozovski{\u\i}, B. L.},
   title        = {Stochastic evolution systems},
   series       = {Mathematics and its Applications (Soviet Series)},
```

Also, you can [[../20140301-git-latexdiff.md|create a compiled PDF]] showing the changes.

## You can easily merge changes made by co-authors

If you and a co-author are working on a file at the same time, git will **NEVER** allow you to accidentally overwrite each others changes because you "edited the wrong version".
In this case when you push your changes, `git` will inform you of a conflict.
Often, if you and your co-authors edited different files, or even different parts of the same file, `git` can automatically merge your changes for you.
If you and your co-author edited the same part of a file, `git` will inform you, and leave *conflict markers* in the file showing the differences.
These look something like this:

<pre class='codehilite'>
In 1875, Galton and Watson~\cite{WatsonGalton75} took up an investigation into the phenomenon
of ``the decay of the families of men who occupied conspicuous positions in past times.''
<span class='gh'>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD:paper.tex</span>
The problem, posed by Galton, was summarized by the Rev. H. W. Watson as follows.
<span class='gh'>=======</span>
The problem was summarized by the Rev. H. W. Watson as follows.
<span class='gh'>&gt;&gt;&gt;&gt;&gt;&gt;&gt; fe933fa:paper.tex</span>
</pre>

Now you can edit the file, and tell `git` when you have "resolved all conflicts".

## You can still use Dropbox/Box/etc.

You don't have to abandon your favorite cloud storage (like Dropbox, Box, Google Drive, etc.) to use `git`.
If you use cloud storage to synchronize files on your computer, you can simply run `git` inside your "cloud folder".
Only caveat: If you run `git` inside your cloud folder, be sure you only use that folder to synchronize between your own personal computers -- don't ever share this folder with a co-author otherwise there will be trouble.
