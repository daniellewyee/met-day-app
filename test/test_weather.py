# this is the "test/test_weather.py" file...

# todo: test the functionality in the "app/weather.py" file
import requests
from app.weather import get_today_weather, FORECAST_URL, NYC_latitude, NYC_longitude


def get_todays_date():
    # grab the first date from the 16 day forecast
    # should be todays date
    WEATHER_URL = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max&forecast_days=16"
    response = requests.get(WEATHER_URL)
    data = response.json()
    return data["daily"]["time"][0]


def test_get_today_weather():
    # checks that get today weather returns a dictionary with 3 items
    today = get_todays_date()
    weather = get_today_weather(NYC_latitude, NYC_longitude, today)

    assert "high_temp" in weather
    assert "low_temp" in weather
    assert "rain_chance" in weather


def test_get_today_weather_numbers():
    # check that the values returned in the dictionary are all numbers
    today = get_todays_date()
    weather = get_today_weather(NYC_latitude, NYC_longitude, today)

    assert isinstance(weather["high_temp"], (int, float))
    assert isinstance(weather["low_temp"], (int, float))
    assert isinstance(weather["rain_chance"], (int, float))