from flask import render_template
from application.src.samples.samples import Samples
from application.src.pages.editor import EditorBase
from application.src.fields_new.dbfield import DBField
from application.src.fields_new.sample_fields import SampleFields

import sys


class MultiEditor(EditorBase):

    styles = [{"filename": "add-multiple.css", "prefix": "samples"},
              {"filename": "markers.css"},
              {"filename": "tooltips.css"},
              {"filename": "info.css"}];
    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"}];

    form_type = "edit"


    @classmethod
    def header_col(cls, field: "Field") -> "HTML":
       return render_template("samples/form/multi/col_head.html", field=field);


    @classmethod
    def all_col(cls, field: "Field") -> "HTML":
        print(f"Field: {field}", file=sys.stderr)
        return render_template("samples/form/multi/col_all.html", field=field);


    @classmethod
    def render_row(cls, cols: list=[], classes: list=[]) -> "HTML":
        return "<tr class='"+ " ".join(classes) +"'>" + " ".join(cols)+"</tr>";


    @classmethod
    def render_fields(cls, sample_ids: list=[]) -> "HTML":
        header_row = [];
        template_row = [];
        all_row = [];

        for fd in SampleFields.list_for_editor():
            field = DBField.get_field(fd);
            header_row.append(cls.header_col(field));
            all_row.append(cls.all_col(field));

        html = cls.render_row(header_row);
        html+= cls.render_row(all_row, classes=["editor", "raw", "all"]);

        return html;


    @classmethod
    def render_editor_head(cls) -> "HTML":
        reg_samples = [];
        if cls.form_type == "add":
            reg_samples = Samples.fetch_list();
        return render_template("samples/form/multi/head.html",
                               form_type=cls.form_type,
                               reg_samples=reg_samples);


    @classmethod
    def render_editor_tail(cls) -> "HTML":
        return render_template("samples/form/single/tail.html");


    @classmethod
    def render_editor(cls, sample_ids: list=[]) -> "HTML":
        html = cls.render_editor_head();
        html+= cls.render_fields();
        html+= cls.render_editor_tail();
        return html;


    @classmethod
    def show(cls, sample_ids: list=[]) -> "HTML":
        """Returns HTML of basic editor."""
        html = render_template("head.html", styles=cls.styles);
        html+= cls.render_editor(sample_ids=sample_ids);
        html+= render_template("footer.html", scripts=cls.scripts);
        return html;




class MultiEditorAdd(MultiEditor):

    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"},
               {"filename": "import-data.js", "prefix": "samples"}];

    form_type = "add";
