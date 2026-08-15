from app.weather import get_today_weather, FORECAST_URL, NYC_latitude, NYC_longitude
from app.art_search import find_art, get_object_details, get_random_art_list
# AI used here to figure out how to link the weather.py and art_search.py file to this file


import requests
import random

# a small list of predefined words to search Met art with to curate art list
RAIN_WORDS = ["rain", "storm", "umbrella", "clouds"]
HOT_WORDS = ["sun", "summer", "beach", "garden"]
COLD_WORDS = ["winter", "snow", "fire", "moon"]
NICE_WORDS = ["garden", "flower", "landscape", "bird"]

def get_museum_recommendation(high_temp, low_temp, rain_chance):
    # decides if it's a good museum day based on weather, and picks a random search term to curate some art
    # search word is a list of words that matches the weather
    # returns a dictionary

    avg_temp = (high_temp + low_temp) / 2

    if rain_chance >= 50:
        return {
            "should_go": True,
            "reason": "A rainy day :/ perfect excuse to go to the museum!",
            "search_words": RAIN_WORDS
        }
    elif avg_temp >= 90:
        return {
            "should_go": True,
            "reason": "Wow, it's way too hot to be outside for long. Let's go to the museum!",
            "search_words": HOT_WORDS
        }
    elif avg_temp <= 35:
        return {
            "should_go": True,
            "reason": "Wow, it's way too cold to be outside for long. Let's go to the museum!",
            "search_words": COLD_WORDS
        }
    else:
        return {
            "should_go": False,
            "reason": "Actually pretty nice out, maybe we should just go outside instead of the museum",
            "search_words": NICE_WORDS
        }


def get_museum_day_plan(date):
    # gets the weather from weather.py
    # makes a recommendation based on weather function above and returns respective dictionary
    # searches the random word list for a word to recommend art on based on the search word tied to each weather condition
    # searchest Met API for art based on word and returns a list of 10 object Ids

    weather = get_today_weather(NYC_latitude, NYC_longitude, date)
    # gets the weather recommendation based on date
    # function returns a dictionary with high temp, low temp, and rain chance

    recommendation = get_museum_recommendation(weather["high_temp"], weather["low_temp"], weather["rain_chance"])
    # gets the museum recommendation for the day based on weather

    search_term = random.choice(recommendation["search_words"])
    # picks a random search term out of our defined list

    artwork = get_random_art_list(search_term)
    # gets the list of 10 art pieces based on the search term

    return {
        "date": date,
        "high_temp": weather["high_temp"],
        "low_temp": weather["low_temp"],
        "rain_chance": weather["rain_chance"],
        "should_go": recommendation["should_go"],
        "reason": recommendation["reason"],
        "search_word": search_term,
        "artwork": artwork
    }


if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
    print("MUSEUM DAY PLANNER")

    date = input("What date do you want to go to the MET? (YYYY-MM-DD): ")

    # same date-checking as weather.py
    WEATHER_URL = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&timezone=auto&forecast_days=16"    
    response = requests.get(WEATHER_URL)
    data = response.json()

    while date not in data["daily"]["time"]:
        print("Invalid date. Please enter a date within the next 16 days.")
        date = input("What date do you want to go to the MET? (YYYY-MM-DD): ")

    plan = get_museum_day_plan(date)
    print(plan)

    print(f"\nWeather on {plan['date']}: high of {plan['high_temp']}°F, low of {plan['low_temp']}°F, {plan['rain_chance']}% chance of rain")
    print(plan["should_go"],plan["reason"])

    print(f"\nSearched for: {plan['search_word']}")
    print(f"Found {len(plan['artwork'])} pieces:\n")

    for art in plan["artwork"]:
        print(art["name"])
        print(f"  Artist: {art['artist']}")
        print(f"  Photo: {art['photo']}")
        print()
