import json
import os
import requests
import smtplib
import ssl


from weather.utils import helper


def get_weather_json():
    response = requests.get(helper.URL)
    data = json.loads(response.text)
    return data

    # print(os.popen(f"curl wttr.in/{helper.LOCATION}").read())


def send_mail():
    message = '''\
    subject: Test email
    
    This is just a test email. if you see this message be happy!
    '''

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(helper.SMTP_SERVER, helper.PORT, context=context) as server:
        server.login(helper.SENDER_EMAIL, helper.PASSWORD)
        server.sendmail(helper.SENDER_EMAIL, helper.RECEIVER_EMAIL, message)



