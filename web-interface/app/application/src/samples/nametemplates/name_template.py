from jinja2 import Template
from application.src.db.cursor import Cursor
from application.src.db.interface import DBInterface
from application.src.samples.samples import Samples

class NameTemplate(DBInterface):

    display_table_name = "";
    submit_table_name = "virusnames";
    save_procedure = "upsert_dict_table";
    dict_key = "";


    @classmethod
    def fetch_format_string(cls):
        virusname_format = Cursor.select(
            cls.submit_table_name,
            clauses="WHERE item_key='{:s}'".format(cls.dict_key));
        return virusname_format[0]["item_value"];


    @classmethod
    def create_name(cls, sample):
        virusname = Template(cls.fetch_format_string());
        return virusname.render(sample);


    @classmethod
    def available_db_keys(cls):
        items = Cursor.column_names(cls.display_table_name);
        items.remove("sample_id");
        return items;


    @classmethod
    def call_save_procedure(cls, virusname):
        args = (cls.submit_table_name, 0, cls.dict_key, virusname);
        Cursor.call_procedure(cls.save_procedure, args=args, commit=True);



    @classmethod
    def format_name(cls, sample_id):
        sample = Samples.fetch(cls.display_table_name, sample_id);
        return cls.create_name(sample);
