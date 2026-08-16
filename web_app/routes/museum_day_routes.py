# this is the "web_app/routes/museum_day_routes.py" file...
# used AI to help with creation of this py file


from flask import Blueprint, request, render_template, redirect


from app.museum_day import get_museum_day_plan
from app.weather import FORECAST_URL, NYC_latitude, NYC_longitude
import requests

museum_day_routes = Blueprint("museum_day_routes", __name__)


@museum_day_routes.route("/museum-day/form")
def museum_day_form():
    print("MUSEUM DAY FORM...")
    return render_template("museum_day_form.html")


@museum_day_routes.route("/museum-day/plan", methods=["POST"])
def museum_day_plan():
    print("MUSEUM DAY PLAN...")
    print(dict(request.form))

    date = request.form.get("date")

    # same date-checking as weather.py and museum_day.py
    WEATHER_URL = f"{FORECAST_URL}?latitude={NYC_latitude}&longitude={NYC_longitude}&daily=temperature_2m_max&forecast_days=16"    
    response = requests.get(WEATHER_URL)
    data = response.json()

    if date not in data["daily"]["time"]:
        print("Invalid date.")
        return redirect("/museum-day/form")

    try:
        plan = get_museum_day_plan(date)
        return render_template("museum_day_result.html", plan=plan)
    except Exception as err:
        print("OOPS", err)
        return redirect("/museum-day/form")
