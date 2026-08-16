# this is the "web_app/routes/home_routes.py" file...
# used AI to help with creation of this py file

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")
