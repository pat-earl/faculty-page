title: Reverse chronological sorting with BibTeX
tags: latex
summary: How to sort references chronologically, reverse chronologically or change the references title.

If you'd like to list your references sorted in reverse chronological order do the following:

* Download [[{{filesdir}}/habbrvyr.bst|this]] bibliography style file and save it in the same directory as your TeX file (or in `~/texmf/bibtex/bst`)

* Include your bibliography as follows:

        \bibliographystyle{habbrvyr}
        \bibliography{refs}

This is most commonly used in CV's. If that's what you're using it for, here are a few other things you might want to do.

## Sorting chronologically

Edit [[{{filesdir}}/habbrvyr.bst|habbrvyr.bst]] and replace ever occurrence of `REVERSE` with `ITERATE`. (See [this thread](http://tex.stackexchange.com/questions/4461/is-there-a-bibtex-style-that-sorts-references-in-reverse-chronological-order) on StackExchange.

## Using different styles.

I looked at the differences  between the `plain.bst` and `plainyr.bst` (which should both be in your standard BibTeX installation), and then adapted the arXiv's [habbrv.bst](http://arxiv.org/hypertex/bibstyles/habbrv.bst). 
A similar trick should work for your your favourite style file.

## Changing the section title.

The references show up in a section called "References". To change the section title, use

    \renewcommand{\refname}{Selected Publications} 
