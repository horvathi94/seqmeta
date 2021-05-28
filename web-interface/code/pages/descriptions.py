from __main__ import app
from flask import render_template

from .src.library import LibraryStrategies, \
    LibrarySelections, \
    LibrarySources


@app.route("/descriptions/library")
def descriptions_library():

    html = render_template("head.html", styles=["descriptions.css"]);
    html+= render_template("descriptions/library.html",
                           lib_strategies=LibraryStrategies.fetch_list(),
                           lib_sources=LibrarySources.fetch_list(),
                           lib_selections=LibrarySelections.fetch_list());
    html+= render_template("footer.html");
    return html;
