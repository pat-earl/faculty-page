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

* Read [[/blog/20171021-setup/README.md|this file]] for site specific extensions / macros, and [[/blog/20171021-setup/markdown.md]] for generic Markdown syntax.

## Bugs

* 2017-10-21: Continuously watching for changes isn't perfect. Any file you change is always re-rendered, but the dependencies and changes to meta-data are ignored. I'm not interested in fixing this. Re-running the build script produces correct output.

