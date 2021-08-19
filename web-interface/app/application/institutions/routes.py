from flask import Blueprint, render_template, request, redirect, url_for
from .info import Info
from application.src.institutions import Institutions
from application.src.misc import Countries

institutions_bp = Blueprint("institutions_bp", __name__,
                            template_folder="templates",
                            static_folder="static");




@institutions_bp.route("/institutions/view", methods=["GET"])
def show():
    """Main page for insititutions."""

    institutions_list = Institutions.fetch_list();
    html = render_template("head.html");

    if len(institutions_list) == 0:
        html+= render_template("empty_list.html",
                               name_plural=Info.name_plural,
                               link="institutions_bp.edit",
                               description=Info.description);
    else:
        html+= render_template("institutions/list.html",
                               institutions=institutions_list);

    html+= render_template("footer.html");
    return html;


@institutions_bp.route("/institutions/edit", methods=["GET"])
def edit():
    """Editor for institutions."""

    styles=[{"filename": "smbasicform.css"}];
    institution_id = int(request.args["id"]) if "id" in request.args else 0;
    institution = Institutions.fetch_entry(id=institution_id);
    html = render_template("head.html", styles=styles);
    html+= render_template("institutions/edit.html", institution=institution,
                           countries=Countries.fetch_list());
    html+= render_template("footer.html");
    return html;


@institutions_bp.route("/institutions/submit", methods=["POST"])
def submit():
    """Handle institution data submitted from the editor."""

    data = request.form.to_dict();
    Institutions.save_entry(data);
    return redirect(url_for('institutions_bp.show'));

