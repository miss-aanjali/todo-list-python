import requests

API_KEY = "YOUR_API_KEY_HERE"   # <-- Paste your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # For Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found!")
        return

    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)


def main():
    city = input("Enter city name: ")
    get_weather(city)

main()
import requests

API_KEY = "YOUR_API_KEY_HERE"   # <-- Paste your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # For Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found!")
        return

    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)


def main():
    city = input("Enter city name: ")
    get_weather(city)

main()



import requests

API_KEY = "YOUR_API_KEY_HERE"   # <-- Paste your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # For Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found!")
        return

    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)


def main():
    city = input("Enter city name: ")
    get_weather(city)

main()

