---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **UNIX Shells**

CSC252 - UNIX Scripting & Administration

Prof. Patrick Earl

Spring 2022

---

## UNIX Shells

- sh - Bourne Shell
- ksh - Korn Shell
- -*bash** - *Bourne Again Shell*
- dash - Debian Almquist Shell
- tcsh - TC Shell
- zsh - Z Shell
- *Most of following information will apply to bash and tcsh*

---

## The Command Line

- Commands execute a program in response to a prompt
  - `ls`
- A *simple* command includes the command and any arguments.
  - *Simple* commands can be any utility program, shell script, application program, etc.
- `command arg1 [arg2] ... [argn] RETURN`
  - The shell will interpret this command
  - *Whitespace* is used to separate the various parts

---

## Command Syntax

- Command Arguments
  - Default Values vs. Required
  - Optional Arguments - `[ ]`
- Arguments are *tokens* a command acts on
  - *token* or *word* - A sequence of nonblank characters
- `cp temp tempcopy`
- Command arguments are numbered starting at zero and include the command itself

---

## Command Syntax (continued)

- *Options*
  - Modifies the effects of the command
- *Usually* optional in a command
  - `ls` options?
- Options are interpreted by the program called by the command line
  - Proceed arguments for the command

---

## Command Syntax (continued)

- Short v Long Options
  - `-h` - Short Options (Hyphen followed by one character)
  - `--help` - Long Options (Two Hyphens followed by two or more chars)
  - *Not a standard, depends on the program*
- Short options can *usually* be combined 
  - `ls -l -a` and `ls -la`

---

## Command Syntax (continued)

- Option commands *with* required arguments
  - `gcc -o`
- "Human-Readable" file sizes
  - `ls -lh`
- `--` - Convention that indicates the end of options
  - File named `-l`

---

## Processing

- tty device driver examines the characters entered and determines to send them to the shell.
  - `CONTROL-H` - Character erase
  - `CONTROL-U` - Kill a line
  - `CONTROL-W` - Erase a word
  - `CONTROL-L` - Clear Screen
  - Immediate Actions
- Non immediate actions are placed in a buffer for tty until RETURN is pressed and then handled by the shell.

---

## Processing 

- The Shell will look at the line as whole and *parse* it into various parts.
  - Using whitespace to separate.
  - The shell will start by looking for the command by filename.

---

## Processing

- `ls`
- `/bin/ls`
- Absolute and Relative Paths
- Simple filenames require the shell to search a list of directories for a filename that matches.
  - PATH
- If found, the shell spawns a new *process* and waits for it to finish.

---

## Standard Input & Output

- *Standard Output* - Place where the program can send information (usually text)
- *Standard Input* - Where information can come from (again usually text)
- Program never "knows" if it's a keyboard, printer, monitor, etc.
  - Programs can query the Kernel to determine if talking to a terminal (`isatty()`)
- *Standard Error* - Used for error messages
- `cat`
  - *CONTROL-D* - "EOF"

---

## Redirection

- `>` - Standard Output
  - *Can destroy a file (clobber)*
- `>>` - Append
- `<` - Standard Input

---

## Filename Generation

- *globbing*
  - `*` - Wildcard (Zero or More Matches)
  - `?` - Wildcard (One Character)
  - `[..]` - Any Character within the brackets
- `\`command\`` - Command substitution
- `|` - Pipe
- `;` - Separate Commands

---

## set

- Configuration of various shell options
- `set`
  - `-o` sets an option
  - `+o` unsets
  - `noclobber`
  - `ignoreeof`
  - `history`

---

## Pipelines

- One or more commands separated by the pipe `|`
- Sends the standard output of proceeding command to the standard input of the next
- `command_a [arguments] | command_b [arguments]`
- `command_a [arguments] > temp; command_b [arguments] < temp; rm temp`
- *Filters*
  - Command that processes an input stream to processes to an output

---

## Environment

<style scoped>
  li { font-size: 90% }
</style>

- Environment Variables
  - `export`
  - `printenv` or `env`
- `HOME`
- `PATH`
- `PS1`
- `USER`
- `SHELL`
- `TERM`
- `CDPATH`