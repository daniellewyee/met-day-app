# this is the "web_app/routes/art_search_routes.py" file...
# used AI to help with creation of this py file

from flask import Blueprint, request, render_template, redirect

from app.art_search import get_random_art_list

art_search_routes = Blueprint("art_search_routes", __name__)


@art_search_routes.route("/art-search/form")
def art_search_form():
    print("ART SEARCH FORM...")
    return render_template("art_search_form.html")


@art_search_routes.route("/art-search/results", methods=["POST"])
def art_search_results():
    print("ART SEARCH RESULTS...")
    print(dict(request.form))

    search_word = request.form.get("search_word")

    try:
        art_list = get_random_art_list(search_word)
        return render_template("art_search_results.html", search_word=search_word, art_list=art_list)
    except Exception as err:
        print("OOPS", err)
        return redirect("/art-search/form")
