from email.message import EmailMessage
import smtplib
import os

def send_email(message,src,destination):
    # important, you need to send it to a server that knows how to send e-mails for you
    server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
    #server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    # don't know how to do it without cleartexting the password and not relying on some json file that you dont git control...
    server.login('AKIAVEE3CB3IVEBQYRUS','BG4DFQS6nNnM9l7kIzkm4vfktPc7JvvkFsQJ9eHC0phE')
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'TEST'
    msg['From'] = 'admin@handymia.com'
    msg['To'] = destination
    text = msg.as_string()
    server.send_message(msg,src,destination)

if __name__ == '__main__':
    send_email('test msg 1','admin@handymia.com','lmarin@hotmail.com')
