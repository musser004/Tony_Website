import smtplib
import os


class EmailSender:

    # Contact information retrieved from environmental variables

    def __init__(self):
        self.email = "email"
        self.email = os.environ['EMAIL']
        self.app_password = os.environ["GMAIL_APP_PASSWORD"]

    def send_email(self, name, phone, contact_email, message):

        # Sending email with smtplib, based on contact form submissions

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.app_password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject: (tonyweikel.com) Portfolio contact form message!\n\nName: {name}\n\nPhone: {phone}\n\n"
                    f"Email: {contact_email}\n\n{message}"
            )
