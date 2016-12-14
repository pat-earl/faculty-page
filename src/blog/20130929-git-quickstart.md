title: A git quickstart guide for LaTeX users
tags: git, latex
summary: [Git](http://git-scm.com/) is a [source control management](http://en.wikipedia.org/wiki/Source_Control_Management)
    system that you can use to track changes in any text file.
    Git, however, is quite complicated and learning it can be quite time consuming.
    This is a quick introduction to git for someone who will primarily use git to edit LaTeX/text documents (not code) and possibly collaborate with a handful of co-authors.

{{summary | join('\n')}}

{% for f in glob( basename[:-3] ~ "/[0-9]*.md" ) | sort -%}
* [[{{f}}]]
{% endfor %}
