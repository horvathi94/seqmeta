from application.src.db.cursor import Cursor
from .base import SampleExtension
from application.src.misc.library import LibraryLayouts



class Library(SampleExtension):

    display_table_name = "view_samples_library";
    submit_table_name = "samples_library";


    clean_keys_strings = ["library_id",
                          "library_preparation_date",
                          "library_design_description",
                          "library_construction_protocol"];

    clean_keys_numbers = ["insert_size"];

    clean_keys_select = ["library_layout_paired",
                         "library_source_id",
                         "library_selection_id",
                         "library_strategy_id"];


    @classmethod
    def extra_clean_submitted(cls, entry: dict) -> dict:
        key = "library_layout_paired";
        if not key in entry:
            return entry;
        lay = LibraryLayouts.get_item_from_value(entry[key]);
        entry[key] = lay.dbsave;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for key in cls.clean_keys_strings:
            entry = cls.clean_fetched_string(entry, key);
        for key in cls.clean_keys_numbers:
            entry = cls.clean_fetched_number(entry, key);

        key = "library_layout_paired";
        if not key in entry: return entry;
        lay = LibraryLayouts.get_item_from_dbvalue(entry[key]);
        entry[key] = lay.value;
        return entry;


    @classmethod
    def select_library_ids(cls):
        return Cursor.select(cls.display_table_name, fields=["library_id"]);
