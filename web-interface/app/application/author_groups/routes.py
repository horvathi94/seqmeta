from flask import Blueprint, request, redirect, url_for
from .pages.display import DisplayPage
from .pages.editor import EditorPage
from application.src.authors import AuthorGroups
from application.src.forms.form import Form


author_groups_bp = Blueprint("author_groups_bp", __name__,
                               template_folder="templates",
                               static_folder="static",
                               static_url_path="/static/author-groups/");



@author_groups_bp.route("/author-groups/view")
def show():
    """Main page for author groups."""

    return DisplayPage.show();



@author_groups_bp.route("/author-groups/edit")
def edit():
    """Editor page for author groups."""

    group_id = int(request.args["id"]) if "id" in request.args else 0;
    return EditorPage.show(group_id);



@author_groups_bp.route("/author-groups/submit", methods=["POST"])
def submit():
    """Handle author group data submitted from the edior."""

    form_data = request.form.to_dict();
    authors_list = Form.parse_list(form_data, "author")[1:];
    group = Form.parse_simple(form_data, "group");
    AuthorGroups.save(group, authors_list);
    return redirect(url_for('author_groups_bp.show'));
