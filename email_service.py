def send_email(to_email, subject, html_body):

    try:
        print("EMAIL STEP 1: Checking environment variables")

        if not Config.OWNER_EMAIL:
            raise ValueError("OWNER_EMAIL is not configured")

        if not Config.APP_PASSWORD:
            raise ValueError("APP_PASSWORD is not configured")

        print("EMAIL STEP 2: Environment variables exist")
        print("EMAIL SENDER:", Config.OWNER_EMAIL)
        print("EMAIL RECIPIENT:", to_email)

        message = MIMEMultipart("alternative")

        message["From"] = Config.OWNER_EMAIL
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(
            MIMEText(html_body, "html")
        )

        print("EMAIL STEP 3: Connecting to Gmail")

        with smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=30
        ) as server:

            print("EMAIL STEP 4: Starting TLS")
            server.starttls()

            print("EMAIL STEP 5: Logging into Gmail")
            server.login(
                Config.OWNER_EMAIL,
                Config.APP_PASSWORD
            )

            print("EMAIL STEP 6: Sending email")
            server.sendmail(
                Config.OWNER_EMAIL,
                to_email,
                message.as_string()
            )

        print("EMAIL STEP 7: Email sent successfully")

    except Exception as e:
        print("========== EMAIL ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("=================================")

        raise
