from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class Editor(Page):


    def __post_init__(self):
        self.scripts.append("templates.js")
        self.styles.append("editor.css")


    def render_content(self) -> "html":
        return render_template("templates/editor.html")
