import ssl
import smtplib

from email.message import EmailMessage
from weather.src import helpers


def send_mail(message):
    subject = "Today's weather"

    email = EmailMessage()
    email['From'] = helpers.SENDER_EMAIL
    email['To'] = helpers.RECEIVER_EMAIL
    email['Subject'] = subject
    email.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(helpers.SMTP_SERVER, helpers.PORT, context=context) as server:
        server.login(helpers.SENDER_EMAIL, helpers.PASSWORD)
        server.sendmail(helpers.SENDER_EMAIL, helpers.RECEIVER_EMAIL, email.as_string())
