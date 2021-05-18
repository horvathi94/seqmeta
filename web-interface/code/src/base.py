from .cursor import Cursor


class Base:

    view_table_name = "";
    submit_table_name = "";

    save_procedure = "";

    def __init__(self):
        pass;


    def clean_entry(self, entry):
        pass;


    def fetch_list(self):

        cursor = Cursor();
        entries = cursor.select_all(self.view_table_name);
        cursor.close();

        for entry in entries:
            self.clean_entry(entry);

        return entries;


    def fetch_entry(self, id=0):

        cursor = Cursor();
        entry = cursor.select_by_id(self.view_table_name, id);
        cursor.close();
        self.clean_entry(entry);
        return entry;


    def save_entry(self, submitted):

        self.clean_submit(submitted);

        submitted_id = int(submitted["id"]);
        cursor = Cursor();

        if submitted_id == 0:
            cursor.insert_item(self.submit_table_name, submitted);
        else:
            cursor.update_row(self.submit_table_name, submitted_id, submitted);

        cursor.close();


    def clean_submit(self, submitted):
        pass;


    def save_by_procedure(self, items):
        """
            Good for basic tables with columns: | id | label |
        """
        if self.save_procedure == "":
            return;

        cursor = Cursor();

        for item in items:
            args = (int(item["id"]), str(item["label"]));
            cursor.call_procedure(self.save_procedure, args=args, commit=True);

        cursor.close();

