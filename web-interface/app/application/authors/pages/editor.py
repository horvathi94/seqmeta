from flask import render_template
from application.src.pages.editor import EditorBase
from application.src.authors import Authors


class EditorPage(EditorBase):

    styles = [{"filename": "smbasicform.css"}];


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":
        """Return author editor."""
        author = Authors.fetch_entry_edit(id=item_id);
        html = render_template("authors/edit.html", author=author);
        return html;
