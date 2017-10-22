title: Source Code and Setup Instructions for this site.
summary: I recently rewrote my website using a static site generator. [This](https://gitlab.com/gi1242/sjinja-www) is the source code for [my website](http://www.math.cmu.edu/~gautam), and here are the features / setup-instructions.

{{summary}}

## Description

* It is a static site, based on [staticjinja](http://staticjinja.readthedocs.org/en/latest/).

* Content is written in HTML or [markdown](https://daringfireball.net/projects/markdown/), and served as HTML5 files with an (almost) vanilla [bootstrap](http://getbootstrap.com/) layout.

* Your file directory structure is preserved. Binary files are directly copied, and the rest are passed through [Jinja2](http://jinja.pocoo.org/).

## Source code

I use a heavily customized build script (available [here](https://gitlab.com/gi1242/sjinja-www)) to provide the following:

* Render [markdown](https://daringfireball.net/projects/markdown/) with lots of extensions ([MathJax](https://www.mathjax.org/), wikilinks, breadcrumbs, etc.).

* Allow using [Jinja2](http://jinja.pocoo.org/) templates in markdown.

* Provide globbing functions (accessible via Jinja2) to display lists of files.

* Use a YAML site configuration file

* Only render files based on modification times for speed (configurable).

## Setup Instructions

* To download use

        git clone --recursive https://gitlab.com/gi1242/sjinja-www.git

    (Don't forget `--recursive`, otherwise you will have to run `git submodule update --init` to update the submodules.)

* Edit `site.cfg` and put in your URL / defaults.

* Generate the site by running `build.py`. Use `build.py -h` for options. Pass regexps on the command line to force re-rendering of certain files.

## Editing instructions

* Generic Markdown syntax can be found [[{{filesdir}}/markdown.md|here]].

* Site specific markdown extensions and macros can be found [[{{filesdir}}/README.md|here]].

* The current layout and structure is described [[{{filesdir}}/layout.md|here]]. (You can ignore this if you plan to just write in Markdown, or want to create your own layouts from scratch.)

## Bugs

* 2017-10-21: Continuously watching for changes with `-w` isn't perfect. Any file you change is always re-rendered, but the dependencies and changes to meta-data are ignored. I'm not interested in fixing this. Re-running the build script (without `-w`) renders everything correctly.

