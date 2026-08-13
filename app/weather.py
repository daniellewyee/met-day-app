# This function tells you the weather for today in NYC and defines the latititude and logitude for NYC.
import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

NYC_latitude = 40.71
NYC_longitude = -74.01

def get_today_weather(latitude, longitude):
    # gets today's highest temp (in Farenheight) and chance of rain (%) for a location
    request_url = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max,precipitation_probability_max&temperature_unit=fahrenheit&timezone=auto&forecast_days=1"

    response = requests.get(request_url)
    data = response.json()

    daily = data["daily"]

    return {
        "high_temp": daily["temperature_2m_max"][0],
        "rain_chance": daily["precipitation_probability_max"][0]}


if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE'RE TRYING TO JUST IMPORT SOME STUFF FROM THIS FILE
    weather = get_today_weather(NYC_latitude, NYC_longitude)
    print(weather)