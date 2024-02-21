import requests
import json

from weather.utils import helper


def get_weather_json():
    response = requests.get(helper.URL)
    print(response.text)




