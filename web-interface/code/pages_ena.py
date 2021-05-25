from __main__ import app
from flask import render_template, redirect, request, url_for, Response
from src.ena import Studies


@app.route("/ena/studies/view")
def view_ena_studies():
    studies = Studies.fetch_list();
    html = render_template("head.html");
    if len(studies) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="ENA studies",
                               link="edit_ena_studies");
    else:
        html+= render_template("ena_studies/list.html", studies=studies);
    html+= render_template("footer.html");
    return html;


@app.route("/ena/studies/edit")
def edit_ena_studies():
    study_id = int(request.args["id"]) if "id" in request.args else 0;
    study = Studies.fetch_entry_edit(id=study_id);
    html = render_template("head.html");
    html+= render_template("ena_studies/edit.html", study=study);
    html+= render_template("footer.html");
    return html;


@app.route("/ena/studies/submit", methods=["POST"])
def submit_ena_studies():
    Studies.save_entry(request.form.to_dict());
    return redirect(url_for("view_ena_studies"));


@app.route("/ena/studies/xml")
def xml_ena_studies():
    xml_data = Studies.create_xml(1);
    return Response(xml_data, mimetype="text/xml");
