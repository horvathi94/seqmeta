from flask import Blueprint, request, redirect, url_for
from .pages.display import DisplayPage
from .pages.editor import EditorPage
from application.src.institutions import Institutions

institutions_bp = Blueprint("institutions_bp", __name__,
                            template_folder="templates",
                            static_folder="static");




@institutions_bp.route("/institutions/view", methods=["GET"])
def show():
    """Main page for insititutions."""

    return DisplayPage.show();



@institutions_bp.route("/institutions/edit", methods=["GET"])
def edit():
    """Editor for institutions."""

    institution_id = int(request.args["id"]) if "id" in request.args else 0;
    return EditorPage.show(institution_id);



@institutions_bp.route("/institutions/submit", methods=["POST"])
def submit():
    """Handle institution data submitted from the editor."""

    data = request.form.to_dict();
    Institutions.save_entry(data);
    return redirect(url_for('institutions_bp.show'));

