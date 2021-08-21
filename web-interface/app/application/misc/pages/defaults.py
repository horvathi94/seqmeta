from flask import render_template, redirect, url_for
from application.src.defaults import DefaultValues
#from application.src.fields import Field
#from application.src.editor.dlist import get_dlist

from application.src.pages.editor import EditorBase
from application.src.fields_new.dbfield import DBField
from application.src.fields_new.sample_fields import SampleFields



class DefaultsEditor(EditorBase):

    styles = [{"filename": "markers.css"}];


    @classmethod
    def render_field(cls, field_handle: SampleFields) -> "HTML":
        field = DBField.get_field(field_handle);
        field.input.value = field.get_value(sample_id=0);
        return render_template("defaults/field.html", field=field);


    @classmethod
    def render_editor(cls, item_id: int=0) -> "HTML":
        html = render_template("defaults/head.html");
        for handle in SampleFields.list_for_defaults():
            html+= cls.render_field(handle);
        html+= render_template("defaults/tail.html");
        return html;


    @classmethod
    def field(cls, handle) -> "HTML":
        dlist = get_dlist(handle);
        field = Field.fetch(handle);
        field["input"]["value"] = DefaultValues.fetch()[field["db_key"]];
        return render_template("defaults/field.html",
                               info=field, dlist=dlist);


    @classmethod
    def save(cls, submitted: "request.form") -> "flask.redirect":
        DefaultValues.save(submitted.to_dict());
        return redirect(url_for("misc_bp.edit_default_values"));
