import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def main():
    names_mails = [
        ("isim1", "isim1@gmail.com"),
        ("isim2", "isim1@gmail.com"),
        ("isim3", "isim1@gmail.com"),
        ("isim4", "isim1@gmail.com"),
    ]

    smtp_server = 'mailhost.ceng.metu.edu.tr'
    smtp_port = 587
    smtp_username = input("Enter username: ")
    smtp_password = input("Enter password: ")

    from_mail = "e2521326@ceng.metu.edu.tr"
    subject = "Secret Santa"

    random.shuffle(names_mails)

    for i in range(len(names_mails)):
        
        index = 0 if i == len(names_mails) - 1 else i + 1

        body = "Hediyeni " +  names_mails[index][0]  +"'ya alacaksın."

        msg = MIMEMultipart()
        msg['From'] = from_mail
        msg['To'] = names_mails[i][1]
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(msg)

if __name__ == "__main__":
    main()
