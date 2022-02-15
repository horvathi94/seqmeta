from flask import render_template
from dataclasses import dataclass, field
from typing import List


@dataclass
class Page:

    title: str = "Page title"
    styles: List[str] = field(default_factory=lambda: ["main.css"])
    scripts: List[str] = field(default_factory=lambda: [])


    def render_head(self) -> "html":
        return render_template("head.html",
                               title=self.title,
                               styles=self.styles)


    def render_content(self) -> "html":
        return "<p>Content placeholder</p>"


    def render_end(self) -> "html":
        return render_template("end.html")


    def render(self) -> "html":
        html = self.render_head()
        html+= self.render_content()
        html+= self.render_end()
        return html
