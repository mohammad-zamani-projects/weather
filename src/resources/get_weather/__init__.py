import json
import requests

from weather.src import helpers


def get_weather_json():
    response = requests.get(helpers.URL)
    data = json.loads(response.text)
    return data
    # print(os.popen(f"curl wttr.in/{helper.LOCATION}").read())  # It is just for fun in cli output!
