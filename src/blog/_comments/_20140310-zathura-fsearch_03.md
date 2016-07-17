page: 20140310-zathura-fsearch.md
subject: Re: Thanks, that was really useful. How did you figure this out?
name: Gautam Iyer
email: gautam@math.cmu.edu
avatar: http://cdn.libravatar.org/avatar/0ec534a31b72b69338d0897211ec9925
date: 2016-07-16 21:31:28 EDT
ip: 24.3.21.34
referer: http://www.math.cmu.edu/~gautam/sj/blog/20140310-zathura-fsearch.html

> Did you have to go through the source to find the "input" and "line" variables?

Thankfully no. It's in the man page, but a little cryptic. Explicitly, the man page of `zathura` (under `SYNCTEX SUPPORT`) says *"For convince zathura also knows how to parse the output of  the `synctex  view`  command."* Now if you look in the help of `synctex`, the variables are documented. (You can access it by `synctex help edit` and `synctex help view`)
