from dataclasses import dataclass, field
from typing import List
from flask import render_template
from seqmeta.page import Page


@dataclass
class Editor(Page):

    template_name: str = None
    samples: List[int] = field(default_factory=lambda: [])


    def __post_init__(self):
        self.add_script("fields.js")
        self.add_script("parsetemplate.js")
        self.add_script("samplefields.js")
        self.add_script("sampleeditor.js")
        self.styles.append("sampleeditor.css")


    @property
    def sample_names(self) -> str:
        return ",".join(self.samples)


    def render_content(self) -> "html":
        return render_template("samples/editor.html",
                               template_name=self.template_name,
                               samples=self.sample_names)
