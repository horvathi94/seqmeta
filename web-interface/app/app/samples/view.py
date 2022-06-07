from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.sample_template import SampleTemplate
from seqmeta.objects.sample import Sample


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css");
        self.add_script("samples-view.js")


    @property
    def templates(self) -> List["Template"]:
        return SampleTemplate.list_names()


    def render_content(self) -> "html":
        return render_template("samples/view.html", templates=self.templates)
