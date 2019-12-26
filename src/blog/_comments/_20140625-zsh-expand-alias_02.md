page: 20140625-zsh-expand-alias.md
subject: Re: A little question
name: Gautam Iyer
email: gautam@math.cmu.edu
avatar: http://cdn.libravatar.org/avatar/0ec534a31b72b69338d0897211ec9925
date: 2019-12-24 05:25:40 EST
ip: 127.0.0.1
referer: http://localhost:8000/blog/20140625-zsh-expand-alias.html

> How to understand this statement `"\<(${(j:|:)ealiases})\$"`?

It's described in the `zshexpn` man page. It joins all elements of the
`ealiases` array with `|`, and so the above gives a regular expression
matching any existing expandable alias.
