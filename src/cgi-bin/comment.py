#! /usr/bin/python3
import cgi
import os, time, hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

form = cgi.FieldStorage()
dev_env = "{{dev_env}}"

print( "Content-type: text/plain;\n" )

email_address = form.getvalue('email', 'unknown@email.id').strip()
page = form.getvalue( 'page', 'error-no-page' ).strip()
subject = form.getvalue( 'subject', 'Error: No subject' ).strip()
name = form.getvalue( 'name', 'Anonymous' ).strip()
date = time.strftime( '%F %T %Z' )
ip = os.environ.get( 'REMOTE_ADDR', 'Unknown' )
referer = os.environ.get( 'HTTP_REFERER', 'Unknown' )
comment = form.getvalue( 'comment', 'No comment' ).strip()
num = int( form.getvalue( 'comment-number', 1 ) )

# Build the email.
msg = MIMEMultipart()
msg['Subject'] = '[comment %s] %s' % (page, subject)
msg['To'] = '{{site_email}}'
msg['From'] = '%s <%s>' % (name, email_address)
msg.preamble = 'A comment was posted to page %s on %s' % (page, date)

msg.attach( MIMEText( msg.preamble ) )

attach = MIMEText( """\
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
        hashlib.md5( email_address.lower().encode( errors='replace' ) ) \
                .hexdigest(),
        date, ip, referer, comment),
    _charset='utf-8'
)
attach['Content-Disposition'] = 'attachment; filename="_%s_%02d.md"' % \
        ( os.path.splitext(page)[0], num )
msg.attach( attach )

s = smtplib.SMTP('{{site_smtp}}')
print( s.sendmail( msg['To'], msg['To'], msg.as_string() ) or "OK" )
s.close()
