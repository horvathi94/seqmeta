from flask import Flask, render_template, request
from datetime import datetime

from cursor import Cursor
import viewdb

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
    html+= render_template("table.html");
    html+= render_template("footer.html");
    return html;


@app.route("/submit", methods=["POST"])
def submitted():


    html = render_template("head.html");

    sample_name = request.form["sample-name"]
    submission_date = datetime.today().strftime("%Y-%m-%d");


    html+= "<h1> Submitted data </h1>";
    html+= "<p> Sample name: {:s} </p>".format(sample_name);
    html+= "<p> Submission date: {:s} </p>".format(submission_date)

    html+= render_template("footer.html");
    return html;


@app.route("/search")
def search_database():

    html = render_template("head.html");
    html+= "<h2> Search the database </h2>";

    html+= viewdb.database_view();

    html+= render_template("footer.html");

    return html;


@app.route("/test")
def test():

    html = render_template("head.html");
    html+= "<h2> This page is for running tests </h2>";

    cursor = Cursor();
    raw = cursor.select_all("sample_data");
    cursor.close();

    html+= str(raw);

    html+= render_template("footer.html");

    return html;


if __name__ == "__main__":
   app.run("0.0.0.0", debug=True);
