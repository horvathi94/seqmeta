from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.templates import TemplatesTable
from seqmeta.database.samples import SamplesTable


@dataclass
class View(Page):


    def render_content(self) -> "html":
        templates = TemplatesTable.select_all()
        samples = SamplesTable.select_all()
        return render_template("samples/view/page.html",
                               templates=templates,
                               samples=samples)
