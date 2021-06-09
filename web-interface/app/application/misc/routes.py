from flask import Blueprint, render_template, request, redirect, url_for
from application.src.library import LibraryStrategies, \
    LibrarySelections, \
    LibrarySources
from application.src.samples.virusname import VirusnameGisaid

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


@misc_bp.route("/misc/edit")
def edit():
    html = render_template("head.html");
    html+= render_template("misc/virusname.html",
                virusname_format=VirusnameGisaid.fetch_format_string(),
                available_db_keys=VirusnameGisaid.available_db_keys());
    html+= render_template("footer.html");
    return html;


@misc_bp.route("/misc/submit/virusname", methods=["POST"])
def submit_virusname():
    virusname = request.form.to_dict()["virusname"];
    VirusnameGisaid.call_save_procedure(virusname);
    return redirect(url_for("misc_bp.edit"));
