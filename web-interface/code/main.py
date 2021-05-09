from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def front_page():
   return render_template("index.html");


@app.route("/sample", methods=["GET", "POST"])
def submit_sample():

    if request.method == "GET":
        return render_template("table.html");

    sample_name = request.form["sample-name"]
    return """
        <p> Sample Name: {:s} </p>
    """.format();


@app.route("/submit", methods=["POST"])
def submitted():

    sample_name = request.form["sample-name"]
    submission_date = datetime.today().strftime("%Y-%m-%d");


    html = "<h1> Submitted data </h1>";
    html+= "<p> Sample name: {:s} </p>".format(sample_name);
    html+= "<p> Submission date: {:s} </p>".format(submission_date)

    return html;

from cursor import Cursor

@app.route("/test")
def test():

    html = "<h2> This page is for running tests </h2>";

    cursor = Cursor();
    raw = cursor.describe("sample_data");

    html+= str(raw);

    return html;


if __name__ == "__main__":
   app.run("0.0.0.0", debug=True);
