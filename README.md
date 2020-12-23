# Kutztown Faculty Page

This is the repo for what is currently running on my employer's web server, located [here](csit.kutztown.edu/~earl/). This work
is very much based off the amazing work of [Gautam Iyer](http://www.math.cmu.edu/~gautam/sj/). Thanks to him for publishing his work, sjinja-www, which can be found on [here on gitlab](https://gitlab.com/gi1242/sjinja-www/)

## Setup Instructions

* Edit `site.cfg` and put in your URL / defaults.

* **HIGHLY** recommended you use a virtual env for this. If you're unsure how to do that, [brush up here](https://docs.python.org/3/library/venv.html).

* Once in your virtualenv (or base env if you're brave), just run *pip install -r requirements.txt*

* Generate the site by running `build.py`. Use `build.py -h` for options. Pass regexps on the command line to force re-rendering of certain files.

* Editing instructions and other details can be found [here](http://www.math.cmu.edu/~gautam/sj/blog/20171021-setup.html).

## Other Stuff

Again most of the work is credited to *Gaumtam Iyer*, who released this under the [CC 4.0 BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. 

I've made minor changes to adapt it to my needs. This list will be updated as things change

* Moved from the submodule setup to just installing modules in a virtualenv. Injecting into sys.path just wasn't working for me and led to import errors.


## This is from Gautam's orginal README
*** 

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

