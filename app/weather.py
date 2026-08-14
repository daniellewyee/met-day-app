# This function tells you the weather for today in NYC and defines the latititude and logitude for NYC.
import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# created variables for the latitude and longitude of NYC (fixed values)
NYC_latitude = 40.71
NYC_longitude = -74.01

def get_today_weather(latitude, longitude,date):
    # gets today's highest temp (in Farenheight) and chance of rain (%) for a location
    # days = 16 gets the next 16 days of forecast (all thats available from the API)
    WEATHER_URL = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&timezone=auto&forecast_days=16"

    response = requests.get(WEATHER_URL)
    data = response.json()

    daily = data["daily"]

    date_index = daily["time"].index(date)
    # used AI to figure out exactly how to get this line to work

    # print(data) -- tested this and prints the data returned from API call - 16 temperatures
    return {
        "high_temp": daily["temperature_2m_max"][date_index],
        "low_temp": daily["temperature_2m_min"][date_index],
        "rain_chance": daily["precipitation_probability_max"][date_index]
    }


if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE'RE TRYING TO JUST IMPORT SOME STUFF FROM THIS FILE
    date = input("What date do you want to go to the MET? (YYYY-MM-DD)")

    # Check input is valid - if not, ask again
    WEATHER_URL = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&timezone=auto&forecast_days=16"    
    response = requests.get(WEATHER_URL)
    data = response.json()

    # print(data["daily"]["time"])  Used to check list of date output 

    # Continue prompting user for a valid date until one is provided
    while date not in data["daily"]["time"]:
        print("Invalid date. Please enter a date within the next 16 days.")
        date = input("What date do you want to go to the MET? (YYYY-MM-DD)")


    weather = get_today_weather(NYC_latitude, NYC_longitude,date)
    print(weather)