from flask import render_template
from application.src.pages.display import DisplayBase
from application.src.institutions import Institutions



class DisplayPage(DisplayBase):

    name_plural = "institutions";
    description = "Register organizations and instutions, " \
        "who have contributed in the collection of the samples, " \
        "the sequencing of the samples or in the submissions of the samples."
    editor_link = "institutions_bp.edit";


    @classmethod
    def get_list(cls) -> list:
        return Institutions.fetch_list();


    @classmethod
    def render_list(cls, items: list) -> "HTML":
        return render_template("institutions/list.html", institutions=items);


