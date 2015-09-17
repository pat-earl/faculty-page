#! /usr/bin/python
import cgi
import os
import time
import hashlib
import email
import smtplib

form = cgi.FieldStorage()
dev_env = "{{dev_env}}"

print "Content-type: text/plain;\n"

email_address = unicode( form.getvalue('email') ).strip()

body = """\
page: %s
subject: %s
name: %s
email: %s
avatar: http://cdn.libravatar.org/avatar/%s
date: %s
ip: %s
referer: %s

%s
""" % (
        unicode( form.getvalue( 'page' ) ),
        unicode( form.getvalue( 'subject' ) ).strip(),
        unicode( form.getvalue( 'name' ) ) or 'Anonymous',
        email_address,
        hashlib.md5( email_address.lower() ).hexdigest(),
        time.strftime( '%F %T %Z' ),
        os.environ.get( 'HTTP_ADDR' ),
        os.environ.get( 'HTTP_REFERER' ),
        unicode( form.getvalue( 'comment' ) ).strip(),
    )

s = smtplib.
email.message_from_string( body, 

if dev_env == 'local':
    print body
    
#cgi.print_environ()
#cgi.print_environ_usage()
#cgi.print_form( form )

print( "</body></html>" )
