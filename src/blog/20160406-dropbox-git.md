title: Using git and Dropbox
tags: linux, git
summary: [Dropbox](https://www.dropbox.com/) isn't version control.
    If you use [git](https://git-scm.com/) to version control your files, and
    have co-authors that use `Dropbox` then here is a way to use the two
    systems together.

{{summary | join('\n')}}

## Make your shared Dropbox folder have a separate repository

I'd like my shared [Dropbox] folder to be a full fledged git repository, and
version control all relevant files there via [git]. However, git repositories
usually contain a special `.git/` folder in the root. Storing this special
`.git/` folder in a **shared dropbox folder** is a recipe for disaster. A
non-git aware collaborator will certainly wreak havoc on it. Further, doing
most git operations (even if they are simply checking the status) will push
notifications to all your collaborator saying that a few git files have
changed.

This can be annoying (and disastrous). A better alternative is to set up your
shared Dropbox folder to be a git repository, but store the git repository (the
`.git/` folder) in a separate (non-dropbox) directory.

    :::console
    $ cd ~/Dropbox/shared/foo
    $ dropbox exclude add .git
    Excluded:
    .git
    $ mkdir -p $HOME/.separate-gitroots
    $ git init --separate-git-dir=$HOME/.separate-gitroots/foo.git
    Initialized empty Git repository in /home/gautam/.separate-gitroots/foo.git

This creates the git repository in `$HOME/.separate-gitroots/foo.git` instead
of in `./.git/` as is customary. Now `./.git` will be a plain text file (not
folder) that contains the location of the `foo.git` directory above.

Obviously `./.git` will be truly useless to anyone else sharing your Dropbox
folders,  so I recommend excluding it from the list of synchronized files. The
`dropbox exclude` command above does this using Dropbox's
[Selective sync](https://www.dropbox.com/en/help/4456) feature.

## Working on a local copy.

I set up a local copy, away from Dropbox, to work on. This way a collaborator
who makes changes while I'm working will not overwrite mine, and I can tell
the two changes apart easily. I also use a centralized remote (so I can share
it with git-aware co-authors), but you can do without it (if you know what
you're doing.)

### Setting up the repositories

Let's assume you have a git server and created an empty repository on it at `git@yourserver.com:foo`.
We first add this remote into Dropbox, and put your shared files in it:

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git remote add origin git@yourserver.com:foo
    $ git add paper.tex ... # (or use git add -Av .)
    $ git commit --author 'Coauthor <who@doesnt.use.git>'
    [master a484503] Blah blah (commit subject)
     1 file changed, 10 insertions(++++++)
    $ git push -u origin master
    Branch master set up to track remote branch master from origin.
    Counting objects: 5, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 6.80 KiB | 0 bytes/s, done.
    Total 5 (delta 3), reused 0 (delta 0)
    To yourserver.com/foo
       9996b2d..f9d5e30  master -> master    

Now set up a local copy by cloning this repository into `~/foo`. Type:

    :::console
    $ git clone git@yourserver.com:foo ~/foo
    Cloning into 'foo'...
    remote: Counting objects: 545, done.
    remote: Compressing objects: 100% (542/542), done.
    remote: Total 545 (delta 341), reused 0 (delta 0)
    Receiving objects: 100% (545/545), 691.49 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (341/341), done.

or use your favorite GUI client.
You should now have your work in the remote repository `git@yourserver.com`, one clone in Dropbox (for your coauthors to edit) and one local clone in `~/foo` for you to edit.
(Of course, if you had local files you were already working on in `~/foo`, you could have done the `git remote add` in `~/foo`, committed, pushed and then pulled in Dropbox instead.)


### Committing changes

When a collaborator make changes in Dropbox, you have to commit and push it
for them, and pull it into your local copy.

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git commit -a --author 'Coauthor <who@doesnt.use.git>'
    [master a484503] Blah blah (commit subject)
     1 file changed, 10 insertions(++++++)
    $ git push
    Counting objects: 5, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 6.80 KiB | 0 bytes/s, done.
    Total 5 (delta 3), reused 0 (delta 0)
    To yourserver.com/foo
       9996b2d..f9d5e30  master -> master    
    $ cd ~/foo
    $ git pull
    Updating 9996b2d..f9d5e30
    Fast-forward
     paper.tex        |  141 +++---
     refs.bib         |    5 +-
     3 files changed, 140 insertions(+), 6 deletions(-)

After the first commit as your co-author, you can just use `--author Coauthor`
without typing the whole email address every time. Also, if you have only one
co-author who will commit in Dropbox, then you can use `git config` to set
`user.name` and `user.email` in the Dropbox repository, and not use `--author`
above.

When you make changes:

    :::console
    $ cd ~/foo
    $ git commit -a && git push
    [master a484503] Blah blah (commit subject)
     1 file changed, 10 insertions(++++++)
    Counting objects: 5, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 6.80 KiB | 0 bytes/s, done.
    Total 5 (delta 3), reused 0 (delta 0)
    To yourserver.com/foo
       9996b2d..f9d5e30  master -> master    
    $ cd ~/Dropbox/shared/foo
    $ git pull
    Updating 9996b2d..f9d5e30
    Fast-forward
     paper.tex        |  141 +++---
     refs.bib         |    5 +-
     3 files changed, 140 insertions(+), 6 deletions(-)

### When you and your co-author simultaneously made changes

No problem. Git handles it painlessly. (I'm omitting the console output of git below for brevity.)

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git commit -a --author Coauthor && git push
    $ cd ~/foo
    $ git commit -a
    $ git pull --rebase

The last command may warn you about conflicts (if you and your co-author
edited similar portions of the same file). Follow the instructions displayed
by git. Once you're done, push your changes and pull them into Dropbox as
shown in the previous section.

## Creating branches for a co-author

Often when when I'm editing my local copy my collaborator makes changes in
Dropbox simultaneously. For simple changes you can merge them quickly as
above. If there have been more elaborate changes, I usually create a branch
and merge it as follows.

1. Commit and push your collaborators changes to a new branch

        :::console
        $ cd ~/Dropbox/shared/foo
        $ git checkout -b coauthor-b1
        $ git commit --author Coauthor -a
        $ git push --all

2. Merge your co-authors changes in your local copy. (Or rebase it, if you
   know what you are doing.)

        :::console
        $ cd ~/foo
        $ git commit -a
        $ git fetch origin coauthor-b1
        $ git merge coauthor-b1
        $ git push

3. Pull them in the shared Dropbox folder.

        :::console
        $ cd ~/Dropbox/shared/foo
        $ git checkout master
        $ git pull


[Dropbox]: https://www.dropbox.com/

[git]: https://git-scm.com/
