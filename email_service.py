import smtplib
from email.mime.text import MIMEText

from config import Config


def send_email(to, subject, html):
    msg = MIMEText(html, "html")
    msg["Subject"] = subject
    msg["From"] = Config.OWNER_EMAIL
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            Config.OWNER_EMAIL,
            Config.APP_PASSWORD
        )
        server.send_message(msg)