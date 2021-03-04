---
title: "BASH & Shell Scripting"
subtitle: "CSC252"
author: Patrick Earl
date: 03/03/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Pronunciation guide to UNIX
* [See Here](https://ss64.com/bash/syntax-pronounce.html)

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

---

## Shell Scripting
* `#!` - specifies a shell
* `#` - Comments
* Command separation
    * `;` AND *NEWLINE*
* `&&` and `||` - Boolean Control
* `\` - Continue a command

---

## Parameters and Variables
* *Shell Parameters* - A value you or the shell script can access
* *Variables* - shell parameter that consists of:
    * Letters
    * Digits
    * Underscores
  
--- 

* *User-Created*
* *Shell Variables* & *Env Vars*
* Syntax: `VARIABLE=value`
    * `num=1`
    * **Cannot** have whitespace

---

* echo copies it's arguments to stdout
* `$` - Substitute the variable's value
    * $ can be quoted, with single quotes or backtick
* Double Quotes don't prevent substitution, but do turn off special meanings for other characters.
    * Used for variables with spaces in them

---

* "{}" BRACES
    * Braces insulate variable name from adjacent chars
    * `PREF=counter; WAY=$PREFclockwise; FAKE=$PREFfeit`
* `unset` - Set the value of a variable to *null*
* `readonly`
* `declare`
    * `declare -r`
    * `declare -x`

---

## User Prompts
* `read` - Read from stdin (or FD) and split into words
    * `read [options] [NAMES ...]`
    * `read -p <prompt> [NAMES ...]`
* If no *NAME*, gets stored in variable *REPLY*

## Control Flow
* `if..then` - *test* command
* `test "thing" = "thing2"`
* `test $# -eq 0`
* `[]` - Alias for *test*