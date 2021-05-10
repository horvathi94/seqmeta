from flask import render_template
from cursor import Cursor
import funcs

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

def save_authors(raw_form):

    submitted = funcs.form_to_dict_list(raw_form, "authors");

    html = "";
    cursor = Cursor();
    html += cursor.list_and_save("author", submitted);
    cursor.close();


    return html;

