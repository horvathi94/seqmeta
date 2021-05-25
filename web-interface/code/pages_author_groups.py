from __main__ import app
from flask import render_template, redirect, request
from src.authors import Authors
from src.author_groups import AuthorGroups
from src import funcs

@app.route("/author-groups/view")
def view_author_groups():
    groups_list = AuthorGroups.fetch_list();
    html = render_template("head.html");
    if len(groups_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="author groups",
                               link="edit_author_groups");
    else:
        html+= render_template("author_groups/list.html", groups=groups_list);
    html+= render_template("footer.html");
    return html;


@app.route("/author-groups/edit")
def edit_author_groups():
    group_id = int(request.args["id"]) if "id" in request.args else 0;
    group = AuthorGroups.fetch_entry_edit(group_id=group_id);
    authors_list = Authors.fetch_list();
    html = render_template("head.html");
    html+= render_template("author_groups/edit.html",
                           group=group,
                           authors_list=authors_list);
    html+= render_template("footer.html", scripts=["author_groups.js"]);
    return html;


@app.route("/author-groups/submit", methods=["POST"])
def submit_author_groups():
    form_data = request.form.to_dict();
    authors_list = funcs.parse_form_list(form_data, "author");
    group = funcs.parse_form_simple(form_data, "group");
    AuthorGroups.save(group, authors_list);
    return redirect(url_for('view_author_groups'));
