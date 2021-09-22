from flask import render_template
from application.src.samples.samples import Samples
from application.src.pages.editor import EditorBase
from application.src.fields.dbfield import DBField
from application.src.fields.sample_fields import SampleFields

import sys


class MultiEditor(EditorBase):

    styles = [{"filename": "add-multiple.css", "prefix": "samples"},
              {"filename": "markers.css"},
              {"filename": "tooltips.css"},
              {"filename": "info.css"}];
    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"},
               {"filename": "import-data.js", "prefix": "samples"}];

    form_type = "edit"


    @classmethod
    def header_col(cls, field: "Field") -> "HTML":
       return render_template("samples/form/multi/col_head.html", field=field);


    @classmethod
    def all_col(cls, field: "Field") -> "HTML":
        if field.field_type in ["text", "number", "date"]:
            field.input.onchange = "updateColumn(this);";
        return render_template("samples/form/multi/col_all.html", field=field);


    @classmethod
    def template_col(cls, field: "Field") -> "HTML":
        val = field.get_value();
        if field.field_type == "seqfile":
            field.input.value = val.get_display_name();
            ftype = val.file_extension_id;
            return render_template("samples/form/multi/col_template.html",
                               field=field, ftype=ftype);
        field.input.value = val;
        if field.handle_std == SampleFields.SAMPLE_NAME:
            field.input.onchange = "checkSampleNames();";
        elif field.handle_std == SampleFields.LIBRARY_ID:
            field.input.onchange = "checkLibraryNames();";
        return render_template("samples/form/multi/col_template.html",
                               field=field);


    @classmethod
    def sample_col(cls, field: "Field", sample: Samples) -> "HTML":
        val = field.get_value_from_sample(sample);

        if field.field_type == "seqfile":
            field.input.value = val.get_display_name();
            ftype = val.file_extension_id;
            return render_template("samples/form/multi/col_template.html",
                                   field=field, ftype=ftype);

        field.input.value = val;
        if field.handle_std == SampleFields.SAMPLE_NAME:
            field.input.onchange = "checkSampleNames();";
        elif field.handle_std == SampleFields.LIBRARY_ID:
            field.input.onchange = "checkLibraryNames();";
        return render_template("samples/form/multi/col_sample.html",
                               field=field);


    @classmethod
    def render_row(cls, cols: list=[],
                   classes: list=[], style: str="") -> "HTML":
        tr = "<tr class='"+ " ".join(classes) + "' style='" + style + "'>"
        return tr + " ".join(cols)+"</tr>";


    @classmethod
    def list_header_row(cls) -> list:
        row = [];
        for fd in SampleFields.list_for_editor():
            field = DBField.get_field(fd);
            row.append(cls.header_col(field));
        return row;


    @classmethod
    def list_template_row(cls) -> list:
        row = [];
        for fd in SampleFields.list_for_editor():
            field = DBField.get_field(fd);
            row.append(cls.template_col(field));
        return row;


    @classmethod
    def list_all_row(cls) -> list:
        row = [];
        for fd in SampleFields.list_for_editor():
            field = DBField.get_field(fd);
            row.append(cls.all_col(field));
        return row;


    @classmethod
    def list_sample_row(cls, sample_id: int=0) -> list:
        row = [];
        sample = Samples.fetch("view_samples_base", sample_id);
        for fd in SampleFields.list_for_editor():
            field = DBField.get_field(fd);
            field.input.replace_id_in_template_name(sample_id);
            row.append(cls.sample_col(field, sample=sample));
        return row;


    @classmethod
    def render_fields(cls, sample_ids: list=[]) -> "HTML":
        header_row = cls.list_header_row();
        template_row = cls.list_template_row();
        all_row = cls.list_all_row();

        sample_rows = [];
        for sample_id in sample_ids:
            sample_rows.append(cls.list_sample_row(sample_id=sample_id));

        html = cls.render_row(header_row);
        html+= cls.render_row(all_row, classes=["editor", "row", "all"]);
        html+= cls.render_row(template_row,
                              classes=["editor", "row", "template"],
                              style="visibility: collapse;");

        for sample_row in sample_rows:
            html+= cls.render_row(sample_row);

        return html;


    @classmethod
    def render_editor_head(cls) -> "HTML":
        reg_samples = Samples.fetch_list();
        return render_template("samples/form/multi/head.html",
                               form_type=cls.form_type,
                               reg_samples=reg_samples);


    @classmethod
    def render_editor_tail(cls) -> "HTML":
        return render_template("samples/form/multi/tail.html");


    @classmethod
    def render_editor(cls, sample_ids: list=[]) -> "HTML":
        html = cls.render_editor_head();
        html+= cls.render_fields(sample_ids=sample_ids);
        html+= cls.render_editor_tail();
        return html;


    @classmethod
    def empty_selection(cls) -> "HTML":
        return "<p><strong>Nothing selected</strong></p>";


    @classmethod
    def render_page(cls, sample_ids: list=[]) -> "HTML":
        if len(sample_ids) == 0:
            return cls.empty_selection();
        return cls.render_editor(sample_ids=sample_ids);




class MultiEditorAdd(MultiEditor):

    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"},
               {"filename": "import-data.js", "prefix": "samples"}];

    form_type = "add";

    @classmethod
    def render_page(cls, sample_ids: list=[]) -> "HTML":
        return cls.render_editor(sample_ids=sample_ids);
