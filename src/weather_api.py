# weather_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    params = {
        'q': location,
        'appid': WEATHER_API_KEY
    }
    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status()
    return response.json()
