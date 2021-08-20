from flask import render_template
from application.src.pages.editor import EditorBase
from .editor_fields import EDITOR_FIELDS



from flask import jsonify
from application.src.fields_new.dbfield import DBField
from application.src.fields_new.field import Field
from application.src.fields_new.sample_fields import SampleFields

import sys


class Editor(EditorBase):

    styles = [{"filename": "edit.css", "prefix": "samples"},
              {"filename": "markers.css"}];
    scripts = [{"filename": "validate-sample-name.js", "prefix": "samples"},
               {"filename": "edit-sample.js", "prefix": "samples"}];



    @classmethod
    def render_field(cls, field_handle: SampleFields,
                     sample_id: int) -> "HTML":
        field = DBField.get_field(field_handle);
        field.input.value = field.get_value(sample_id=sample_id);

        return render_template("samples/form/single/field_new.html",
                               info=field);


    @classmethod
    def render_fields(cls, sample_id: int) -> "HTML":
        html = "";
        for field in SampleFields.list_for_editor():
            print(f"Field: {field}");
            html+= cls.render_field(field, sample_id);
        return html;


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":

        html = render_template("samples/form/single/head.html",
                               sample_id=item_id);

        html+= cls.render_fields(item_id);
        html+= render_template("samples/form/single/tail.html");
        return html;


    @classmethod
    def test(cls):
        fd = SampleFields.SAMPLE_NAME;
        testval = DBField.get_field(fd);
        dl = testval.get_options_list()
        print(dl, file=sys.stderr)
