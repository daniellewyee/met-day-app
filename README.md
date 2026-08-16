# met-day-app
An app used to determine if its a good day to go to the met, allows you to search the art for specific pieces to see, and creates a scavenger hunt of art for your day there.

# Setup
Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line.
cd ~/Desktop/met-day-app

Create a virtual environment:
conda create -n met-day-app python=3.11

Activate the virtual environment:
conda activate met-day-app

Install package dependencies:
pip install -r requirements.txt

# Configuration
The APIs used do not require any key / account. Both are free to use

# Usage
Run weather getter:

python -m app.weather

Run museum_day planner:

python -m app.museum_day


# Web App
Run the web app (then view in the browser at http://localhost:5000/):

if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app 
flask run

# Windows OS:
... if `export` doesn't work for you, try `set` instead
... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
whenever we make updates to our flask web app, we need to restart the web server. We do that by typing 'ctrl+c' to stop and 'flask run' again to start

Testing
Run tests:

pytest
