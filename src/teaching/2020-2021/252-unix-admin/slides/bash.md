---
title: "Chapter 8: BASH"
subtitle: "CSC252"
author: Patrick Earl
date: 02/25/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## BASH
* Bourne Again Shell - *bash*
    * sh - Bourne Shell, written by Steve Bourne at AT&T's Bell Lab
    * Many systems sym-link sh to bash (or dash)
* POSIX Standard
    * *Portable Operating System Interface*
    * [POSIX FAQ](http://www.opengroup.org/austin/papers/posix_faq.html)

* `chsh` - Change your login shell

---

## Shell Files
* Startup Files
    * Files a shell runs to initialize itself
    * Files depend on it being an interactive or non-interactive
* Login Shells
    * First shell that displays a prompt to login into a system

---

* *Interactive Shells*
    * /etc/profile
    * .bash_profile, .bash_login, .profile
    * .bash_logout
* *Non-interactive*
    * .bashrc
    * /etc/bashrc

## source
* `.`(dot) or `source`
* If changes are made to your startup files, these commands can allow for "reloading"
    * Typically to see the changes you'd have to logout and in again.

## Standard Error Redirection
* 0 - stdin, 1 - stdout, 2 - stderr
* `<, >`
    * `<` - shorthand for `0<`
    * `>` - shorthand for `1>`
    * `2>` - redirect stderr
    * `&>` - Redirect stdout & stderr
* Can have more than one redirection.
  
---

| Operator | Meaning |
| -- | -- |
| >!*filename* | Redirects to stdout and overwrites even if *noclobber* is set | 
| >>*filename* | Redirects and appends stdout to filename. Creates if doesn't exist |
| &>*filename* | Redirects stdout and stderr to filename |
*Table 8-2 from Practical Guide to Linux Textbook*