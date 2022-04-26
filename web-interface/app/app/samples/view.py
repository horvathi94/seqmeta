from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.samples.templates import TemplatesList, SamplesList


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css");


    @property
    def templates(self) -> List["Template"]:
        tl = TemplatesList()
        return tl.load_names()


    @property
    def samples(self) -> List["Sample"]:
        sl = SamplesList()
        return sl.load()


    def render_content(self) -> "html":
        return render_template("samples/view/page.html",
                               templates=self.templates,
                               samples=self.samples)
