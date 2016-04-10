title: Using git and Dropbox
tags: linux, git
summary: [Dropbox](https://www.dropbox.com/) isn't version control.
    Unfortunately, many people will never understand this and will never truly
    appreciate the benefits of a true version control system
    like [git](https://git-scm.com/). I primarily write mathematical papers
    using [LaTeX](https://latex-project.org/intro.html), and if like me, your
    collaborators insist on using `Dropbox` and are unwilling to investigate
    `git`, then you can still use `git` in the `Dropbox` folder. Here are
    setup instructions.

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

This can be annoying (and disastrous). You can alternately set up your shared
Dropbox folder to be a git repository, but store the git repository (the
`.git/` folder) in a separate (non-dropbox) directory.

    $ cd ~/Dropbox/shared/foo
    $ dropbox exclude add .git
    $ mkdir -p $HOME/.separate-gitroots/shared.git
    $ git init --separate-git-dir=$HOME/.separate-gitroots/shared.git

This creates the git repository in `$HOME/foo/.dropbox.git` instead of in
`./.git/` as is customary. Now `./.git` will be a plain text file (not folder)
that contains the location of the true git repository.

Obviously `./.git` will be truly useless to anyone else sharing your Dropbox
folders,  so I recommend excluding it from the list of synchronized files. The
`dropbox exclude` command above does this using Dropbox's
[Selective sync](https://www.dropbox.com/en/help/4456) feature.

## Working directly in the Dropbox folder.

If you plan to work directly in Dropbox, then you're ready to go. When you
make a change, you can just `git commit` it as usual. The first time your
collaborator makes a change, you can commit it using:

    git commit --author 'An Idiot <who@doesnt.use.git>'

For subsequent changes, you can use `--author Idiot` (or any part of his
name/email that identifies it uniquely).

The disadvantage of working directly in Dropbox is that your collaborator can
make changes at the same time as you. If he/she makes a change when you have
an uncommitted change, there is no way to tell which changes were made by you,
and which were made by your collaborator. For these reasons, I usually set up
a [local copy](#creating-a-local-copy) for anything important.

## Creating a local copy.

I prefer to work on a local copy, away from Dropbox. This way a collaborator
who makes changes while I'm working will not overwrite mine, and I can tell
the two changes apart easily.

There are two options:

1. Use a centralized remote to pull/push from. This involves double the work
   per commit; if you need a centralized server for other purposes (e.g.
   backups, sharing with others etc.) then you have to use this method.

2. Directly pulling/pushing between your local copy and the shared Dropbox
   folder. This is less work per commit, but if you don't have remote backups
   then bye bye git history.

### Using a centralized remote

#### Setting up the repositories

To use a centralized remote, first create a git repository on your git server.
If you don't have a git server and want to create a local one on your machine,
use

    $ mkdir -p ~/.gitroots
    $ git init --bare ~/.gitroots/foo.git

Assuming your git remote is `~/.gitroots/foo.git`, add it to your shared
Dropbox folder by:

    $ cd ~/Dropbox/shared/foo
    $ git remote add origin ~/.gitroots/foo.git

Now setup a local clone:

    $ git clone ~/.gitroots/foo.git ~/foo

Of if you already have some work in `~/foo`, you can

    $ git remote add origin ~/.gitroots/foo.git

#### Committing changes

When a collaborator make changes in Dropbox, you commit and push it for them,
and pull it into your local copy.

    $ cd ~/Dropbox/shared/foo
    $ git commit --author 'Idiot' && git push
    $ cd ~/foo
    $ git pull

If you have only one co-author who will commit in Dropbox, then you can use
`git config` to set `user.name` and `user.email` in the Dropbox repository,
and not use `--author` above.

When you make changes:

    $ cd ~/foo
    $ git commit && git push
    $ cd ~/Dropbox/shared/foo
    $ git pull

### Directly pulling/pushing to the shared folder

This is a little less work. You can't ever push changes; but can only pull
them. Also if you use this method, I hope you have your git repository backed
up in case of hard disk crashes.

#### Setting up the repositories

    $ cd ~/Dropbox/foo
    $ git remote add origin ~/foo

    $ cd ~/foo
    $ git init
    $ git remote add origin ~/Dropbox/foo

#### Committing changes

Follow the same instructions as with using a
[centralized remote](#committing-changes),
but omit all the `git push` commands.


## Creating branches for a co-author

Often when when I'm editing my local copy my collaborator makes changes in
Dropbox simultaneously. If you're a Git Guru, you can merge these changes
however you normally do. I usually create a branch using the following:

1. Commit and push your collaborators changes to a new branch

        $ cd ~/Dropbox/shared/foo
        $ git co -b idiot-b1
        $ git commit --author Idiot -a
        $ git push --all

2. Merge your co-authors changes in your local copy.

        $ cd ~/foo
        $ git commit -a
        $ git fetch origin idiot-b1
        $ git merge idiot-b1
        $ git push

3. Pull them in the shared Dropbox folder.

        $ cd ~/Dropbox/shared/foo
        $ git co master
        $ git pull


[Dropbox]: https://www.dropbox.com/

[git]: https://git-scm.com/
