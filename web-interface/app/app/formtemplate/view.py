from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.templates import TemplatesTable


@dataclass
class View(Page):

    def __post_init__(self):
        self.add_style("view.css")


    def render_content(self) -> "html":
        templates = TemplatesTable.select_all()
        return render_template("templates/view.html", templates=templates)
