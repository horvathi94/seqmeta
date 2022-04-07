from flask import render_template
from dataclasses import dataclass, field
from typing import List


@dataclass
class Page:

    title: str = "Page title"
    styles: List[str] = field(default_factory=lambda: ["main.css"])
    scripts: List[str] = field(default_factory=lambda: [])


    def add_style(self, stylessheet: str) -> None:
        if stylesheet not in self.styles:
            self.styles.append(stylesheet)


    def add_script(self, script: str) -> None:
        if script not in self.scripts:
            self.scripts.append(script)


    def render_head(self) -> "html":
        return render_template("head.html",
                               title=self.title,
                               styles=self.styles)


    def render_content(self) -> "html":
        return "<p>Content placeholder</p>"


    def render_end(self) -> "html":
        return render_template("end.html",
                               scripts=self.scripts)


    def render(self) -> "html":
        html = self.render_head()
        html+= self.render_content()
        html+= self.render_end()
        return html
