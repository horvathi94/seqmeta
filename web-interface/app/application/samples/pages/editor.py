from flask import render_template
from application.src.pages.editor import EditorBase
from .editor_fields import EDITOR_FIELDS



from flask import jsonify
from application.src.fields_new.field import DBField, SampleFields


class Editor(EditorBase):

    styles = [{"filename": "edit.css", "prefix": "samples"},
              {"filename": "markers.css"}];
    scripts = [{"filename": "validate-sample-name.js", "prefix": "samples"},
               {"filename": "edit-sample.js", "prefix": "samples"}];



    @classmethod
    def render_field(cls) -> "HTML":
        pass;


    @classmethod
    def render_fields(cls) -> "HTML":
        html = "";
        for field in EDITOR_FIELDS:
            html+= render_field(field);
        return html;


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":

        html = render_template("samples/form/single/head.html",
                               sample_id=item_id);

        html+= cls.render_fields();
        html+= render_template("samples/form/single/tail.html");
        return html;


    @classmethod
    def test(cls):
        fd = SampleFields.COLLECTOR_NAME;
        testval = DBField.get_field(fd);
        testval = jsonify(testval)
        return testval;
