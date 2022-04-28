---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
title: Text Processing
---

# **Text Processing**

CSC252 - UNIX Scripting & Administration

Prof. Patrick Earl

Spring 2022

---

## Regular Expressions (Regex or RE)
- *Regular Expressions* are sequences of characters that define a *search pattern* in text. 
- **POSIX Basic Regular Expressions** - BRE
- **POSIX Extended Regular Expression** - ERE
    - Both extend basic functionality of the regex language and can be used in POSIX following editors.
- *Appendix A* in textbook.

---
  
- Simple Strings:

| REGEX | Matches | Examples |
| -- | -- | -- |
| /ring/ | *ring* | *ring*, sp*ring*, *ring*ing, st*ring*ing |
| /Thursday/ | *Thursday* | *Thursday*, *Thursday*'s |
| /or not/ | *or not* | *or not*, po*or no*thing |

---

## Metacharacters
* `.` (Dot) - Matches any single character
* `[]` (Brackets) - Defines a character class. Will match any character within the class
    - You can use a hyphen (`-`)to define a range of characters: `[a-z]`
* `*` (Star) - Represents a zero character. Will match on zero or more occurrences
* `^` (Carrot) - Regex can only match at the start of a string
* `$` (Dollar) - Can only match at the end of a line. 
    - These two are known as *anchors* because force matching at the start or end of a line.
