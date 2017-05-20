#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


mail_host="SMTP_ADDRESS"  # SMTP server address
mail_user="ACCOUNT"    # account
mail_pass="PASSWORD"   # password


sender = 'secret_sender@xxx.xxx'  # single email address
receivers = ['XXXXX@gmail.com', 'OOOOO@gmail.com']  # can be a list of email addresses

message = MIMEText('Can you guess who I am?\nNo you cannot\nBecause I am a spammer who knows code', 'plain', 'utf-8')    # email content goes here

message['from'] = Header("secret_origin@xxx.xxx")
# message['from'] = Header("xxx", 'utf-8')  # this will become xxx@smtps.ntu.edu.tw
message['to'] = Header(receivers[0])
# message['to'] =  Header("testReceiver@example.com")  # this can be anything you want
# message['reply-to'] = Header("b04901117@ntu.edu.tw")  # sets the reply-to address


subject = 'Evil evil spam'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP_SSL()  # NTU mail requires SSL connection
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Email sent!"
except smtplib.SMTPException:
    print "Error: email not sent."