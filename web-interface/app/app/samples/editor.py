from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.templates import TemplatesTable


@dataclass
class Editor(Page):


    @property
    def template(self) -> "Template":
        return TemplatesTable.select(6)


    def render_content(self) -> "html":
        return render_template("samples/editor/editor.html",
                               template=self.template)
