title: Site layout
breadcrumb: /{{dirname}}.md

All the layouts are in the `src/layouts` directory.

## HTML files

base.j2:
: This is the main body is in `base.j2`, with the navbar and footer in `frag/nav.j2` and `frag/footer.j2` directories.
  The main theme is based of the standard Bootstrap example.

jumbotronXY.j2:
: These are the Bootstrap jumbotron examples. Here `X` `Y` are numbers giving the size of the main and the right columns respectively.
  I only regularly use `layouts/jumbotron93.j2`, so can not guarantee completeness of the other jumbotron layouts.

nav-right.j2, nav-left.j2:
: The block `nav_column` from any child template gets put on the right as a navigation column.
  Also if the variable `toc` is set, then the contents of this variable will be used of the table of contents, **provided** it doesn't contain an empty list of the form `<ul></ul>`.

nav-right-affix.j2, nav-left-affix.j2:
: These are based on `nav-left.j2` and `nav-right.j2`. They use the Bootstrap `affix` plugin to make the navigation column stay sticky when you scroll down.

## Markdown files

All the markdown layouts are named in the form `md-XXX.j2`.
They will be documented shortly.
(Use the source, Luke.)
