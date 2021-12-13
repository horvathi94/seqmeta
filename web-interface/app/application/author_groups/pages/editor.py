from flask import render_template
from application.src.pages.editor import EditorBase
from application.src.authors import AuthorGroups, Authors


class EditorPage(EditorBase):

    scripts = [{"filename":"edit.js", "prefix":"author-groups"}]
    styles = [{"filename": "group-editor.css", "prefix": "author-groups"},
              {"filename": "smbasicform.css"}]


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":
        """Return author group editor."""

        group = AuthorGroups.fetch_entry_edit(group_id=item_id)
        authors_list = Authors.fetch_list()
        html = render_template("author_groups/edit.html", group=group,
                               authors_list=authors_list)
        return html
