import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def shuffle_no_self_index(n):
    original_list = list(range(n))
    shuffled_list = []

    while original_list:
        index = random.randint(0, len(original_list) - 1)
        while index == len(shuffled_list):
            index = random.randint(0, len(original_list) - 1)
            
        shuffled_list.append(original_list.pop(index))

    return shuffled_list

def main():
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
    subject = "Secret Santa"

    reciever = shuffle_no_self_index(len(names_mails))

    for i in range(len(names_mails)):
        
        body = "You will buy a gift for : " + names_mails[reciever[i]][0]  +"."

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
