from .base import SampleExtension


LIBRARY_LAYOUTS = [
    {
        "db_value": "",
        "db_save": None,
        "value": 1000,
        "label": "N/A"
    },
    {
        "db_value": 1,
        "db_save": True,
        "value": 1,
        "label": "Paired-End"
    },
    {
        "db_value": 0,
        "db_save": False,
        "value": 2,
        "label": "Single"
    },
];


class Library(SampleExtension):

    submit_table_name = "samples_library";

    @classmethod
    def clean_submit(cls, entry):
        for layout in LIBRARY_LAYOUTS:
            if layout["value"] == int(entry["layout_paired"]):
                entry["layout_paired"] = layout["db_save"];
                break;
        if entry["preparation_date"] == "":
            entry["preparation_date"] = None;
        if entry["lib_id"] == "":
            entry["lib_id"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        for layout in LIBRARY_LAYOUTS:
            if layout["db_value"] == entry["library_layout_paired"]:
                entry["library_layout_paired"] = layout["value"];
                break;
        return entry;
