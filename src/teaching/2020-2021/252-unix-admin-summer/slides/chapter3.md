---
title: "The Utilities"
subtitle: "CSC252"
author: Patrick Earl
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: fade
---

## Special Characters

* Some characters have special meaning in *the shell*
  * These characters should be avoided when naming a file
* & ; | * ? ' "     ` [ ] ( ) $ < > { } # / \ ! ~
* Whitespace
  * Not special characters, but have special meanings
  * RETURN (ENTER), SPACE, TAB
* Quote (or Escape) special characters
  * Use the `backslash` (\\) or `single quotes` (')

## Basic Utilities

* Linux terminology uses the term *directory*, a resource that holds files or other directories
  * Typically known as Folders on Windows and macOS.
* `ls` - List the name of files
* `cat` - Display the contents of a text file
* `rm` - *remove* a file
  * `rm -i` - Interactive version

## Helper Commands

* `clear`
* `echo`
* `date`
* `script`
* `who`, `w`

## Locating Utilities

* `which`
* `whereis`
* `type` - *bash* built-ins
  
## Users

* `id` - Account Information
* System Users
  * root
  * mail
  * bin
* `/etc/passwd`
* `whoami` 

## Groups

* `groups`

## The Terminal

* Sessions
* Environment Variables
* `stty` - Display or Change Terminal Properties

## Honorable Mentions

* `time`
* `cal`
* `hostname`
* `nslookup`
* `uname`