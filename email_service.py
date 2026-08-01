import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import Config


def send_email(to_email, subject, html_body):

    if not Config.OWNER_EMAIL:
        raise ValueError("OWNER_EMAIL is not configured")

    if not Config.APP_PASSWORD:
        raise ValueError("APP_PASSWORD is not configured")

    message = MIMEMultipart("alternative")

    message["From"] = Config.OWNER_EMAIL
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(
        MIMEText(
            html_body,
            "html"
        )
    )

    with smtplib.SMTP(
        "smtp.gmail.com",
        587,
        timeout=30
    ) as server:

        server.starttls()

        server.login(
            Config.OWNER_EMAIL,
            Config.APP_PASSWORD
        )

        server.sendmail(
            Config.OWNER_EMAIL,
            to_email,
            message.as_string()
        )
