from application.src.db.cursor import Cursor
from .base import SampleExtension
from application.src.misc import LibraryLayouts



class Library(SampleExtension):

    display_table_name = "view_samples_library";
    submit_table_name = "samples_library";

    @classmethod
    def clean_submit(cls, entry):
        lay = LibraryLayouts.get_item_from_value(
            entry["library_layout_paired"]);
        entry["library_layout_paired"] = lay.dbsave;
        if entry["library_id"] == "":
            entry["library_id"] = None;
        if entry["library_preparation_date"] == "":
            entry["library_preparation_date"] = None;
        if entry["library_id"] == "":
            entry["library_id"] = None;
        if entry["insert_size"] == "":
            entry["insert_size"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        lay = LibraryLayouts.get_item_from_dbvalue(
            entry["library_layout_paired"]);
        entry["library_layout_paired"] = lay.value;
        if entry["library_id"] == None:
            entry["library_id"] = "";
        if "insert_size" in entry:
            if entry["insert_size"] == None:
                entry["insert_size"] = "";
        return entry;

    @classmethod
    def select_library_ids(cls):
        return \
            Cursor.select(cls.display_table_name, fields=["library_id"]);
