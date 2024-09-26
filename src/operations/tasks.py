import smtplib
import time

from celery_init import celery
from email.message import EmailMessage

from config import settings

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Отчет'
    email['From'] = settings.SMTP_USER
    email['To'] = settings.SMTP_USER
    email.set_content(f"HI!, {username}")
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(email)
