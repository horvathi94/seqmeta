from flask import Blueprint, request, redirect, url_for
from .pages.display import DisplayPage
from .pages.editor import EditorPage
from application.src.authors import Authors


authors_bp = Blueprint("authors_bp", __name__,
                       template_folder="templates",
                       static_folder="static",
                       static_url_path="/static/authors/");




@authors_bp.route("/authors/view", methods=["GET"])
def show():
    return DisplayPage.render();



@authors_bp.route("/authors/edit", methods=["GET"])
def edit():
    author_id = int(request.args["id"]) if "id" in request.args else 0;
    return EditorPage.render(author_id);



@authors_bp.route("/authors/submit", methods=["POST"])
def submit():
    data = request.form.to_dict();
    Authors.save_entry(data);
    return redirect(url_for('authors_bp.show'));




