from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
#from seqmeta.database.templates import TemplatesTable
from seqmeta.objects.samples.template import list_templates


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css")


    @property
    def templates(self) -> List["Template"]:
        return list_templates()


    def render_content(self) -> "html":
        return render_template("templates/view.html", templates=self.templates)
