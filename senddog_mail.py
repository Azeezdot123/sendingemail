import os
import smtplib
import requests
from email.message import EmailMessage

dog_info = requests.get("https://api.thedogapi.com/v1/images/search").json()[0]
dog_url = dog_info['url']
dog_breed = dog_info['breeds']
dog_list = dog_breed[0]

if dog_list:
    dog_name = dog_list['name']
    dog_lifespan = dog_list['life_span']
    dog_tem = dog_list['temperament']
    dog_bred = dog_list['bred_for']


EMAIL_ADDRESS = "devolamilekan@gmail.com"
EMAIL_PASSWORD = "qfbducqlcpwjsbpo"

msg = EmailMessage()
msg['Subject'] = "About Dog"
msg["From"] = EMAIL_ADDRESS
msg['To'] = ['headofstate123@gmail.com']

msg.set_content(f"{dog_url}\n The name of the bred is {dog_name}. it has a life span of {dog_lifespan}.\n The temperament of the dog is {dog_tem}.\n it is also breed for {dog_bred}")
msg.add_alternative(f'\n<img src="{dog_url}" width="300px">\n<br/> The name of the bred is <strong>{dog_name}</strong>. it has a life span of <strong>{dog_lifespan}</strong>.\n The temperament of the dog is <strong>{dog_tem}</strong>.\n it is also breed for <strong>{dog_bred}</strong>', subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)