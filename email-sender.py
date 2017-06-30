#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# remember to change your computer name too!

mail_host = "smtps.ntu.edu.tw"  # sample SMTP server address
mail_user = "USERNAME"    # account
mail_pass = "PASSWORD"   # password

message = MIMEText('嵩仁同學，\n\n祝你生日快樂。可是毛同學比你帥。\n不用回我信了。\n\nBest wishes,\n世偉', 'plain', 'utf-8')    # email content goes here
subject = '黃同學，blah blah blah'
message['Subject'] = Header(subject, 'utf-8')

sender = 'liao@csie.ntu.edu.tw'  # single email address
from_addr = formataddr((str(Header('廖世偉', 'utf-8')), "liao@csie.ntu.edu.tw"))
message['from'] = from_addr
# message['from'] = Header("xxx", 'utf-8')  # this will become xxx@smtps.ntu.edu.tw

cc = ['b04902099@ntu.edu.tw']  # can be a list of email addresses
bcc = ['b04901117@ntu.edu.tw', 'ccm29cam@gmail.com'] # other people won't know this person received email
message['to'] = Header(','.join(cc)) # header is a comma-separated string
receivers = cc + bcc
message['reply-to'] = Header("b04901117@ntu.edu.tw")  # sets the reply-to address



try:
    smtpObj = smtplib.SMTP_SSL()  # NTU mail requires SSL connection
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Email sent!"
except smtplib.SMTPException:
    print "Error: email not sent."