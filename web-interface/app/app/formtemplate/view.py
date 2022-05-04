from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.template import SampleTemplate


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css")


    @property
    def templates(self) -> List["Template"]:
        return SampleTemplate.list_all()


    def render_content(self) -> "html":
        return render_template("templates/view.html", templates=self.templates)
