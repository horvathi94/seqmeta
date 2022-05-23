from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page


@dataclass
class Editor(Page):

    template: "Template" = None


    def __post_init__(self):
        self.add_style("editor.css")
        self.add_script("fields.js")
        self.add_script("parsetemplate.js")
        self.add_script("templates-attribs.js")
        self.add_script("templates-cell.js")
        self.add_script("templates-row.js")
        self.add_script("templates-editor.js")
        self.add_script("import-ena.js")
        self.add_script("import-taxonomy.js")


    def render_content(self) -> "html":
        return render_template("templates/editor.html", template=self.template)
