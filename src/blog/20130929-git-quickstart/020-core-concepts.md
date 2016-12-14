title: Core Concepts
breadcrumb: /{{dirname}}.md

## Setup

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

## Basic operations and terminology.

### Cloning a repository.

Every paper is stored in a *git repository*.
The first thing you have to do is to get the *repository URL* and then *clone it*.
For papers on my git server the *repository URL* will look something like `git@wiki.math.cmu.edu:papers/201401-xxx`.
Now you can *clone the repository* by typing following into a terminal.

    git clone git@wiki.math.cmu.edu:papers/201401-xxx myfolder

or using your GUI client. (`myfolder` above is the name of a directory you want to use for this project.)

### Pulling changes from the server.

To fetch changes that others might have made when you are away you have to *pull* them.
Most GUI clients can do this directly.
On a terminal, <span class='text-warning'>change to your project directory first</span> and type

    git pull

If you have any local changes, don't worry.
A `git pull` will **never** overwrite your changes.
If your locally modified files have also been modified by others, then git will abort with an error message and you need to merge the changes (described [below](#mergeing-changes)) to proceed.


### Committing and Pushing your changes to the server.

You can edit the files in the project as you please.
When you are done making changes and are ready to share them, you have to *commit* them and then *push* them.
*Committing* tells git to save your current changes into your local git repository (not the server).
Anything committed into git can be easily resurrected at any time, or compared to the current files or anything else committed into git.
Once you have committed your changes, you should *push* them.
This sends your changes to the server for other co-authors to *pull*.

#### Committing your changes

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

#### Pushing your changes

<span class='text-danger'>Committing your changes DOES NOT automatically push them.</span>
For others to see your changes, you have to *push* your changes.
Most GUIs will handle pushing. On a terminal you can do this by typing

    git push

This should work "most of the time". 
Sometimes, git will abort with a message saying *"Non-fast forward updates were rejected"*.
This happens when someone else made a change which you **did not** pull before making your changes.
In this case, you have to pull their changes, [merge them](#merging-changes), and then push your changes.

### Merging changes

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

### Resolving conflicts

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

## Further reading

Git, of course, is much more powerful than the simple use case described above.
Here are links to more information:

* [[030-tips-n-tricks.md]].

* [[../20130929-git-quickstart.md]].

* [Collaborating with LaTeX and git](https://www.sharelatex.com/blog/2012/10/16/collaborating-with-latex-and-git.html) (from the ShareLaTeX blog).

* [Collaborative Writing of LaTeX Documents wiki book](http://en.wikibooks.org/wiki/LaTeX/Collaborative_Writing_of_LaTeX_Documents) (a wiki book describing collaborating with LaTeX in general, and not just with git).

* [The Pro-Git book](http://git-scm.com/book) (a comprehensive introduction to git).
