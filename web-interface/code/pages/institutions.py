from __main__ import app
from flask import render_template, redirect, request, url_for
from .src.institutions import Institutions


@app.route("/institutions/view")
def view_institutions():
    institutions_list = Institutions.fetch_list();
    html = render_template("head.html");
    if len(institutions_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="institutions",
                               link="edit_institutions");
    else:
        html+= render_template("institutions/list.html",
                               institutions=institutions_list);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/edit")
def edit_institutions():
    institution_id = int(request.args["id"]) if "id" in request.args else 0;
    institution = Institutions.fetch_entry(id=institution_id);
    html = render_template("head.html");
    html+= render_template("institutions/edit.html", institution=institution);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/submit", methods=["POST"])
def submit_institutions():
    data = request.form.to_dict();
    Institutions.save_entry(data);
    return redirect(url_for('view_institutions'));
