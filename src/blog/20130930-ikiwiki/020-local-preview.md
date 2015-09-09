title: Setting up a local preview or creating a static site
breadcrumb: /{{dirname}}.md

It's usually nice to be able to see changes locally, before having the whole world see them.
Also, it's often convenient to use ikiWiki to create a static site.
Both these tasks are easy to do (but aren't documented too well).
Here are brief instructions:

1. First install ikiwiki on your local machine.

2. Clone the wiki repository into the directory `local-wiki`.

3. Copy your wiki setup file from the server into `preview.setup` and put it into the local `local-wiki` directory.

4. Edit `preview.setup` and make the following changes:

        srcdir: .
        destdir: ./html_output
        exclude: (^|/)Makefile$|\.setup$|(^|/)html_output

    Also edit `libdir` if you have custom ikiwiki scripts on the server

5. For speed improvement you might want to comment out the lines with

        rcs
        git_wrapper
        cgi_wrapper

6. Disable unnecessary plugins: `userlist`, `notifyemail`, `404`, `recentchanges`.

7. Disable the cgiurl, and discussion pages.
   If you don't want the default documentation etc. that comes with the default ikiWiki, also disable the default underlay.

        # cgiurl: 
        underlaydir: /dev/null
        discussion: 0

8. Create a file called `Makefile` with the following:

        refresh:
                ikiwiki --setup preview.setup --verbose --refresh

        rebuild:
                rm -rf html_output
                ikiwiki --setup preview.setup --verbose --rebuild


9. Run `make rebuild`. Now running `make` will refresh your wiki.
   Open `html_output/index.html` in your local browser and you have a local preview.

10. If you wanted to create a static site, then the contents are in the `html_output` directory.
    [rsync](http://rsync.samba.org/) this directory to your server and you're good to go.
