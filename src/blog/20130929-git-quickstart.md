title: A git quickstart guide for LaTeX users
tags: git, latex
summary: [Git](http://git-scm.com/) is a [source control management](http://en.wikipedia.org/wiki/Source_Control_Management)
    system that you can use to track changes in any text file.
    Git, however, is quite complicated and learning it can be quite time consuming.
    This is a quick introduction to git for someone who will primarily use git to edit LaTeX/text documents (not code) and possibly collaborate with a handful of co-authors.

{{summary | join('\n')}}

## A few benefits of using Git

Here are a few benefits you get when using `git`.

### Easily see changes made by co-authors

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

Also, you can [[20140301-git-latexdiff.md|create a compiled PDF]] showing the changes.

### Easily merge changes made by co-authors

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

### Always have full access to old versions

With `git` you have **full access** to older versions at all times.
(This, in some sense, is the point of *version control*).
Some of the things you can do are:

* Restore old versions, or temporarily view them, or compare them.

* Search for when a phrase was first introduced.

* Find out who/when a particular line was changed.

### Compatible with Dropbox/Box/etc.

You don't have to abandon your favorite cloud storage (like Dropbox, Box, Google Drive, etc.) to use `git`.
If you use cloud storage to synchronize files on your computer, you can simply run `git` inside your "cloud folder".
Only caveat: If you run `git` inside your cloud folder, be sure you only use that folder to synchronize between your own personal computers -- don't ever share this folder with a co-author otherwise there will be trouble.

## Core Concepts

### Setup

1. The first thing you should do is [install git](http://git-scm.com/book/en/Getting-Started-Installing-Git).
   If you're not a command line geek, then you might consider installing a GUI.
   I've heard good things about [SourceTree](https://www.sourcetreeapp.com/), but there are many [other choices](https://git-scm.com/downloads/guis).

2. Introduce yourself to git. If your GUI client doesn't let you do this directly, open a terminal and type:

        git config --global user.name 'Your Name'
        git config --global user.email you@math.youruniv.edu

3. In order to share changes with others you will (almost surely) need an SSH key.
   If you don't have one already, instructions on how do this can be found [here](https://help.github.com/articles/generating-ssh-keys).
   If you are using my git server to share changes, you will need to email me your SSH **public** key.
   This is usually a file called `id_rsa.pub` in your SSH directory (`~/.ssh` in Linux).
   <span class='text-warning'>Don't ever share your **private** key (usually a file called `id_rsa` without the `.pub` extension).</span>

### Basic operations and terminology.

#### Cloning a repository.

Every paper is stored in a *git repository*.
The first thing you have to do is to get the *repository URL* and then *clone it*.
For papers on my git server the *repository URL* will look something like `git@wiki.math.cmu.edu:papers/201401-xxx`.
Now you can *clone the repository* by typing following into a terminal.

    git clone git@wiki.math.cmu.edu:papers/201401-xxx myfolder

or using your GUI client. (`myfolder` above is the name of a directory you want to use for this project.)

#### Pulling changes from the server.

To fetch changes that others might have made when you are away you have to *pull* them.
Most GUI clients can do this directly.
On a terminal, <span class='text-warning'>change to your project directory first</span> and type

    git pull

If you have any local changes, don't worry.
A `git pull` will **never** overwrite your changes.
If your locally modified files have also been modified by others, then git will abort with an error message and you need to merge the changes (described [below](#mergeing-changes)) to proceed.


#### Committing and Pushing your changes to the server.

You can edit the files in the project as you please.
When you are done making changes and are ready to share them, you have to *commit* them and then *push* them.
*Committing* tells git to save your current changes into your local git repository (not the server).
Anything committed into git can be easily resurrected at any time, or compared to the current files or anything else committed into git.
Once you have committed your changes, you should *push* them.
This sends your changes to the server for other co-authors to *pull*.

##### Committing your changes

Most GUI's will handle committing.
If you prefer the terminal, use

    git commit -a

to commit *all locally modified files that are currently tracked by git*.
This will open an editor into which you can type a *commit message*.
<span class='text-warning'>TYPE A USEFUL COMMIT MESSAGE.</span>
The first line of your commit message should be short, and is called the *commit subject*.
You can optionally provide a more detailed explanation.
To do this, leave one blank line after your commit subject and then type a longer message explaining your changes.
When you are done, save your changes and close your editor to finish the commit.

Committing is actually a multi-step process:
You're supposed to first *stage files* by using

    git add file.tex ...
    
and then *commit them*  using `git commit`.
The `git commit -a` above stages all locally modified files, and commits them.
You can do this most of the time.
The most common exception is when you create a new file.
In this case you have to first add it using `git add ...` and then commit it.
To see what files have been modified, staged, etc. use `git status`.
(More detailed information is in the documentation [here](https://git-scm.com/docs/git-commit))

##### Pushing your changes

<span class='text-danger'>Committing your changes DOES NOT automatically push them.</span>
For others to see your changes, you have to *push* your changes.
Most GUIs will handle pushing. On a terminal you can do this by typing

    git push

This should work "most of the time". 
Sometimes, git will abort with a message saying *"Non-fast forward updates were rejected"*.
This happens when someone else made a change which you **did not** pull before making your changes.
In this case, you have to pull their changes, [merge them](#merging-changes), and then push your changes.

#### Merging changes

In the normal workflow of a math paper with a handful of co-authors, you probably won't have to perform too many merges.
The most common situation is when someone else makes change while you are in the middle of yours.
In this case a *push* or a *pull* will likely abort with an error message.
Most GUIs should have a good way of dealing with merges.
If you prefer the terminal instead, then do the following:

1. Commit your changes when you are done editing. (But don't push them yet.)

2. Run `git pull --rebase`.
   If this completes without any warning, then any remote changes that were made *did not conflict* with any local changes you made, and you can go on to the next step.
   If there was an error message, then follow the instructions on screen.
   Typically, git will ask you to [resolve a conflict](#resolving-conflicts) in certain files.
   Resolve these conflicts.
   
3. Push your changes back via `git push`

#### Resolving conflicts

Conflicts arise when more than one person edited the same part of the same file.
You might encounter it after doing a pull (via `git pull`, `git pull --rebase`) or a `git merge`.
The status message should tell you what files are conflicted, and what you should do once you have *"fixed the conflicts"*.

You can fix these conflicts by opening these files in your editor, and searching for the conflict markers `<<<<<<<`, `=======`, `>>>>>>>`.
Here's what it will typically look like:
<pre class='codehilite'>
In 1875, Galton and Watson~\cite{WatsonGalton75} took up an investigation into the phenomenon
of ``the decay of the families of men who occupied conspicuous positions in past times.''
<span class='gh'>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD:paper.tex</span>
The problem, posed by Galton, was summarized by the Rev. H. W. Watson as follows.
<span class='gh'>=======</span>
The problem was summarized by the Rev. H. W. Watson as follows.
<span class='gh'>&gt;&gt;&gt;&gt;&gt;&gt;&gt; fe933fa:paper.tex</span>
</pre>

The text between `<<<<<<<` and `=======` is what you wrote, and the text between `=======` and `>>>>>>>` is what your co-authors wrote.
Edit it to your taste, <span class='text-info'>remove the conflict markers</span>.
Your conflict is now fixed. Type `git status` and follow the instructions. (This will typically involving marking your conflicts as fixed using `git add`, and the concluding the merge/rebase using `git rebase --continue` or `git commit`.)

Some GUIs might help you with merging, if you don't like the above.
Alternately, you can also use `git mergetool` to help.


## Tips and tricks

Once you're a more seasoned user of `git` (on the terminal), here are a few tips that might help you.

### Viewing Differences

[[20140301-git-latexdiff.md|This page]] has instructions showing you how to view differences between versions by words, lines or as a complied PDF using [latexdiff](http://www.ctan.org/tex-archive/support/latexdiff).

### Viewing History

`git log` shows history and has many options.
Here's a way to get colorful logs that are a bit easier to read.
Put the following in `~/.gitconfig`:

```
[alias]
    lg = log --format='%w(72,0,8)%C(auto)%h%d %s'
    lga = log --date=short --format='%w(72,0,8)%C(auto)%h %C(green)%cd \
        %<(20,trunc)%aN%C(auto)%d%n%w(72,8,8)%s'
```

Now `git lg` will show you a brief log, and `git lga` will show you a brief log with authors.
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

### Using Git and Dropbox

If you're using git in a Dropbox folder that you never share with anyone else, then you can "just do it" and nothing should go wrong.
If however, you plan to share the folder with co-authors, you should be careful.
Here are [[20160406-dropbox-git.md|instructions]] on how to do this safely.

### Sharing files with non-git aware co-authors.

If you use `git`, but your co-authors don't you can still get many benefits of `git` when merging changes.
This will also avoid fiascos where your co-author edits an older version of the file, and silently overwrites your changes.
The trick to using `git` in this situation is to find the commit the co-author based his changes on, and create a branch for these changes.
`git` provides a way to do this, but requires some work to set up:

1. Edit (or create) `.gitattributes` and add the line

        *.tex text ident

2. Add a line containing `$Id$` to your LaTeX files.
   For instance,

        % DO NOT EDIT -> $Id$ <- DO NOT EDIT

    On checkouts (**not checkins**), `git` will replace this with the SHA1 sum of the blob identifier.

3. Install [git-ident](https://gitlab.com/gi1242/git-ident).

4. Install the post-commit hook from `git-ident`:

        $ cd .git/hooks
        $ ln -s /path/to/git-ident/post-commit

Now edit and commit your changes as you normally would.
When you commit your changes, you'll notice that the `$Id$` token has been replaced with `$Id: 987547... $`.
Share this file with your co-author (say over Dropbox, as described [[20160406-dropbox-git.md|here]]).
When they are done making changes and send it to you, run

    git-find-commit.pl file.tex

(`git-find-commit.pl` is supplied with [git-ident](https://gitlab.com/gi1242/git-ident) that was installed earlier.)
This will output the *commit hash* of the file your co-author based his changes on.
If this is what `HEAD` points to, then he made changes based on your latest version, and you can just save his version over yours and you're good to go.
If not, he made changes based on an earlier version (say `ffffff`).
To merge it use

    $ git checkout -b coauthor-v1 ffffff
    $ # Save his file over yours
    $ git commit --author 'Co Author <who@doesnt.use.git>'
    $ git checkout master
    $ git merge coauthor-v1

This way you keep the whole history in your git repository, and are guaranteed that your co-author hasn't accidentally used an old version and overwritten your changes.

## Further reading

Git, of course, is much more powerful than the simple use case described above.
Here are links to more information:

* [Collaborating with LaTeX and git](https://www.sharelatex.com/blog/2012/10/16/collaborating-with-latex-and-git.html) (from the ShareLaTeX blog).

* [Collaborative Writing of LaTeX Documents](http://en.wikibooks.org/wiki/LaTeX/Collaborative_Writing_of_LaTeX_Documents) (a wiki book describing collaborating with LaTeX in general, and not just with git).

* [The Pro-Git book](http://git-scm.com/book) (a comprehensive introduction to git).
