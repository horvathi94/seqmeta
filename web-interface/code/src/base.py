from .cursor import Cursor


class Base:

    view_table_name = "";
    submit_table_name = "";

    save_procedure = "";

    def __init__(self):
        pass;


    @staticmethod
    def clean_entry(entry):
        return entry;


    @classmethod
    def fetch_list(cls):

        cursor = Cursor();
        entries = cursor.select_all(cls.view_table_name);
        cursor.close();

        for entry in entries:
            entry = cls.clean_entry(entry);
        return entries;


    @classmethod
    def fetch_entry(cls, id=0):

        cursor = Cursor();
        entry = cursor.select_by_id(cls.view_table_name, id);
        cursor.close();
        cls.clean_entry(entry);
        return entry;


    @classmethod
    def save_entry(cls, submitted):

        submitted = cls.clean_submit(submitted);

        cursor = Cursor();

        if submitted["id"] == 0:
            cursor.insert_item(cls.submit_table_name, submitted);
        else:
            cursor.update_row(cls.submit_table_name,
                              submitted["id"], submitted);

        cursor.close();


    @staticmethod
    def clean_submit(submitted):
        submitted["id"] = int(submitted["id"]);
        return submitted;


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

