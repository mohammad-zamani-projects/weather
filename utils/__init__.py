import requests
import os
import json

from weather.utils import helper


def get_weather_json():
    response = requests.get(helper.URL)
    print(response.text)

    # print(os.popen(f"curl wttr.in/{helper.LOCATION}").read())




