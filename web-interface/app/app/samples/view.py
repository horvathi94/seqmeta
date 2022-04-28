from dataclasses import dataclass
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.template import SampleTemplate
from seqmeta.objects.sample import Sample


@dataclass
class View(Page):


    def __post_init__(self):
        self.add_style("view.css");


    @property
    def templates(self) -> List["Template"]:
        templates = SampleTemplate.list_all()
        return [t.name for t in templates]


    @property
    def samples(self) -> List["Sample"]:
        return Sample.list_all()


    def render_content(self) -> "html":
        return render_template("samples/view/page.html",
                               templates=self.templates,
                               samples=self.samples)
