title: Git tips and tricks
breadcrumb: /{{dirname}}.md

## Viewing Differences

[[../20140301-git-latexdiff.md|This page]] has instructions showing you how to view differences between versions by words, lines or as a complied PDF using [latexdiff](http://www.ctan.org/tex-archive/support/latexdiff).

## Viewing history

`git log` shows history and has many options.
Here's a way to get colorful logs that are a bit easier to read.

```dosini
[alias]
    lg = log --format='%w(72,0,8)%C(auto)%h%d %s'
    lga = log --date=short --format='%w(72,0,8)%C(auto)%h %C(green)%cd \
        %<(20,trunc)%aN%C(auto)%d%n%w(72,8,8)%s'
```

The outputs look like this:

<pre>
<b>&gt;</b> git lg -5
<span style="color:olive;">0caf6bf</span><span style="color:olive;"> (</span><span style="color:teal;font-weight:bold;">HEAD -&gt; </span><span style="color:green;font-weight:bold;">master</span><span style="color:olive;">)</span> Avoid md.reset() when processing links
<span style="color:olive;">50bbc70</span><span style="color:olive;"> (</span><span style="color:red;font-weight:bold;">origin/master</span><span style="color:olive;">, </span><span style="color:red;font-weight:bold;">origin/HEAD</span><span style="color:olive;">)</span> Used localhost for smtp.
<span style="color:olive;">95826b7</span> Fluids WG
<span style="color:olive;">b47d349</span> Delete unused files in output
<span style="color:olive;">b4a8b5d</span> Added stochastic nucleation paper with Dan

<b>&gt;</b> git lga -5
<span style="color:olive;">0caf6bf</span> <span style="color:green;">2016-12-11  Gautam Iyer         </span><span style="color:olive;"> (</span><span style="color:teal;font-weight:bold;">HEAD -&gt; </span><span style="color:green;font-weight:bold;">master</span><span style="color:olive;">)</span>
        Avoid md.reset() when processing links
<span style="color:olive;">50bbc70</span> <span style="color:green;">2016-11-12  Gautam Iyer         </span><span style="color:olive;"> (</span><span style="color:red;font-weight:bold;">origin/master</span><span style="color:olive;">, </span><span style="color:red;font-weight:bold;">origin/HEAD</span><span style="color:olive;">)</span>
        Used localhost for smtp.
<span style="color:olive;">95826b7</span> <span style="color:green;">2016-11-11  Gautam Iyer         </span>
        Fluids WG
<span style="color:olive;">b47d349</span> <span style="color:green;">2016-11-11  Gautam Iyer         </span>
        Delete unused files in output
<span style="color:olive;">b4a8b5d</span> <span style="color:green;">2016-10-25  Gautam Iyer         </span>
        Added stochastic nucleation paper with Dan
</pre>

## Using Git and Dropbox

If you're using git in a Dropbox folder that you never share with anyone else, then you can "just do it" and nothing should go wrong.
If however, you plan to share the folder with co-authors, you should be careful.
Here are [[20160406-dropbox-git.md|instructions]] on how to do this safely.
