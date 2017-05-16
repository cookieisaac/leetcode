#!/usr/bin/python
# Send email via personal gmail
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello World!")
me = "me@gmail.com"
my_password = "password"
you = "you@gmail.com"

msg['Subject'] = 'Test Email'
msg['From'] = me
msg['To'] = you

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

server.login(me, my_password)
server.sendmail(me, [you], msg.as_string())
server.quit()