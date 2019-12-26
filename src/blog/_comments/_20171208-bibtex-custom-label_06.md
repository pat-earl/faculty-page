page: 20171208-bibtex-custom-label.md
subject: Re: Nice, but labels aren't sorted alphanumerically
name: Gautam Iyer
email: gautam@math.cmu.edu
avatar: http://cdn.libravatar.org/avatar/0ec534a31b72b69338d0897211ec9925
date: 2019-11-01 11:21:30 EDT
ip: 127.0.0.1
referer: http://localhost:8000/blog/20171208-bibtex-custom-label.html

> The style is very nice. One gripe: I have labels such as `RFC1` and `RFC2`, which I'd expect to appear in that order. However, the order is reversed when the latter is cited before the former.

Yikes, true. I don't know how to fix BibTeX sort issues unfortunately. I've
had trouble with it in the past.

> (Also, `\bibliographystyle{habbrv}` should be `\bibliographystyle{halpha-abbrv}`, or `halpha-abbrv.bst` should be renamed.)

Indeed, thanks. I fixed it.

GI
