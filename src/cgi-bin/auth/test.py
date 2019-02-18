#! /usr/bin/python3

import cgitb; cgitb.enable()

import cgi, os, sys, csv

print( "Content-type: text/plain;\n" )

# Print values
print( 'Query: {}\n\n'.format( os.environ.get( 'QUERY_STRING', 'None' ) ) )

print( 'CGI Fields:' )
form = cgi.FieldStorage()
for k in form.keys():
    print( '{}: {}'.format( k, form.getvalue(k) ) )

# Print environment (text)
print( '\n\nEnvironment:' )
for k, v in os.environ.items():
    print( '{}: {}'.format(k, v) )

