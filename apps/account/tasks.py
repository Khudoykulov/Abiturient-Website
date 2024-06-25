# from config.celery import app
# from django.core.mail import send_mail
# import os
# from django.contrib.auth import get_user_model
from config.celery import app
from django.core.mail import send_mail
import os


@app.task(bind=True)
def crm_send_email(self, subject, message, recipient_list, *args, **kwargs):
    from_email = os.getenv('EMAIL_HOST_USER')
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    return f'yuborildi'


@app.task(bind=True)
def send_mail_func(self, subject, message, recipient_list, *args, **kwargs):
    from_email = os.getenv('EMAIL_HOST_USER')
    send_mail(subject=subject,
              message=message,
              from_email=from_email,
              recipient_list=recipient_list,
              )
    return "Sent"
