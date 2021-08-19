from flask import render_template
from application.src.pages.display import DisplayBase
from application.src.authors import Authors


class DisplayPage(DisplayBase):

    name_plural = "author groups";
    description = "Create author groups from registered authors. " \
        "These groups will appear in author enumeration fields.";
    editor_link = "author_groups_bp.edit";


    @classmethod
    def get_list(cls) -> list:
        return AuthorGroups.fetch_list();


    @classmethod
    def render_list(cls, items: list) -> "HTML":
        return render_template("author_groups/list.html", groups=items);


