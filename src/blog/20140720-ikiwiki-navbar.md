title: De-Uglyfying ikiWiki and other horror stories.
tags: linux, ikiwiki
summary: I use [ikiWiki](http://ikiwiki.info) to host this (and a few other) wiki's. I love it! It is based on [git](http://git-scm.com/), and hosts pages written in [markdown](http://daringfireball.net/projects/markdown/) and [multimarkdown](http://fletcherpenney.net/multimarkdown/). From a development point of view it is great:
summary:
summary: 1. Type documents into [vim](http://www.vim.org/).
summary: 
summary: 2. Using [multimarkdown] syntax, and render math with [MathJAX](http://www.mathjax.org/) (setup instructions [[20130930-ikiwiki/010-setup.md|here]]).
summary: 
summary: 2. Press `<c-k>` and look at a local preview (setup instructions [[20130930-ikiwiki/020-local-preview.md|here]]).
summary: 
summary: 3. Type `git commit && git push` and have it uploaded to the server.
summary: 
summary: No annoying (and slow) web-based editors / sign-up forms etc. Great, great great!
summary: 
summary: Now for the bad news: [This is the default look](http://ikiwiki.info/). (And the setup is a b\*\*tch.)
summary: 
summary: It was written in `html 1.0` designed only for `w3m` users on a teletype. If there's even a remote change one of your users might use a (god forbid) GUI or a browser that is less than 100 years old, then you're going to have to work to theme it.

{{'\n'.join( summary )}}

## Theme

[ikiWiki] has exactly one theme that doesn't suck: `actiontabs`.
I use this (with some modifications) on [this site](http://wiki.math.cmu.edu/iki/wiki).
To use this, put

    theme: actiontabs

in your setup file. (Be sure to also enable the `theme` plugin.)

## Navigation Bar

A third party navigation bar plugin is available [here](https://ikiwiki.info/plugins/contrib/navbar/).
It looks just as ugly as everything else.
I fixed a few bugs and hacked it.

Here's what you need to do:

1. Get my version [here](http://wiki.math.cmu.edu/gitweb-pub/?p=ikiwiki-plugins.git;a=blob_plain;f=IkiWiki/Plugin/navbar.pm;hb=HEAD) (or browse the git repo from one of the links below).

2. You will also need [the css file](http://wiki.math.cmu.edu/iki/wiki/navbar.css).

3. Patch your `templates/page.tmpl` as follows:

        --- /usr/share/ikiwiki/templates/page.tmpl      2013-11-30 18:09:54.000000000 -0500
        +++ templates/page.tmpl  2014-07-20 16:38:25.118037883 -0400
        @@ -16,6 +16,9 @@
         <link rel="icon" href="<TMPL_VAR BASEURL><TMPL_VAR FAVICON>" type="image/x-icon" />
         </TMPL_IF>
         <link rel="stylesheet" href="<TMPL_VAR BASEURL>style.css" type="text/css" />
        +<TMPL_IF NAVBAR>
        +<link rel="stylesheet" href="<TMPL_VAR BASEURL>navbar.css" type="text/css" />
        +</TMPL_IF>
         <TMPL_IF LOCAL_CSS>
         <link rel="stylesheet" href="<TMPL_VAR BASEURL><TMPL_VAR LOCAL_CSS>" type="text/css" />
         <TMPL_ELSE>
        @@ -131,6 +134,11 @@
         <TMPL_IF HTML5></aside><TMPL_ELSE></div></TMPL_IF>
         </TMPL_IF>
         </TMPL_UNLESS>
        +<TMPL_IF NAVBAR>
        +<TMPL_IF HTML5><nav id="navbar"><TMPL_ELSE><div id="navbar"></TMPL_IF>
        +<TMPL_VAR NAVBAR>
        +<TMPL_IF HTML5></nav><TMPL_ELSE></div></TMPL_IF>
        +</TMPL_IF>

         <div id="pagebody">

4. Alternately, download my [page.tmpl](http://wiki.math.cmu.edu/iki/wiki/templates/page.tmpl), but be warned that I might have also made other changes you don't want.

5. Put this in `navbar.mdwn`

        o [[Main|index]]
        o [[Lecture Notes|notes]]
        o [[Student Stuff|students]]
        o [[Code n Git|code]]
        o [[Tips "blog"|tips]]

Oh yeah, also my CSS file only works if you use `html5`.

## Site Title

If you want a site title at the top, and page titles just above the content, do the following:

1. Install and enable the third party plugin [varioki](http://ikiwiki.info/todo/varioki_--_add_template_variables___40__with_closures_for_values__41___in_ikiwiki.setup/) plugin.

2. Edit your setup file:

        # varioki plugin
        varioki:
          sitetitle: "\"Gautam Iyer's Wiki.\""

3. Edit your `page.tmpl`:

        diff --git a/templates/page.tmpl b/templates/page.tmpl
        index 5669d59..2d756ff 100644
        --- a/templates/page.tmpl
        +++ b/templates/page.tmpl
        @@ -56,12 +56,16 @@
         <a href="<TMPL_VAR URL>"><TMPL_VAR PAGE></a>/ 
         </TMPL_LOOP>
         </span>
        +<TMPL_IF SITETITLE>
        +<span class="sitetitle"><TMPL_VAR SITETITLE></span>
        +<TMPL_ELSE>
         <span class="title">
         <TMPL_VAR TITLE>
         <TMPL_IF ISTRANSLATION>
         &nbsp;(<TMPL_VAR PERCENTTRANSLATED>%)
         </TMPL_IF>
         </span>
        +</TMPL_IF>
         </span>
         <TMPL_UNLESS DYNAMIC>
         <TMPL_IF SEARCHFORM>
        @@ -141,6 +145,7 @@
         </TMPL_IF>

         <div id="pagebody">
        +<TMPL_IF SITETITLE><span class='pagetitle'><TMPL_VAR TITLE></span></TMPL_IF>

         <TMPL_IF HTML5><section id="content"><TMPL_ELSE><div id="content"></TMPL_IF>
         <TMPL_VAR CONTENT>''']]

4. Style it:

        /* Extra styles for when sitetitle is enabled. */
        span.parentlinks { display: none; }

        span.sitetitle {
          display: block; 
          font: 144% sans-serif;
          text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.2);
          margin-bottom: .2em;
          margin-top: .2em;
        }

        span.pagetitle {
          display: block; 
          font: 144% sans-serif;
          text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.2);
          /* margin: 1em 2rem; */
          margin: 1em 1.388889em;
        }

## Local modifications

If you want a similar look to [my old wiki](http://wiki.math.cmu.edu/iki/wiki) / use one of my plugins, here are all the browsable sources of this wiki:

* [Content and style files](http://wiki.math.cmu.edu/gitweb-pub/?p=wiki-wiki.git)

* [Plugins](http://wiki.math.cmu.edu/gitweb-pub/?p=ikiwiki-plugins.git)

* [Setup scripts](http://wiki.math.cmu.edu/gitweb-pub/?p=ikiwiki-setup.git)

You can `git clone` them (read only) from here:

    git clone git://wiki.math.cmu.edu/pub/wiki-wiki.git
    git clone git://wiki.math.cmu.edu/pub/ikiwiki-plugins.git
    git clone git://wiki.math.cmu.edu/pub/ikiwiki-setup.git

[ikiWiki]: http://ikiwiki.info/
[git]: http://git-scm.com/
[multimarkdown]: http://fletcherpenney.net/multimarkdown/
