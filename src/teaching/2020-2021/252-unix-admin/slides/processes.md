---
title: "UNIX Processes"
subtitle: "CSC252"
author: Patrick Earl
date: 03/18/2021
slideNumber: true
revealjstheme: simple
width: 1600
height: 1000
transition: fade
---

## Overview
* Program Space
* What is a process?
* UNIX Boot
* Parents and Children
* Basic Process Commands
* Process Table
* Daemon Process
* Process States
* Managing Processes

---

## Program Space
* Memory Space separation to protect system internals
* User(Land)
  * User Applications
  * File Utilities
* Kernel
  * stat
  * System Calls

---

## What is a process?
* Each program launched becomes a *process* until it exits
* The Kernel will manage processes
  * Assign a *process id* (PID)
  * Assign memory space
  * Accept System Calls
  * Scheduling on the processor
  * Send SIGNALs
* `ps` - View current processes

---

## UNIX Boot
* Once control is handled over the kernel, the first process is *created* (or *spawned*).
* Usually known as *init*
  * Will have *pid* of 0 or 1
* Init is responsible for launching all the processes required to run the system
  * Daemons
  * Memory Management
  * I/O Events
* All processes created could be considered *children* of init. 

---

## Parent and Children
* The two main system calls for process creation:
  * `fork()`
  * `exec()` - exec has many different forms
* The process calling `fork()` becomes the parent process
  * *PPID* - Parent Process ID
  * The newly created process is consider a *child* process
* `exec()` - Will execute an executable and replace a processes' memory space

---

## Sessions
* After successful login, a new *session* is created.
* The process that handles login, will fork and exec the user's configured shell
* `job` - Manage jobs in a session
* `&` - Send a command to the background

---

## Basic Process Commands
* history
* jobs
* kill
* fg,bg
* ps
* top
* uptime
* free
* pstree
* nohup

---

## The Process Table
* Kernel Data Structure to manage running processes
* Contains the following:
  * *Process ID*
  * *Process Owner*
  * *Process Priority*
  * *Environment Variables*
  * *Parent Process*
  * *Location of code, data, stack, and user area* (Memory Space)
  * *Pending Signals*

---

## Daemon Process
* Typically a process running in the background *indirectly* interacting with a user.
* `daemon` in section 7 of man page
* Example Daemons:
  * `sshd`
  * `httpd`
  * `ftpd`

---

## Process States

---

## Process Termination

---

## Process Internals

---

## Process Areas

---

## Scheduling Jobs
