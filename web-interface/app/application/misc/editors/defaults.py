from flask import render_template
from application.src.defaults import DefaultValues
from application.src.fields import Field
from application.src.editor.dlist import DLIST


FIELDS = [

    "location_continent",
    "location_country",
    "location_region",
    "location_locality",
    "geo_loc_latitude",
    "geo_loc_longitude",
    "host",

    "originating_lab",
    "author_group",
    "sequencing_lab",
    "submitting_lab",

    "patient_status",
    "host_health_state",
    "host_anatomical_material",
    "host_body_product",
    "collection_device",
    "sampling_strategy",
    "specimen_source",
    "sample_capture_status",

    "sars_cov_2_diag_gene_name_1",
    "sars_cov_2_diag_gene_name_2",
    "purpose_of_sampling",
    "purpose_of_sequencing",

    "sequencing_instrument",
    "assembly_method",
    "sample_storage_conditions",
    "passage_number",
    "passage_method",

    "library_source",
    "library_strategy",
    "library_selection",
    "library_layout",
    "library_construction_protocol",
    "insert_size",

    ];


class Editor:


    @classmethod
    def field(cls, handle):
        dlist = DLIST[handle] if handle in DLIST else [];
        field = Field.fetch(handle);
        field["input"]["value"] = DefaultValues.fetch()[field["db_key"]];
        return render_template("defaults/field.html",
                               info=field, dlist=dlist);


    @classmethod
    def show(cls):
        html = render_template("defaults/head.html");
        for handle in FIELDS:
            html+= cls.field(handle);
        html+= render_template("defaults/tail.html");
        return html;
