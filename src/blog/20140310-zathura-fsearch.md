title: LaTeX forward/inverse searches with Zathura
tags: linux, latex
summary: I use [zathura](http://pwmt.org/projects/zathura/) to view PDF files. As of version 0.2.7 it supports full forward / inverse searches with LaTeX. Namely, you can "control click" in any place on the PDF file, and it will open the TeX source file in your editor, and move to the corresponding location. Conversely, you can configure your editor so that pressing a particular key when editing your TeX file will open the PDF file and highlight the corresponding location.

{{summary}}

## General usage

While doing this with zathura is possible, the documentation *SUCKS*.
Here's how: To open a PDF in zathura and tell it what your editor is use:

    zathura -s -x 'gvim +%{line} %{input}' paper.pdf

If the PDF is already open, and you want to highlight line 193 column 1, then use:

    zathura --synctex-forward 193:1:paper.tex paper.pdf

## Use with FVWM and VIM

If you use [vim](http://www.vim.org) as your text editor and [fvwm](http://fvwm.org) as your window manager, heres how you can get rid of all sorts of quirks (e.g. opening the file twice in different windows, not raising / focussing the PDF files, etc.):

1. Save [this script](http://wiki.math.cmu.edu/gitweb-pub/?p=bash-scripts.git;a=blob_plain;f=szathura.sh;hb=HEAD) as `szathura` somewhere in your PATH.

2. Save [this script](http://wiki.math.cmu.edu/gitweb-pub/?p=bash-scripts.git;a=blob_plain;f=svim.sh;hb=HEAD) as `svim` somewhere in your PATH.

3. Put

	    nnoremap <F9>	:exec "!szathura %:r.pdf" line('.')  col('.') "% > /dev/null"<cr><cr>

    in your `~/.vimrc`.

4. Edit your file with `svim -G file.tex`.
   Control click the PDF to go back to the TeX file (a new window will be opened if you're not already editing it).
   Press `F9` in `vim` to highlight the corresponding location in the PDF file and raise the window (a new window will be opened if you're not already viewing it).

If you're not using fvwm as your window manager, then comment out the fvwm specific stuff in both those scripts.


[zathura]: http://pwmt.org/projects/zathura/

