title: Maintaining an old texlive installation.
tags: latex, linux
summary: How to subbornly continue using an obsolete version of [texlive](https://www.tug.org/texlive/) well after its due date.

As of 2014-07-12, [texlive] 2013 is no longer supported and users are required to upgrade to [texlive] 2014.
Consequently, any attempts to install new packages with `tlmgr` are met with an unfriendly message of the form:

> tlmgr: The TeX Live versions supported by the repository (2014) does
> not include the version of the local installation (2013).

If you'd like to keep using your old (2013) installation, and need to run `tlmgr` for some reason, then do the following first:

    tlmgr option repository ftp://tug.org/historic/systems/texlive/2013/tlnet-final

Now you should be able to manage packages with `tlmgr` as usual.
(Note: No updates for texlive 2013 will be available; but you can certainly install / remove packages...)

[texlive]: https://www.tug.org/texlive/
