from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for
from application.src.authors import Authors


authors_bp = Blueprint("authors_bp", __name__,
                       template_folder="templates",
                       static_folder="static");



@authors_bp.route("/authors/view", methods=["GET"])
def show():
    authors_list = Authors.fetch_list();
    html = render_template("head.html");
    if len(authors_list) == 0:
        html+= render_template("empty_list.html",
                               name_plural="authors",
                               link="bp_authors.edit");
    else:
        html+= render_template("authors/list.html", authors=authors_list);
    html+= render_template("footer.html");
    return html;


@authors_bp.route("/authors/edit", methods=["GET"])
def edit():
    author_id = int(request.args["id"]) if "id" in request.args else 0;
    author = Authors.fetch_entry_edit(id=author_id);
    html = render_template("head.html");
    html+= render_template("authors/edit.html", author=author);
    html+= render_template("footer.html");
    return html;


@authors_bp.route("/authors/submit", methods=["POST"])
def submit():
    data = request.form.to_dict();
    Authors.save_entry(data);
    return redirect(url_for('authors_bp.show'));




