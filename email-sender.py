#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


mail_host="smtps.ntu.edu.tw"  # sample SMTP server address
mail_user="ACCOUNT"    # account
mail_pass="PASSWORD"   # password


sender = 'XXXX@ntu.edu.tw'  # single email address
receivers = ['OOOO@ntu.edu.tw']  # can be a list of email addresses

message = MIMEText('信件內容寫在這！\n換行還要這樣。', 'plain', 'utf-8')    # email content goes here

from_addr = formataddr((str(Header('SENDER_NAME', 'utf-8')), "SENDER_EMAIL"))
message['from'] = from_addr
# message['from'] = Header("xxx", 'utf-8')  # this will become xxx@smtps.ntu.edu.tw
message['to'] = Header(receivers[0])
# message['to'] =  Header("testReceiver@example.com")  # this can be anything you want. same format applies to 'from' header
# message['reply-to'] = Header("b04901117@ntu.edu.tw")  # sets the reply-to address


subject = '標題'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP_SSL()  # NTU mail requires SSL connection
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Email sent!"
except smtplib.SMTPException:
    print "Error: email not sent."