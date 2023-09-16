# (c) 2018 Manikandan
import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
