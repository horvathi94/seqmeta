from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class View(Page):


    def render_content(self) -> "html":
        return render_template("templates/view.html")
