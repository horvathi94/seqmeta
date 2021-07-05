from .base import SampleExtension


LIBRARY_LAYOUTS = [
    {
        "db_value": "",
        "db_save": None,
        "value": 0,
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

    display_table_name = "view_samples_library";
    submit_table_name = "samples_library";

    @classmethod
    def clean_submit(cls, entry):
        if "library_layout_paired" in entry:
            for layout in LIBRARY_LAYOUTS:
                if layout["value"] == int(entry["library_layout_paired"]):
                    entry["library_layout_paired"] = layout["db_save"];
                    break;
        if entry["library_preparation_date"] == "":
            entry["library_preparation_date"] = None;
        if entry["library_id"] == "":
            entry["library_id"] = None;
        if entry["insert_size"] == "":
            entry["insert_size"] = None;
        return entry;


    @classmethod
    def clean_entry(cls, entry):
        if "library_layout_paired" in entry:
            for layout in LIBRARY_LAYOUTS:
                if layout["db_value"] == entry["library_layout_paired"]:
                    entry["library_layout_paired"] = layout["value"];
                    break;
        if entry["insert_size"] == None:
            entry["insert_size"] = "";
        return entry;
