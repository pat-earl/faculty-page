title: Various Miscalaneous Tests in Markdown
layout: md-nav-right.j2

## Filename and includes

``` yaml
title       : {{title}}
dirname     : {{dirname|e}}
basename    : {{basename|e}}
name        : {{name|e}}
1 + 1       : {{1 + 1}}
```

## WikiLinks

* `auth/test`: [[auth/test]]
* `test`: [[test]]
* `/test`: [[/test]]
* `test.md`: [[test.md]]

## Glob

{% for f in glob( dirname ~ '/[0-9a-zA-Z]*.md') | sort -%}
* [[/{{f}}|{{meta( f, 'title' ) }}]]
{% endfor %}
