import json
import kavenegar
# import os
import requests
import smtplib
import ssl

from kavenegar import *
from email.message import EmailMessage
from weather.utils import helper


def get_weather_json():
    response = requests.get(helper.URL)
    data = json.loads(response.text)
    return data
    # print(os.popen(f"curl wttr.in/{helper.LOCATION}").read())  # It is just for fun in cli output!


def report_weather_data(data):
    if "rain" in data["weather"][0]["description"] or "drizzle" in data["weather"][0]["description"]:
        message = "It's rainy, so remember to bring an umbrella!"
        send_message(message)

    if (data["main"]["temp"] - 273.15) <= 3:
        message = "It is very cold, please wear warm clothes"
        send_message(message)

    weather_title = data['weather'][0]['main']
    weather = data['weather'][0]['description']
    temp = int(data['main']['temp'] - 273.15)
    min_temp = int(data['main']['temp_min'] - 273.15)
    max_temp = int(data['main']['temp_max'] - 273.15)
    message = f"""
    It is {weather_title} today, {weather}.
    The temperature is {temp} degrees Celsius.minimum {min_temp} and maximum {max_temp} degrees Celsius.
    """
    send_mail(message)




def send_message(message=None):
    try:
        api = KavenegarAPI('56594A305046422B656566785A4543344A73382B55437043356C314D35687143587052453278616F4C424D3D')
        params = {
            'sender': '10004346',
            'receptor': '09127762933',
            'message': 'Kaveh specialized Web service '
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))



def send_mail(message):
    subject = "Today's weather"

    email = EmailMessage()
    email['From'] = helper.SENDER_EMAIL
    email['To'] = helper.RECEIVER_EMAIL
    email['Subject'] = subject
    email.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(helper.SMTP_SERVER, helper.PORT, context=context) as server:
        server.login(helper.SENDER_EMAIL, helper.PASSWORD)
        server.sendmail(helper.SENDER_EMAIL, helper.RECEIVER_EMAIL, email.as_string())



