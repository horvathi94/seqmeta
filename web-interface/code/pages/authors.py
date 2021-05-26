from __main__ import app
from flask import render_template, redirect, request
from .src.authors import Authors

@app.route("/authors/view")
def view_authors():
    authors_list = Authors.fetch_list();
    html = render_template("head.html");
    if len(authors_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="authors",
                               link="edit_authors");
    else:
        html+= render_template("authors/list.html", authors=authors_list);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/edit")
def edit_authors():
    author_id = int(request.args["id"]) if "id" in request.args else 0;
    author = Authors.fetch_entry_edit(id=author_id);
    html = render_template("head.html");
    html+= render_template("authors/edit.html", author=author);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/submit", methods=["POST"])
def submit_authors():
    data = request.form.to_dict();
    Authors.save_entry(data);
    return redirect(url_for('authors_page'));

