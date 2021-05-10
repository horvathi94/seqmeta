from flask import render_template
from cursor import Cursor

def fetch_authors():
    cursor = Cursor();
    authors = cursor.select_all("author");
    cursor.close();

    for author in authors:
        if author["middle_name"] == None:
            author["middle_name"] = "";

    return authors;


def list_authors():

    authors = fetch_authors();
    html = render_template("authors.html", authors=authors);
    return html;


def edit_authors():

    authors = fetch_authors();
    html = render_template("authors_edit.html", authors=authors);
    return html;

def save_authors(form):

    authors = fetch_authors();

    html = "";
    html+= str(form);
#        html+= str(item["first-name"]) + " : " + str(form[item]) +  "<br>";

#    if form[0] in authors:
#        html += "Is in\n";

    return html;

