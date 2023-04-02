import requests
import os

# Getting API key we stored in environment.
API_KEY = os.environ.get("API_KEY")
# Parameters to get weather condition.
parameters = {
    # Longitude and latitude of place where you want to check weather.
    'lat': 30.666121,  # latitude.
    'lon': 73.102013,  # longitude.
    'appid': API_KEY,
    # reducing data by excluding what we didn't need.
    'exclude': 'current,minute,daily'

}
# Sending a request for weather.
request = requests.get(f'http://api.openweathermap.org/data/2.5/forecast', params=parameters)
# Exception handling.
request.raise_for_status()
# Json data of weather.
data = request.json()
# Next 12 hours forcast:
weather_slice = data['list'][:12]
# check for what condition on every hour.
for weather in weather_slice:
    weather_condition = weather['weather'][0]
    if int(weather_condition['id']) < 700:  # <700 means bad weather may be rainy, snow, etc. For more check API doc.
        print(f"""Bring umbrella 🌧 remarks {weather_condition['description']}""")
    else:
        print("You don't need umbrella.")
