from weather.src.resources.get_weather import get_weather_json
from weather.src.resources.send_mail import send_mail
from weather.src.resources.send_sms import send_message


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


if __name__ == "__main__":
    data = get_weather_json()
    report_weather_data(data)
