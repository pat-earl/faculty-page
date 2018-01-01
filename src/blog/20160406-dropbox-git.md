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
    $ mkdir -p $HOME/.separate-gitroots
    $ git init --separate-git-dir=$HOME/.separate-gitroots/foo.git

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

If you have a remote git repository located at `git@yourserver.com:foo`, then
to set up a local copy, first clone your repository into `~/foo`. Type:

    :::console
    $ git clone git@yourserver.com:foo ~/foo

or use your favorite GUI client.
Now add your git remote into Dropbox:

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git remote add origin git@yourserver.com:foo

### Committing changes

When a collaborator make changes in Dropbox, you have to commit and push it
for them, and pull it into your local copy.

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git commit --author 'Coauthor <who@doesnt.use.git>' && git push
    $ cd ~/foo
    $ git pull

After the first commit as your co-author, you can just use `--author Coauthor`
without typing the whole email address every time. Also, if you have only one
co-author who will commit in Dropbox, then you can use `git config` to set
`user.name` and `user.email` in the Dropbox repository, and not use `--author`
above.

When you make changes:

    :::console
    $ cd ~/foo
    $ git commit && git push
    $ cd ~/Dropbox/shared/foo
    $ git pull

### When you and your co-author simultaneously made changes

No problem. Git handles it painlessly.

    :::console
    $ cd ~/Dropbox/shared/foo
    $ git commit --author 'Coauthor <who@doesnt.use.git>' && git push
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
