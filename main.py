from weather.utils import report_weather_data
from weather.utils import get_weather_json
from weather.utils import send_mail

# check  https://www.geeksforgeeks.org/building-a-weather-cli-using-python/   <--It's useful
if __name__ == "__main__":
    data = get_weather_json()
    report_weather_data(data)
    # send_mail()










