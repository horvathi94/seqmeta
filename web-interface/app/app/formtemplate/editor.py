from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class Editor(Page):


    def __post_init__(self):
        self.styles.append("editor.css")
        self.add_script("templates.js")
        self.add_script("ena.js")
        self.add_script("importena.js")


    def render_content(self) -> "html":
        return render_template("templates/editor.html")
