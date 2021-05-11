from cursor import Cursor

def clean_author_od(author_od):

    if author_od["middle_name"] == None:
        author_od["middle_name"] = "";


def fetch_author(id=0):

    cursor = Cursor();
    author = cursor.select_by_id("authors", id);
    clean_author_od(author);
    cursor.close();
    return author;


def fetch_authors():

    cursor = Cursor();
    authors = cursor.select_all("authors");
    cursor.close();

    for author in authors:
        clean_author_od(author);

    return authors;


def save_authors(submitted):

    submitted["id"] = int(submitted["id"]);
    cursor = Cursor();

    if submitted["id"] == 0:
        cursor.insert_item("authors", submitted);
    else:
        cursor.update_row("authors", submitted["id"], submitted);

    cursor.close();
