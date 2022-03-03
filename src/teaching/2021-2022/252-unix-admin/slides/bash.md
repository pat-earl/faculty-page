---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **BASH Shell**

CSC252 - UNIX Scripting & Administration 

Prof. Patrick Earl

Spring 2022

---

## Pronunciation guide to UNIX
- [See Here](https://ss64.com/bash/syntax-pronounce.html)

---

# **BASH**
- Bourne Again Shell - *bash*
    - sh - Bourne Shell, written by Steve Bourne at AT&T's Bell Lab
    - Many systems sym-link sh to bash (or dash)
- POSIX Standard
    - *Portable Operating System Interface*
    - [POSIX FAQ](http://www.opengroup.org/austin/papers/posix_faq.html)

- `chsh` - Change your login shell

---

## Shell Files
- Startup Files
    - Files a shell runs to initialize itself
    - Files depend on it being an interactive or non-interactive
- Login Shells
    - First shell that displays a prompt to login into a system

---

- *Interactive Shells*
    - /etc/profile
    - .bash_profile, .bash_login, .profile
    - .bash_logout
- *Non-Interactive*
    - .bashrc
    - /etc/bashrc

---

# `source`

- `.`(dot) or `source`
- If changes are made to your startup files, these commands can allow for "reloading"
    - Typically to see the changes you'd have to logout and in again.

---

# Standard Error Redirection
- 0 - stdin, 1 - stdout, 2 - stderr
- `<, >`
    - `<` - shorthand for `0<`
    - `>` - shorthand for `1>`
    - `2>` - redirect stderr
    - `&>` - Redirect stdout & stderr
- Can have more than one redirection.
  
---

| Operator | Meaning |
| -- | -- |
| >!*filename* | Redirects to stdout and overwrites even if *noclobber* is set | 
| >>*filename* | Redirects and appends stdout to filename. Creates if doesn't exist |
| &>*filename* | Redirects stdout and stderr to filename |
- *Table 8-2 from Practical Guide to Linux Textbook*

---

# **BASH aliases**

- Used to define a command that will run another (usually long) command.
- `alias rm='rm -i'`
- `unalias`
- Single vs Double Quotes
    - Expanding of variable *values* during creation or during run-time
- `alias dirA="Working Directory A: $PWD"`
- `alias dirB='Working Directory B: $PWD'`

---

# **Shell Scripting**
- `#!` - specifies a shell
- `#` - Comments
- Command separation
    - `;` AND *NEWLINE*
- `&&` and `||` - Boolean Control
- `\` - Continue a command

---

# Parameters and Variables
- *Shell Parameters* - A value you or the shell script can access
- *Variables* - shell parameter that consists of:
    - Letters
    - Digits
    - Underscores
  
--- 

- *User-Created*
- *Shell Variables* & *Env Vars*
- Syntax: `VARIABLE=value`
    - `num=1`
    - **Cannot** have whitespace

---

- echo copies it's arguments to stdout
- `$` - Substitute the variable's value
    - $ can be quoted, with single quotes or backtick
- Double Quotes don't prevent substitution, but do turn off special meanings for other characters.
    - Used for variables with spaces in them

---

- "{}" BRACES
    - Braces insulate variable name from adjacent chars
    - `PREF=counter; WAY=$PREFclockwise; FAKE=$PREFfeit`
- `unset` - Set the value of a variable to *null*
- `readonly`
- `declare`
    - `declare -r`
    - `declare -x`

---

# Quotes

- `'` - Single Quotes
    - Preserves the literal value of each character
    - [GNU BASH Manual 3.1.2.2](https://www.gnu.org/software/bash/manual/html_node/Single-Quotes.html)
- `"` - Double Quotes
    - Preserves the literal value of each character except: *$, \`, \\, and !*
    - [GNU BASH Manual 3.1.2.3](https://www.gnu.org/software/bash/manual/html_node/Double-Quotes.html)

---

# User Prompts
- `read` - Read from stdin (or FD) and split into words
    - `read [options] [NAMES ...]`
    - `read -p <prompt> [NAMES ...]`
- If no *NAME*, gets stored in variable *REPLY*

---

# Shell Arithmetic
- `declare -i` 
    - Declare a variables as an integer
- `((var+1))`

---

# Control Flow
- `if..then` - *test* command
- `test "thing" = "thing2"`
- `test $# -eq 0`
- `[]` - Alias for *test*
    - `[[]]` - Bash Extension

---

# Arguments
- `$1, $2, $3`
- `$#` - Number of Args  
- `shift` - Shift *n* arguments

---

# Usage Message
- If non-correct or non-arguments are passed show a *usage* message
- `Usage: ./command [arguments]`

---

# Array Variables
- bash supports *1D arrays* and uses zero-based indexing
    - Meaning the first element is at index 0
- `name=(element1 element2 element3)`
- `NAMES=(leela fry bender)`
- `${NAMES[2]}`
    - Braces are not optional for arrays

---

- `[*] [@]` operators
    - Expand array into a variable
- `A=("${NAMES}[*]")`
- `B=("${NAMES}[@]")`
- `${ #NAMES[@]}`


---

# Looping
- `while test-commands; do commands; done`
- `for name [ [in words ..] ] ; ] do commands; done`
    - Expands the *words* and execute commands once for each member
- `break`
- `continue`
  

---

# case statements
```bash
case test-string in
    pattern-1)
        commands-1
    ;;
    pattern-2)
        commands-2
    ;;
    pattern-3)
        commands-3
    ;;
esac
```

---

# Functions
- `fname () { commands; }`
- `function fname() { commands; }`

---

# Command Substitution
- `$(command)`
- `` `command` ``
- Performs the command in a subshell and replaces it with the stdout of the command

---

# Parameter Expansion
- [BASH Manual Section](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
- `${NAME#pattern}` - Suffix Removal
- `${NAME%pattern}` - Prefix Removal