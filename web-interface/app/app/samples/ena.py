from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.objects.template import SampleTemplate
from seqmeta.objects.sample import Sample


@dataclass
class ENA(Page):


    def __post_init__(self):
        self.add_script("samplesview.js")
        self.add_style("view.css");



    def render_content(self) -> "html":
        return render_template("samples/ena.html", templates=self.templates)
