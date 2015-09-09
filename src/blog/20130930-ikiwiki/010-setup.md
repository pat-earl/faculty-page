title: Setup Instructions
breadcrumb: /{{dirname}}.md

# Installation.

On Debian based systems (includes Ubuntu) install the following packages:

    libhighlight-perl libtext-multimarkdown-perl ikiwiki

Then setup your wiki by running:

    ikiwiki --setup /etc/ikiwiki/auto.setup

For more details look at the tutorial [here](http://ikiwiki.info/setup/).

# Getting MathJAX working.

First be sure you're using MultiMarkDown and not Markdown; Markdown attempts to render math itself, and does a terrible job.
Add the following to your setup file.

    multimarkdown: 1

To display math using MathJAX you need to link to the MathJAX script *from every single page* that displays math.
There doesn't seem to be an easy way to automate this.
Here are your options.

## Using a plugin to load MathJAX

So far this seems to be the safest and simplest option.

1. Download the [[files/mathjax.pm|mathjax plugin]] and save it as in `IkiWiki/Plugin/mathjax.pm` in your `libdir`.
   You might also need to `chmod -a+x` the file.

2. Include the directive `[[!mathjax]]` on any page that you want to use MathJAX.
   This will add a link to the MathJAX script from a CDN.
   (If your wiki's baseurl is an `https` URL, then this plugin will use an https CDN; if not, it will use the regular http CDN.)

3. If you you want to include custom macros, or customize settings (e.g. enabling inline math via \$ ... \$), then create a file called `/javascript/mathjax-config.js`.
   Put all your config/macros here as follows:

        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [ ['$','$'], ['\\(', '\\)']  ]
            },
            TeX: {
                TagSide: "right",
                equationNumbers: {autoNumber: "AMS"},
                Macros: {
                    // Add your macros here. Here are some examples.
                    eps:        '\\varepsilon',
                    cosec:      '\\operatorname{cosec}',
                    abs:        [ '\\left\\lvert#1\\right\\rvert', 1 ],
                    paren:      [ '#1(#2#1)', 2, '' ]
                }
            }
        });

    If you want to use a different config file, pass the name via the `config` parameter.
   For example, do

        [[!mathjax config="/javascript/myconfig"]]

    if you save your macros in the `javascript` subdirectory.
   (If this file is not found, an error will be printed and no macro file will be used. Also this file has to be locally served; you can't use this to load external scripts.)

    **Note:**
   Only one macro file per page will ever be used.
   Thus if you inline two pages each sourcing a different macro file, then only the last macro file sourced will be included.

That's it.
If everything is setup right, typing `$E=mc^2$` into some Wiki page should produce $E=mc^2$.

## Disabling htmlscrubber and inlining a page that loads MathJAX

<div class='alert alert-warning' markdown='1'>
**WARNING:**
This method requires you to disable the [htmlscrubber](http://ikiwiki.info/plugins/htmlscrubber/) plugin, which is a security risk.
</div>

1. Disable the `htmlscrubber` plugin, otherwise your MathJAX inclusions will be ignored.
   Edit your setup file file and uncomment the following line:

        htmlscrubber_skip: '!*/Discussion'

2. Create a `mathjax.html` file in the root of your wiki directory with the
   following:

        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [ ['$','$'], ['\\(', '\\)']  ]
            },
            TeX: {
              TagSide: "right",
              equationNumbers: {autoNumber: "AMS"},
              Macros: {
                // Add your macros here. Here are some examples.
                eps:        '\\varepsilon',
                cosec:      '\\operatorname{cosec}',
                abs:        [ '\\left\\lvert#1\\right\\rvert', 1 ],
                paren:      [ '#1(#2#1)', 2, '' ]
              }
            }
          });
        </script>
        <!-- <script src="https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" type="text/javascript"></script> -->
        <script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" type="text/javascript"></script>

    If you're using https to serve your wiki, then you need the https MathJAX CDN above.
   If not, the http one will be (marginally) faster.

3. In any page that you want to display math, put the following line at the top:

        [[!inline pagenames="mathjax.html" raw="yes" ]]

That's it.
If everything is setup right, typing `$E=mc^2$` into some Wiki page should produce $E=mc^2$.

## Other possibilities.

I haven't tried these possibilities; but they should (in theory) work.

### Serving MathJAX locally and using the meta plugin.

If you serve MathJAX locally (as part of your wiki), then you can use the [meta directive](http://ikiwiki.info/ikiwiki/directive/meta/) to include this script in pages that have math.
Note the `script` attribute will only accept scripts that ikiwiki can find locally, so you can not use this method to use a CDN to deliver MathJAX.

### Creating a custom template.

The default template seems to be `page.tmpl`
Copy this to a file `mathjax.tmpl` (in the templates directory) and edit it to include a link to the MathJAX CDN.
Now on pages you want to use MathJAX use the [pagetemplate](http://ikiwiki.info/plugins/pagetemplate/) plugin to render them using the `mathjax.tmpl` template.
