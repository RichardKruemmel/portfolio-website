from flask_mail import Message
from app import app
from app import mail

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)

def send_contact_email(user):
    send_email('[Portfolio Website] New Contact Request',
               sender=[user.email],
               recipients=app.config['ADMINS'][0],
               text_body=[user.text])