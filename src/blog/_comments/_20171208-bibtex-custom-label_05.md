page: 20171208-bibtex-custom-label.md
subject: Wide labels
name: Anonymous
email: unknown@email.id
avatar: http://cdn.libravatar.org/avatar/99daad327e93a79b9b1a785c70649146
date: 2019-10-30 07:05:41 EDT
ip: 89.3.3.106
referer: http://www.math.cmu.edu/~gautam/sj/blog/20171208-bibtex-custom-label.html

Wide labels creep into the text (similarly to [stackexchange](https://tex.stackexchange.com/questions/2659/fixing-the-bibliography-key-margin-when-using-amsalpha)), this can be manually fixed (as shown on tex.stackexchange) using

    {% raw -%}
    :::latex
    \let\stdthebibliography\thebibliography
    \let\stdendthebibliography\endthebibliography
    \renewenvironment*{thebibliography}[1]{%
      \stdthebibliography{WideLabel99}}
      {\stdendthebibliography}
    {%- endraw %}

repaying `WideLabel99` with a suitably wide label.
