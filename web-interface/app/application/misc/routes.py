from flask import Blueprint, render_template, request, redirect, url_for
from application.src.library import LibraryStrategies, \
    LibrarySelections, \
    LibrarySources

misc_bp = Blueprint("misc_bp", __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static/misc/");


@misc_bp.route("/descriptions/library")
def descript_library():
    styles=[{"filename":"library.css", "prefix":"misc"}];
    html = render_template("head.html", styles=styles);
    html+= render_template("descriptions/library.html",
                           lib_strategies=LibraryStrategies.fetch_list(),
                           lib_sources=LibrarySources.fetch_list(),
                           lib_selections=LibrarySelections.fetch_list());
    html+= render_template("footer.html");
    return html;
