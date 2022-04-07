from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.templates import TemplatesTable


@dataclass
class Editor(Page):

    template_id: int = 0

    def __post_init__(self):
        self.scripts.append("sampleeditor.js")
        self.styles.append("sampleeditor.css")


    @property
    def template(self) -> "Template":
        if self.template_id == 0:
            return None
        return TemplatesTable.select(self.template_id)


    def render_content(self) -> "html":
        return render_template("samples/editor/editor.html",
                               template=self.template)
