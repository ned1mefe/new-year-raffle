import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

names_mails = [
    ("Ayça", "ayca.ece.arsln@gmail.com"),
    ("Arda", "ardayungucu48@gmail.com"),
    ("Cenk", "cengizcenkkerem@gmail.com"),
    ("Efe", "efe.candas@metu.edu.tr"),
    ("Sude", "badur.sude@gmail.com"),
    ("Selin", "selin.basar@metu.edu.tr"),
    ("İbo", "erturk.emre@metu.edu.tr")
]

smtp_server = 'mailhost.ceng.metu.edu.tr'
smtp_port = 587
smtp_username = input("Enter username: ")
smtp_password = input("Enter password: ")

from_mail = "e2521326@ceng.metu.edu.tr"
subject = "Yılbaşı Çekilişi"

reciever = list(range(len(names_mails)))

satisfied = False

while(not satisfied):
    random.shuffle(reciever)

    satisfied = True
    for i in range(len(reciever)):
        if (i == reciever[i]):
            satisfied = False    


for i in range(len(names_mails)):
    
    body = "Bu yılbaşında alacağın kişi : " + names_mails[reciever[i]][0]  +"."

    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = names_mails[i][1]
    msg['Subject'] = subject
    msg.attach(MIMEText(body))


    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)
