from .cursor import Cursor


class Base:

    table_name = "";

    def __init__(self):
        pass;


    def clean_entry(self, entry):
        pass;


    def fetch_list(self):

        cursor = Cursor();
        entries = cursor.select_all(self.table_name);
        cursor.close();

        for entry in entries:
            self.clean_entry(entry);

        return entries;


    def fetch_entry(self, id=0):

        cursor = Cursor();
        entry = cursor.select_by_id(self.table_name, id);
        self.clean_entry(entry);
        cursor.close();
        return entry;


    def save_entry(self, submitted):

        submitted_id = int(submitted["id"]);
        cursor = Cursor();

        if submitted_id == 0:
            cursor.insert_item(self.table_name, submitted);
        else:
            cursor.update_row(self.table_name, submitted_id, submitted);

        cursor.close();
