from dataclasses import dataclass, field
from typing import List
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.templates import TemplatesTable


@dataclass
class Editor(Page):

    template_id: int = 0
    samples: List[int] = field(default_factory=lambda: [])


    def __post_init__(self):
        self.add_script("fields.js")
        self.add_script("parsetemplate.js")
        self.add_script("sampleeditor.js")
        self.styles.append("sampleeditor.css")


    @property
    def sample_ids(self) -> str:
        return ",".join([str(sid) for sid in self.samples])


    def render_content(self) -> "html":
        return render_template("samples/editor/editor.html",
                               template_id=self.template_id,
                               samples=self.sample_ids)
