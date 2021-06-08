from .base import SampleExtension


class Library(SampleExtension):

    submit_table_name = "samples_library";

    @classmethod
    def clean_submit(cls, entry):
        if entry["layout_paired"] == "":
            entry["layout_paired"] = None;
        elif entry["layout_paired"]:
            entry["layout_paired"] = True;
        else:
            entry["layout_paired"] = False;
        return entry;
