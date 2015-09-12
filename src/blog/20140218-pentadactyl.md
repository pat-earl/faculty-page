title: Installing older versions of Pentadactyl in Firefox
tags: linux, vim
summary: The "latest" release of Pentadactyl doesn't always run on any modern version of Firefox. Here's how to get and install the bleeding edge version from the source tree.

I'm an avid [vim](http://www.vim.org) user, and try and make all programs I use behave like Vim.
Usually this is painless.
One exception, however, is Firefox: The extension [Pentadactyl] is **splendid**.

However, they have a **TERRIBLE** release schedule.
The "latest" release was over two years ago -- and won't run on any modern version of Firefox.
So if you upgrade Firefox and find [Pentadactyl] doesn't work, try installing a [nightly build](http://5digits.org/nightlies).
That worked fine for me until today.

The current nightly build (2014-02-18) doesn't work on Firefox 24 (more precisely version `24.3.0esr-1~deb7u1` from Debian `wheezy/updates`.
Finding a version that works is a bit painful.
Since I anticipate having this problem multiple times, here's a reminder for myself of what I did:

1. Install mercurial, and get the source:

        $ hg clone http://dactyl.googlecode.com/hg/ dactyl

2. Use `hg blame` to find a version that works:

        $ cd dactyl
        $ hg blame pentadactyl/install.rdf | egrep -i 'm(ax|in)version'
        6983:                 em:minVersion="24.0"
        6994:                 em:maxVersion="30.*"/>

3. In theory this nightly should have worked for me (since I was on Firefox 24).
   But it didn't.
   So I back-tracked to version `6982`:

        $ hg checkout 6982
        $ egrep -i 'm(ax|in)version' pentadactyl/install.rdf
                        em:minVersion="22.0"
                        em:maxVersion="27.*"/>

4. Installing it is painless:

        $ make -C pentadactyl xpi

   and open the file in your browser. This worked for me.
   If it didn't work for you, then do `hg blame` again and backtrack further.

[Pentadactyl]: http://5digits.org/
