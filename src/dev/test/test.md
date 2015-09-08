title: Various Miscalaneous Tests in Markdown
layout: md-nav-right.j2

## Filename and includes

``` yaml
title       : {{title}}
dirname     : {{dirname|e}}
basename    : {{basename|e}}
name        : {{name}}
name[:-3]   : {{name[:-3]}}
1 + 1       : {{1 + 1}}
```

## WikiLinks

* `auth/test`: [[auth/test]]
* `test`: [[test]]
* `/test`: [[/test]]
* `test.md`: [[test.md]]

## Glob

{% for f in glob( '*.md') | sort -%}
* [[{{f}}|{{get_meta( f, 'title' )|default(f, true) }}]]
{% endfor %}

### Filtering tests

* {{ glob( '*.md' ) | search( '^_' ) }}
