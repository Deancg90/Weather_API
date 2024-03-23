import datetime as dt
import requests

# API url, key & the city we want to check the weather for
api_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = open('WeatherAPI.txt', 'r').read()
city = "Manchester"


# Function which converts kelvin to celcius & fahrenheit
def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9 / 5) + 32
    return celcius, fahrenheit


# sum all the above data to create a full url & get the response
url = api_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()

# What we actually want to pull from the website
temp_kelvin = response['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_celcius(temp_kelvin)
wind_speed = response['wind']['speed']
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celcius(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] +
                                         response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] +
                                        response['timezone'])


print(f"The Weather in {city} is: {description}")
print(f"Temperature: {temp_celcius:.2f} °C")
print(f"Temperature feels like: {feels_like_celsius:.2f} °C")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Humidity: {humidity} %")
print(f"Sunrise time: {sunrise_time} AM")
print(f"Sunset time: {sunset_time} PM")