from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from src.cursor import Cursor
from src.samples import Samples
from src.authors import Authors, AuthorNameTag
from src.institutions import Institutions
from src.author_groups import AuthorGroups
from src import funcs

import viewdb
import upload

app = Flask(__name__)

@app.route("/")
def home():

    html = render_template("head.html");
    html+= render_template("index.html");
    html+= render_template("footer.html");
    return html;


@app.route("/upload")
def upload_sample():

    html = render_template("head.html");
    html+= render_template("upload_form.html");
    html+= render_template("footer.html");
    return html;


@app.route("/submit", methods=["POST"])
def submitted():


    html = render_template("head.html");

    sample_name = request.form["sample-name"]
    submission_date = datetime.today().strftime("%Y-%m-%d");

    html+= render_template("registered.html",
                           sample_name=request.form["sample-name"],
                           sample_collection_date=request.form["sample-collection-date"],
                           patient_name=request.form["patient-name"],
                           patient_gender=request.form["patient-gender"]);

    html+= render_template("footer.html");
    return html;


@app.route("/search")
def search_database():

    html = render_template("head.html");
    html+= "<h2> Search the database </h2>";

    html+= viewdb.database_view();

    html+= render_template("footer.html");

    return html;


# Samples
###############################################################################

@app.route("/samples")
def samples_list():

    samples = Samples();
    samples_list = samples.fetch_list();
    html = render_template("head.html");
    if len(samples_list) == 0:
        html+= render_template("samples/empty.html");
    html+= render_template("footer.html");
    return html;


# Authors section
###############################################################################

@app.route("/authors")
def authors_page():

    authors = Authors();
    authors_list = authors.fetch_list();
    html = render_template("head.html");
    if len(authors_list) == 0:
        html+= render_template("authors/empty.html");
    else:
        html+= render_template("authors/list.html", authors=authors_list);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/edit")
def authors_edit():

    author_id = 0;
    if "id" in request.args:
        author_id = int(request.args["id"]);
    authors = Authors();
    author = authors.fetch_entry(id=author_id);
    html = render_template("head.html");
    html+= render_template("authors/edit.html", author=author);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/submit", methods=["POST"])
def authors_submit():

    data = request.form.to_dict();
    authors = Authors();
    authors.save_entry(data);
    return redirect(url_for('authors_page'));


@app.route("/authors/groups")
def author_groups_list():

    groups = AuthorGroups();
    groups_list = groups.fetch_display_list();

    html = render_template("head.html");
    if len(groups_list) == 0:
        html+= render_template("author_groups/empty.html");
    else:
        html+= render_template("author_groups/list.html", groups=groups_list);

    html+= render_template("footer.html");
    return html;


@app.route("/authors/groups/edit")
def author_groups_edit():

    group_id = 0;
    if "id" in request.args:
        group_id = int(request.args["id"]);

    author_group = AuthorGroups();
    group = author_group.fetch_entry(group_id=group_id);

    authors = Authors();
    authors_list = authors.fetch_list();
    authors_list = sorted(authors_list, key=lambda k: k["last_name"]);
    for a in authors_list:
        tag = AuthorNameTag(a);
        a["name_tag"] = tag.abreviated_middle_name();


    html = render_template("head.html");
    html+= render_template("author_groups/edit.html",
                           group=group,
                           authors_list=authors_list);
    html+= render_template("footer.html", scripts=["author_groups.js"]);
    return html;

@app.route("/authors/groups/submit", methods=["POST"])
def author_groups_submit():

    form_data = request.form.to_dict();

    html = str(funcs.parse_form_list(form_data, "author"));
    #html = str(form_data);

    return html;

# Institutions
###############################################################################

@app.route("/institutions")
def institutions_list():

    institutions = Institutions();
    institutions_list = institutions.fetch_list();
    html = render_template("head.html");
    if len(institutions_list) == 0:
        html+= render_template("institutions/empty.html");
    else:
        html+= render_template("institutions/list.html",
                               institutions=institutions_list);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/edit")
def institutions_edit():

    institution_id = 0;
    if "id" in request.args:
        institution_id = int(request.args["id"]);
    institutions = Institutions();
    institution = institutions.fetch_entry(id=institution_id);

    html = render_template("head.html");
    html+= render_template("institutions/edit.html", institution=institution);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/submit", methods=["POST"])
def institutions_submit():

    data = request.form.to_dict();
    institutions = Institutions();
    institutions.save_entry(data);
    return redirect(url_for('institutions_list'));





@app.route("/test")
def test():

    html = render_template("head.html", styles=["test.css"]);
    html+= "<h2> This page is for running tests </h2>";

    cursor = Cursor();
    raw = cursor.select_all("sample_data");
    cursor.close();

    html+= str(raw);

    html+= render_template("footer.html", scripts=["authors_submit.js"]);

    return html;


if __name__ == "__main__":
   app.run("0.0.0.0", debug=True);
