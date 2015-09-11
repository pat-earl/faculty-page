title: LaTeX headers to maximise space.
tags: latex
summary: A few tricks to save space when writing documents (e.g. NSF proposals) that have **strict** font, margin and page restrictions.

{% raw %}
Here are some LaTeX tips to help save space.
I usually use these tricks when writing NSF proposals as they have **strict** font, margin and page restrictions.

## Setting Margins.

The most reliable way to set margins is using the `geometry` package:

```tex
\usepackage[margin=1.1in]{geometry}
```

For NSF proposals you need 1 inch margins; I usually play it safe and use 1.1 inch margins.

## Adjusting the size of titles.

It's good to structure documents using `\section`, `\subsection`, etc.
However, under the default document classes, the section titles take up too much space.
The package `titlesec` allows you to control this.
To get the smallest titles try this:

```tex
\usepackage[compact,small]{titlesec}
```

If you need further customization look up the `\titlespacing` and `\titleformat` commands.

# Wrapping text around figures.

Using the `figure` environment is a major space hog.
Having the text flow around the figure (like in newspapers) saves a lot of space.
The `wrapfig` package helps with this.
First put

```tex
\usepackage{wrapfig}
```

in your preamble.
Now include your figure with:

```tex
\begin{wrapfigure}{r}{5.5\baselineskip}
  \vspace{-1.7\baselineskip}% Squeeze space before.
  \begin{center}
    \includegraphics[width=\linewidth]{figurename}
  \end{center}
  \vspace{-2\baselineskip}% Squeeze space after.
\end{wrapfigure}
Paragraph text goes here. It has to be longer than one line, and it can not
be in the middle of a list.
```

## Fractional Point Font Sizes.

NSF requires proposals to have a minimum of a 11 point font.
If 12 point is too big for you, and 11 point is too small (or you just want to play it safe), then you can use a fractional point size.
Getting a fractional point size font working correctly is a little tricky.
Adjust the parameters `\normalFontSize` and `\fontSizeIncrement` below.

```tex
\usepackage{type1cm}
\newlength\normalFontSize\newlength\fontSizeIncrement
\setlength\normalFontSize{11.20pt}% Recommend starting with 11.5
\setlength\fontSizeIncrement{1.5pt}

% Compute the rest from the normal font size and increment
%{{{
\makeatletter
\newlength\normalFontSkip\setlength\normalFontSkip{1.2\normalFontSize}
% To use arbitrary font sizes.
%
%   1. \usepackage{type1cm}
%   2. kpsewhich size11.clo (replace 11 with 10/12 if you use a 10/12pt default
%      font).
%   3. Cut and paste the font definitions from there to here. Surround with
%      \makeatletter, \makeatother if in a .tex file.
%   4. Replace the first argument following the font size with your desired
%      size. Replace the second argument with 1.2 times the first argument.
\renewcommand\normalsize{%
   \@setfontsize\normalsize{\normalFontSize}{\normalFontSkip}%
   %\abovedisplayskip 11\p@ \@plus3\p@ \@minus6\p@
   \abovedisplayskip 4\p@ \@plus3\p@ \@minus3\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip \z@ \@plus3\p@
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}
\normalsize

\newlength\smallFontSize\newlength\smallFontSkip
\setlength\smallFontSize\normalFontSize
\addtolength\smallFontSize{-1\fontSizeIncrement}
\setlength\smallFontSkip{1.2\smallFontSize}
\renewcommand\small{%
   \@setfontsize\small{\smallFontSize}{\smallFontSkip}
   \abovedisplayskip 10\p@ \@plus2\p@ \@minus5\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6\p@ \@plus3\p@ \@minus3\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 6\p@ \@plus2\p@ \@minus2\p@
               \parsep 3\p@ \@plus2\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
}

\newlength\footnoteFontSize\newlength\footnoteFontSkip
\setlength\footnoteFontSize\normalFontSize
\addtolength\footnoteFontSize{-1.75\fontSizeIncrement}
\setlength\footnoteFontSkip{1.2\footnoteFontSize}
\renewcommand\footnotesize{%
   \@setfontsize\footnotesize\footnoteFontSize\footnoteFontSkip%
   \abovedisplayskip 8\p@ \@plus2\p@ \@minus4\p@
   \abovedisplayshortskip \z@ \@plus\p@
   \belowdisplayshortskip 4\p@ \@plus2\p@ \@minus2\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 4\p@ \@plus2\p@ \@minus2\p@
               \parsep 2\p@ \@plus\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
}

\newlength\scriptFontSize\newlength\scriptFontSkip
\setlength\scriptFontSize\normalFontSize
\addtolength\scriptFontSize{-2.5\fontSizeIncrement}
\setlength\scriptFontSkip{1.2\scriptFontSize}
\renewcommand\scriptsize{\@setfontsize\scriptsize\scriptFontSize\scriptFontSkip}

\newlength\tinyFontSize\newlength\tinyFontSkip
\setlength\tinyFontSize\normalFontSize
\addtolength\tinyFontSize{-3\fontSizeIncrement}
\setlength\tinyFontSkip{1.2\tinyFontSize}
\renewcommand\tiny{\@setfontsize\tiny\tinyFontSize\tinyFontSkip}

\newlength\largeFontSize\newlength\largeFontSkip
\setlength\largeFontSize\normalFontSize
\addtolength\largeFontSize{1\fontSizeIncrement}
\setlength\largeFontSkip{1.2\largeFontSize}
\renewcommand\large{\@setfontsize\large\largeFontSize\largeFontSkip}

\newlength\LargeFontSize\newlength\LargeFontSkip
\setlength\LargeFontSize\normalFontSize
\addtolength\LargeFontSize{2\fontSizeIncrement}
\setlength\LargeFontSkip{1.2\LargeFontSize}
\renewcommand\Large{\@setfontsize\Large\LargeFontSize\LargeFontSkip}

\newlength\LARGEFontSize\newlength\LARGEFontSkip
\setlength\LARGEFontSize\normalFontSize
\addtolength\LARGEFontSize{3\fontSizeIncrement}
\setlength\LARGEFontSkip{1.2\LARGEFontSize}
\renewcommand\LARGE{\@setfontsize\LARGE\LARGEFontSize\LARGEFontSkip}

\newlength\hugeFontSize\newlength\hugeFontSkip
\setlength\hugeFontSize\normalFontSize
\addtolength\hugeFontSize{4\fontSizeIncrement}
\setlength\hugeFontSkip{1.2\hugeFontSize}
\renewcommand\huge{\@setfontsize\huge\hugeFontSize\hugeFontSkip}

\newlength\HugeFontSize\newlength\HugeFontSkip
\setlength\HugeFontSize\normalFontSize
\addtolength\HugeFontSize{5\fontSizeIncrement}
\setlength\HugeFontSkip{1.2\HugeFontSize}
\renewcommand\Huge{\@setfontsize\Huge\HugeFontSize\HugeFontSkip}
\makeatother
%}}}
```
{% endraw %}
