#!/usr/bin/python

import smtplib

sender = 'shy.vijay@gmail.com'
receivers = ['shy.vijay@yahoo.com']

message = """From: From Person <shy.vijay@gmail.com>
To: To Person <shy.vijay@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
 smtpObj = smtplib.SMTP('localhost')
 smtpObj.sendmail(sender, receivers, message)
 print("Successfully sent email")
except smtplib.SMTPException:
 print("Error: unable to send email")
