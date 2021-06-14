from .base import SampleExtension
from .radios import LIBRARY_LAYOUTS

class Library(SampleExtension):

    submit_table_name = "samples_library";

    @classmethod
    def clean_submit(cls, entry):
        for layout in LIBRARY_LAYOUTS:
            if layout["value"] == int(entry["layout_paired"]):
                entry["layout_paired"] = layout["db_value"];
                break;
        if entry["preparation_date"] == "":
            entry["preparation_date"] = None;
        if entry["lib_id"] == "":
            entry["lib_id"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for layout in LIBRARY_LAYOUTS:
            if layout["db_value"] == entry["layout_paired"]:
                entry["layout_paired"] = layout["value"];
                break;
        return entry;
