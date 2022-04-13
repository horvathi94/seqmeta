from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class Editor(Page):

    template_id: int = 0


    def __post_init__(self):
        self.styles.append("editor.css")
        self.add_script("fields.js")
        self.add_script("templates.js")
        self.add_script("ena.js")
        self.add_script("importena.js")
        if self.template_id is None: self.template_id = 0


    def render_content(self) -> "html":
        return render_template("templates/editor.html",
                               template_id=self.template_id)
