title: Expanding aliases in zsh
tags: linux
summary: I wanted to make some of my [zsh](http://zsh.sourceforge.net/) aliases behave like [vim](http://www.vim.org/) abbreviations: Namely, as soon as you press space, the alias is expanded and you see the expanded command before executing it. Since I have a large number of clunky aliases, I didn't want all aliases to be expanded by default.
summary:
summary: Consequently, I came up with the following (based on something I first saw [here](http://blog.patshead.com/2012/11/automatically-expaning-zsh-global-aliases---simplified.html)).

{{'\n'.join( summary )}}

``` shell
typeset -a ealiases
ealiases=()

function ealias()
{
    alias $1
    ealiases+=(${1%%\=*})
}

function expand-ealias()
{
    if [[ $LBUFFER =~ "\<(${(j:|:)ealiases})\$" ]]; then
        zle _expand_alias
        zle expand-word
    fi
    zle magic-space
}

zle -N expand-ealias

bindkey -M viins ' '        expand-ealias
bindkey -M viins '^ '       magic-space     # control-space to bypass completion
bindkey -M isearch " "      magic-space     # normal space during searches
```

The last three bindkey commands are assuming you are primarily using VI mode. If you're not, you might need to either remove the `-M viins` above, or replace it with `-M emacs`, etc.

Finally, to define an expandable alias use `ealias`.
The syntax of `ealias` is the same as that of `alias`
For example, I use

``` shell
ealias gc='git commit'
ealias gp='git push'
```

Now typing `gc` in a position where zsh expands a command will appear like you typed `git commit`.
