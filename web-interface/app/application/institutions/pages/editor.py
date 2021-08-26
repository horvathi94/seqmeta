from flask import render_template
from application.src.pages.editor import EditorBase
from application.src.institutions import Institutions
from application.src.misc.location import Countries


class EditorPage(EditorBase):

    styles = [{"filename": "smbasicform.css"}];


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":
        institution = Institutions.fetch_entry(id=item_id);
        html = render_template("institutions/edit.html",
                               institution=institution,
                               countries=Countries.fetch_list());
        return html;
