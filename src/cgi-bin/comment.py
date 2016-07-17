#! /usr/bin/python
import cgi
import os
import time
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def utf_strip( s ):
    return unicode( s, 'utf-8', 'replace' ).strip()

form = cgi.FieldStorage()
dev_env = "{{dev_env}}"

print "Content-type: text/plain;\n"

email_address = utf_strip( form.getvalue('email') or 'unknown@email.id')
page = utf_strip( form.getvalue( 'page' ))
subject = utf_strip( form.getvalue( 'subject' ) )
name = utf_strip( form.getvalue( 'name' ) or 'Anonymous' )
date = time.strftime( '%F %T %Z' )
ip = os.environ.get( 'REMOTE_ADDR' )
referer = os.environ.get( 'HTTP_REFERER' )
comment = utf_strip( form.getvalue( 'comment' ) or "No comment" )
num = int( form.getvalue( 'comment-number' ) or 1 )

# Build the email.
msg = MIMEMultipart()
msg['Subject'] = '[comment %s] %s' % (page, subject)
msg['To'] = '{{site_email}}'
msg['From'] = '%s <%s>' % (name, email_address)
msg.preamble = 'A comment was posted to page %s on %s' % (page, date)

msg.attach( MIMEText( msg.preamble ) )

attach = MIMEText( u"""\
page: %s
subject: %s
name: %s
email: %s
avatar: http://cdn.libravatar.org/avatar/%s
date: %s
ip: %s
referer: %s

%s
""" % ( page, subject, name, email_address, 
        hashlib.md5( email_address.lower() ).hexdigest(),
        date, ip, referer, comment),
    _charset='utf-8'
)
attach['Content-Disposition'] = 'attachment; filename="_%s_%02d.md"' % \
        ( os.path.splitext(page)[0], num )
msg.attach( attach )

s = smtplib.SMTP('{{site_smtp}}')
print s.sendmail( msg['To'], msg['To'], msg.as_string() ) or "OK"
s.close()
