from cursor import Cursor

def fetch_organizations():

    cursor = Cursor();
    orgs = cusror.selecet_all("organizations");
    cursor.close();
