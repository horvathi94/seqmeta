from flask import render_template
from dataclasses import dataclass
from seqmeta.page import Page


@dataclass
class Index(Page):


    def __post_init__(self):
        self.title = "Index"


    def render_content(self) -> "html":
        return render_template("index.html")
