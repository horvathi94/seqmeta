from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from cursor import Cursor
import viewdb
import upload
import authors
import funcs

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


@app.route("/authors")
def authors_page():

    html = render_template("head.html");
    html+= authors.list_authors();
    html+= render_template("footer.html");
    return html;


@app.route("/authors/edit", methods=["GET", "POST"])
def authors_edit():

    html = render_template("head.html");
    html+= authors.edit_authors();
#    html+= render_template("footer.html", scripts=["authors_submit.js"]);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/submit", methods=["POST"])
def authors_submit():

    authors.save_authors(request.form);
    return redirect(url_for('authors_page'));


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
