# this is the "web_app/__init__.py" file...

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.museum_day_routes import museum_day_routes
from web_app.routes.art_search_routes import art_search_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(museum_day_routes)
    app.register_blueprint(art_search_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)