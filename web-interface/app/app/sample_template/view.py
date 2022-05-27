from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.sample_template import SampleTemplate


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css")


    def render_content(self) -> "html":
        return render_template("templates/view.html",
                               templates=SampleTemplate.list_all())