* `\` (Back Slash) - Used to quote these special characters (Some exceptions like Perl).

---

- Character Class Examples
  
| Class | Defines | 
| -- | -- |
| [xyz] | Defines a character class that matches *x, y, or z*. | 
| [^xyz] | Defines a character class that matches anything *except* *x, y, or z*. |
| [x-z] | Defines a character class that matches any character *x* through *z* inclusive. |
| `\(xyz\)` | Matches what *xyz* matches |

---

- **POSIX Character Classes**

| POSIX | Similar To | meaning |
| ---- | ---- | ---- |
| `[:upper:]` | `[A-Z]` | uppercase letters |
| `[:lower:]` | `[a-z]` | lowercase letters |
| `[:alpha:]` | `[A-Za-z]` | Upper and lowercase letters |
| `[:digit:]` | `[0-9]` | digits |
| `[:alnum:]` | `[A-Za-z0-9]` | Digits, Upper, and Lowercase letters |
| `[:blank:]` | `[\t]` | space and TAB characters only |
| `[:space:]` | `[\t\n\r\f\v]` | Blank (whitespace) characters |

---

- Extended Regular Expressions
  
| Expression | Matches |
| -- | -- | 
| + | Matches one or more of the preceding character | 
| ? | Matches zero or more of the preceding character | 
| (xyz)+ | Matches one or more of what *xyz* matches |
| (xyz)? | Zero or more of what *xyz* matches |
| `xyz\|abc` | Matches either *xyz* or *abc* |

---

## *sed*
- Stream Editor (SED)
    - Transforms an input stream (file or stdin).
- SED in default will transform line by line
- Syntax:

```bash
sed [-n] program [file-list]
```

- Output from the SED command goes to standard output

---

## *sed* (continued)
- Options of note:
    - *-f* - Read a program file instead from the command line
    - *-i[suffix]* - Edit the file in place. Using suffix will make a backup of the original file
    - *-n* - SED won't send output to stdout, unless the Print **(p)** flag is used.

---

- General syntax of a program:

```sed
[address[,address]] instruction [argument-list]
```

- Address optionally select line(s) and runs the command on it.
    - No address means the instruction will be ran on *ALL* lines.
- sed commands can be separated using a semicolon (;).

---

## *sed* (continued)
- *sed* processes input as follows:
    - Read one line of input
    - If the addresses matches the input line, run the instruction.
    - Repeat if there is more than on instruction that matches the address.
    - Repeat until all lines of input are processed.

---
  
## *sed* - Addresses
- Line numbers can be used as an address to select a line. `$` can be used to represent the last line of input.
- A regular expression can also be used to select lines that match the REGEX pattern.

---

## *sed* - Instructions

- There are two buffers:
    - *Pattern Space* - Holds the initially read line
    - *Hold Space* - Can hold data while manipulating data in *Pattern Space*

--- 

- *a* (append):
    - Append one or more lines to the currently selected line
    - `[address[,address]] a\ text \ text \ text`
- *c* (change):
    - Replace text at the current line with the new text
- *d* (delete):
    - Causes sed to not write out the current line or process more instructions.
    - It'll read the next input line

---

- *i* (insert):
    - Similar to append, except text is placed *before* the selected line.
- *N* (next w/o write):
    - Reads the next input line and appends it to the current line. 
    - Can be used to remove **NEWLINESs** from a file.
- *n* (next):
    - Writes out the currently selected line, reads the next, and starts processing the new line.

---

- *p* (print):
    - Prints out the selected line to stdout. Does not reflect possible changes of subsequent instructions.
- *q* (quit):
    - Causes *sed* to quit immediately.
- *r* (file read):
    - Read the contents of a file and append it to the currently selected line.
    - Syntax: `r file-name` (Can only be a single file)

---

- *s* (substitute):
    - Allows for matching on a pattern and replacing the contents
    - Syntax: `s/pattern/replacement-string/[g][p][w file]`
    - *Pattern* is a regular expression
    - The flags:
        - *g* - Global flag: Replace all non-overlapping occurrences
        - *p* - Print Flag: Send substitutions made to stdout.
        - *w* - Write Flag: Sends the output to the specified file.
  
---

## Control Structure
- `!` (NOT) -
    - Causes *sed* to apply instructions to lines *not* selected by the address portion. 
    - `"3!d"` - Deletes all lines except line 3.
- `{}` (Group Instructions) -
    - Allows for grouping of instructions together for a given address.
    - Use a semicolon on a single line.

--- 

## *awk*
- Pattern-Scanning and Processing Language that searches one or more files for records (usually a line) that matches a pattern.
- *AWK* is data-driven:
    - Describe what data you want to find.
    - Do something with that data once it's found.
- *awk* takes this general form (*gawk*):
    - `gawk [options] [program] [file-list]`
    - `gawk [options] -f program-file [file-list]`
- Be aware there are different versions of awk: 
    - GNU AWK (gawk), original awk, or mawk. 
    - Most of our examples will work with *gawk*.

---

## *awk* Program
- Awk can accept a program file or a program enclosed in single quotes on the command line.
- The program is made up of one more *patterns* followed by an *action*.
    - `[pattern] {action}`
    - If a pattern isn't given, the action is applied to all lines of input.
- **Patterns**
    - BEGIN & END:
        - Execute a command before *awk* starts processing a file and afterwards.
    - ~ and !~:
        - Use a regular expression as a *pattern*
            - !~ tests for not matching the pattern

---

    - comma (,):
        - Range operator. Select a range based on matched patterns
    - Patterns can be combined using BOOLEAN operators (&& (AND), || (OR))

---

- **Actions**
    - By default the action is to *print*
        - `{print}`
        - Takes the input and outputs to stdout.
    - Comments - #
    - Variables
        - Variables can be created at any time and are initialized to 0.
        - You can declare user variables with *BEGIN*
        - There are also system variables 

---

- **Actions**
    - Functions
        - awk provides functions to manipulating numbers and strings
    - Arithmetic
    - Associative Arrays
    - printf
        - *print* but with the ability to control the output format
    - Control Structures
        - if..else
        - while
        - for
        - break
        - continue

---

## System Variables

| Variable | Meaning |
| -- | -- |
| $0 | The current record (as a single variable) |
| $1-$n | Fields in the current record |
| FILENAME | Name of the current input file (or null if stdin) |
| FS | Input field separator (Default: SPACE or TAB) |
| NF | Number of fields in current record |
| NR | Record number of current record |
| OFS | Output Field Separator |
| ORS | Output Record Separator |
| RS | Input Record Separator |

---

## Built-in Functions

| Function | Meaning |
| -- | -- |
| `length(str)` | Returns the number of characters in -str* - or - num of chars. in current record. |
| `int(num)` | Returns the integer portion of -num*. |
| `index(str1, str2)` | Returns the index of -str2* in *str1* or 0 if *str2* is not present. | 

---

| Function | Meaning |
| -- | -- |
| `split(str, arr, del)` | Places elements of -str*, delimited by *del*, in the array *arr*. |
| `sprintf(fmt, args)` | Formats -args* according to *fmt* and returns the formatted string. |
| `substr(str, pos, len)` | Returns the substring of -str* that beings and *pos* and is *len* chars long. |
| `tolower/toupper` | Returns a copy of the passed -str* replacing with their lower/upper case counterpart. |

---

## printf formatting

| conv | Type of conversion |
| -- | -- | 
| -d* | Decimal |
| -e* | Exponential Notation |
| -f* | Floating-point number | 
| -o* | Unsigned Octal | 
| -s* | String of characters |
| -x* | Unsigned hexadecimal |