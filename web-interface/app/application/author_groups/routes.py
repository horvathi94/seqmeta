from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for
from application.src.authors import Authors, AuthorGroups
from application.src.forms.form import Form


author_groups_bp = Blueprint("author_groups_bp", __name__,
                               template_folder="templates",
                               static_folder="static",
                               static_url_path="/static/author-groups/");


description = """Create author groups from registered authors. These groups
 will appear in author enumeration fields.""";


@author_groups_bp.route("/author-groups/view")
def show():
    groups_list = AuthorGroups.fetch_list();
    html = render_template("head.html");
    if len(groups_list) == 0:
        html+= render_template("empty_list.html",
                               name_plural="author groups",
                               link="author_groups_bp.edit",
                               description=description);
    else:
        html+= render_template("author_groups/list.html", groups=groups_list);
    html+= render_template("footer.html");
    return html;


@author_groups_bp.route("/author-groups/edit")
def edit():
    scripts = [{"filename":"edit.js", "prefix":"author-groups"}];
    styles = [{"filename": "group-editor.css", "prefix": "author-groups"},
              {"filename": "smbasicform.css"}];
    group_id = int(request.args["id"]) if "id" in request.args else 0;
    group = AuthorGroups.fetch_entry_edit(group_id=group_id);
    authors_list = Authors.fetch_list();
    html = render_template("head.html", styles=styles);
    html+= render_template("author_groups/edit.html",
                           group=group,
                           authors_list=authors_list);
    html+= render_template("footer.html",
                           scripts=scripts);
    return html;

@author_groups_bp.route("/author-groups/submit", methods=["POST"])
def submit():
    form_data = request.form.to_dict();
    authors_list = Form.parse_list(form_data, "author")[1:];
    group = Form.parse_simple(form_data, "group");
    AuthorGroups.save(group, authors_list);
    return redirect(url_for('author_groups_bp.show'));
