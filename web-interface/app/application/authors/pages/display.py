from flask import render_template
from application.src.pages.display import DisplayBase
from application.src.authors import Authors


class DisplayPage(DisplayBase):

    name_plural = "authors";
    description = "Here you can register anyone who has helped in obtaining " \
     "the sequences: the sample collector, the laboratory staff, the" \
     "bioinformaticians, etc."
    editor_link = "authors_bp.edit";


    @classmethod
    def get_list(cls) -> list:
        return Authors.fetch_list();


    @classmethod
    def render_list(cls, items: list) -> "HTML":
        return render_template("authors/list.html", authors=items);


