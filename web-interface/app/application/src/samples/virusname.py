from jinja2 import Template
from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface

class VirusnameGisaid(DBInterface):

    display_table_name = "view_samples_gisaid";
    submit_table_name = "virusname_gisaid";
    save_procedure = "upsert_ordereddict_table";
    item_keys = ["key", "string"];
    items_table = "view_samples_gisaid";


    @classmethod
    def fetch_format_string(cls):
        virusname_format = Cursor.select("virusnames",
                                         clauses="WHERE item_key='gisaid'");
        return virusname_format[0]["item_value"];


    @classmethod
    def create_name(cls, sample):
        virusname = Template(cls.fetch_format_string());
        return virusname.render(sample);


    @classmethod
    def available_db_keys(cls):
        items = Cursor.column_names(cls.items_table);
        items.remove("sample_id");
        return items;


    @classmethod
    def call_save_procedure(cls, virusname):
        args = ("virusnames", 0, "gisaid", virusname);
        Cursor.call_procedure("upsert_dict_table", args=args, commit=True);


