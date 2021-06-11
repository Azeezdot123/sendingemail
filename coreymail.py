import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "devolamilekan@gmail.com"
EMAIL_PASSWORD = "qfbducqlcpwjsbpo"

msg = EmailMessage()
msg['Subject'] = "HTML mail imager"
msg["From"] = EMAIL_ADDRESS
msg['To'] = ['headofstate123@gmail.com']



# image
# msg.set_content("Image Attached")
# with open('z.jpg', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name

# msg.add_attachment(file_data, maintype='image', subtype='file_type', filename='file_name')

# sending pdf 
# msg.set_content("Image Attached")
# files = ['az.pdf']
# for file in files:
#     with open('z.jpg', 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
#     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='file_name')

# html mail

msg.set_content("this is a plain html mail")
msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
    <body>
    <h1 style="color:SlateGray;">This is an HTML Email made by olamilekan!</h1>
    <br/>
    <img src="{path}">
    </body>
    </html>
""", subtype="html")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



