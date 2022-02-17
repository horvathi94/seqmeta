from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.authors import AuthorsTable
from seqmeta.objects.author import Author


@dataclass
class View(Page):

    def render_content(self) -> "html":
        return render_template("authors/view.html",
                               authors=AuthorsTable.select_all())




@dataclass
class Edit(Page):

    author_id: int = None


    def __post_init__(self):
        self.author_id = int(self.author_id)


    def get_author(self) -> Author:
        if self.author_id == 0: return Author()
        return AuthorsTable.select(self.author_id)


    def render_content(self) -> "html":
        author = self.get_author()
        return render_template("authors/edit.html",
                               author_id = author.id,
                               form_fields=author.get_input_fields())
