#! /bin/bash
# Created   : Wed 17 Aug 2016 10:15:34 AM EDT
# Modified  : Wed 17 Aug 2016 10:17:13 AM EDT
# Author    : GI <a@b.c>, where a='gi1242+sh', b='gmail', c='com'

# Run this when pygments is upgraded

pygmentize -S ${1:-default} -f html | \
    sed -e 's/^\./.codehilite ./g' > src/share/css/pygments-theme.css
