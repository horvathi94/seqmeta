from flask import Blueprint, request, redirect, url_for
from .pages.display import DisplayPage
from .pages.editor import EditorPage
from application.src.institutions import Institutions

institutions_bp = Blueprint("institutions_bp", __name__,
                            template_folder="templates",
                            static_folder="static");




@institutions_bp.route("/institutions/view", methods=["GET"])
def show():
    return DisplayPage.render();



@institutions_bp.route("/institutions/edit", methods=["GET"])
def edit():
    institution_id = int(request.args["id"]) if "id" in request.args else 0;
    return EditorPage.render(institution_id);



@institutions_bp.route("/institutions/submit", methods=["POST"])
def submit():
    data = request.form.to_dict();
    Institutions.save_entry(data);
    return redirect(url_for('institutions_bp.show'));

