---
title: "Command Presentations"
subtitle: "CSC252"
author: Patrick Earl
date: 02/23/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## grep & fgrep

* Allows for searching for patterns within a file
  * Can take a list of files or input from standard input
  * *[file-list] should be ordinary files*
  * *pattern* is a regular expression **Appendix A**
* `fgrep` or `grep -f`
  * Can only process simple strings and doesn't process regular expressions
* Returns lines that matter the pattern

## grep examples

* `~earl/public/csc252/grep/`
* `-v` - Inverses the search (Lines that *DON'T* contain the pattern)
* `-n` - Display the line number of each displayed line
* `-w` - Pattern match a whole word
* `-i` - Case insensitive

## bzip2, bunzip2, bzcat

* `bzip2` - Compresses files
* `bunzip2` - Unzips files compressed using *bzip2*
* `bzcat` - Display files compressed with *bzip2*
* Difference from gzip?
  * Uses a different algorithm for compression
  * Compresses files better than `gzip`
* `~earl/public/csc252/bzip`

## ssh

* ssh has many different aspects, allowing you to interact with a remote machine.
* `~/.ssh` directory
  * `config`
  * `known_hosts`
* Login or Run a Command
  * `ssh [user]@machine-name`
  * `ssh [user]@machine-name command [with] [arguments]`

## Bonus - scp

* Copy files from and to a remote server
* `scp [user]@from-host:source-file [user]@to-host:destination-file