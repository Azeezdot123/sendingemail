import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "devolamilekan@gmail.com"
EMAIL_PASSWORD = "qfbducqlcpwjsbpo"

msg = EmailMessage()
msg['Subject'] = "Automating with python"
msg["From"] = EMAIL_ADDRESS
msg['To'] = ['headofstate123@gmail.com']

msg.set_content("This is a python automated email generated by ola\n i will be happy if you reply back")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)