from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from src.cursor import Cursor
from src import authors
from src.authors import Authors
from src.institutions import Institutions
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



# Institutions
###############################################################################

@app.route("/institutions")
def institutions_list():

    institutions = Institutions();
    institutions_list = institutions.fetch_list();
    html = render_template("head.html");
    if len(institutions_list) == 0:
        html+= render_template("institutions/empty.html");
    html+= str(institutions_list);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/edit")
def institutions_edit():

    institution_id = 0;
    if "id" in request.args:
        institution_id = int(request.args["id"]);

    html = render_template("head.html");
    html+= render_template("footer.html");
    return html;


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
