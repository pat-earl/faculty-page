#!/bin/bash

# Make sure you put the following in ~/.netrc
# machine faculty.kutztown.edu
# login <username>
# password <password>

lftp faculty.kutztown.edu <<EOF
set ftp:ssl-protect-data true
set ftp:ssl-force true
set ssl:verify-certificate no
mirror -R -e -n -P=4 ./out-prod /
quit
EOF