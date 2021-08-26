from flask import render_template, redirect, url_for
from application.src.defaults import DefaultValues
from application.src.pages.editor import EditorBase
from application.src.fields.dbfield import DBField
from application.src.fields.sample_fields import SampleFields


class DefaultsEditor(EditorBase):

    styles = [{"filename": "markers.css"}];


    @classmethod
    def render_field(cls, field_handle: SampleFields) -> "HTML":
        field = DBField.get_field(field_handle);
        field.input.value = field.get_value(sample_id=0);
        if field.field_type == "seqfile_assembly":
            field.input.db_key = field.handle_std.value;
        return render_template("defaults/field.html", field=field);


    @classmethod
    def render_editor(cls) -> "HTML":
        html = render_template("defaults/head.html");
        for handle in SampleFields.list_for_defaults():
            html+= cls.render_field(handle);
        html+= render_template("defaults/tail.html");
        return html;


    @classmethod
    def render_page(cls):
        return cls.render_editor();


    @classmethod
    def save(cls, submitted: "request.form") -> "flask.redirect":
        DefaultValues.save(submitted.to_dict());
        return redirect(url_for("misc_bp.edit_default_values"));
