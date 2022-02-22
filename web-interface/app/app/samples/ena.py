from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class Ena(Page):

    def __post_init__(self):
        self.scripts.append("ena.js")
        self.styles.append("ena.css")


    def render_content(self) -> "html":
        return render_template("samples/ena.html")
