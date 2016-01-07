title: LaTeX forward/inverse searches with Zathura
tags: linux, latex
summary: I use [zathura](http://pwmt.org/projects/zathura/) to view PDF files. As of version 0.2.7 it supports full forward / inverse searches with LaTeX. Namely, you can "control click" in any place on the PDF file, and it will open the TeX source file in your editor, and move to the corresponding location. Conversely, you can configure your editor so that pressing a particular key when editing your TeX file will open the PDF file and highlight the corresponding location.

{{summary}}

## General usage

While doing this with zathura is possible, the documentation *SUCKS*.
Here's how: Edit `~/.config/zathura/zathurarc` and add the following lines:

    set synctex true
    set synctex-editor-command "gvim +%{line} %{input}"

This only works on recent versions (0.3.4 or higher).
Older versions require this to be given direction on the command line using `-x` (or `-s`).

If you you want to highlight line 193 column 1, then use:

    zathura --synctex-forward 193:1:paper.tex paper.pdf

If you control click in the PDF, it will take you to the corresponding location in your `LaTeX` file by running your editor.
It will, however, open a **new instance** of the editor every time you control click. This is obviously less than ideal, and the scripts below can help out.

## Use with FVWM and VIM

If you use [vim] as your text editor and [fvwm] as your window manager, I wrote two scripts to get rid of all sorts of quirks (e.g. opening the file twice in different windows, not raising / focussing the PDF files, etc.):

1. Save [this script](http://wiki.math.cmu.edu/gitweb-pub/?p=bash-scripts.git;a=blob_plain;f=szathura.sh;hb=HEAD) as `szathura` somewhere in your `PATH`.
   (If you're not using [fvwm] as your window manager, then comment out the [fvwm] specific stuff.)

2. Save [this script](http://wiki.math.cmu.edu/gitweb-pub/?p=bash-scripts.git;a=blob_plain;f=svim.sh;hb=HEAD) as `svim` somewhere in your `PATH`.
   (Again, if you're not using [fvwm] as your window manager, then comment out the [fvwm] specific stuff.)

3. Edit `~/.config/zathura/zathurarc` and add the lines:

        set synctex true
        set synctex-editor-command "svim -G +%{line} %{input}"

4. Be sure you have the option `-synctex=1` when you run `LaTeX`, otherwise **NOTHING WILL WORK**.
   If you're running `LaTeX` through [vim], add this option to your `&makeprg`.
   If you're using `latexmk`, then edit `~/.latexmkrc` and add the lines:

        $pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
        $pdf_mode = 1;

5. Edit `~/.vimrc` and add the lines:

        nnoremap <F9>
            \ :exec "!szathura %:r.pdf" line('.')  col('.') "% > /dev/null"<cr><cr>
        nnoremap <C-F9>
            \ :exec "!szathura %:r.pdf" > /dev/null 2>&1 &"<cr><cr>

    (Alternately, add them to `~/.vim/after/ftplugin/tex.vim` with other fancy buffer local mappings.)

Now to use it:

1. Edit your file with `svim -G file.tex`.

2. Control click the PDF to go back to the TeX file.
   A new window will be opened if you're not already editing it.

3. Press `F9` in `vim` to highlight the corresponding location in the PDF file and raise the window (a new window will be opened if you're not already viewing it).

4. Press `<Ctrl-F9>` in `vim` to open a new window showing the PDF in case you want multiple views.


[zathura]: http://pwmt.org/projects/zathura/
[vim]: http://www.vim.org
[fvwm]: http://fvwm.org
