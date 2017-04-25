#! /usr/bin/python
#coding=utf-8
import sys
import smtplib
import socks
from email.mime.text import MIMEText
from email.header import Header

to_addr = sys.argv[1]
subject = sys.argv[2]
msg = sys.argv[3]


#socks.setdefaultproxy(TYPE, ADDR, PORT)
socks.setdefaultproxy(socks.HTTP, 'proxy_server', proxy_port)
socks.wrapmodule(smtplib)

smtpserver = 'smtp.139.com'
smtppass = 'XXXXX'

from_addr = 'XXXXX@139.com'

message = MIMEText(msg, 'plain', 'utf-8')
message['From'] = 'test <%s>' % from_addr
message['To'] =  to_addr
message['Subject'] = Header(subject, 'utf-8').encode()

server = smtplib.SMTP(smtpserver,25)
server.set_debuglevel(1)
server.login(from_addr,smtppass)
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()

