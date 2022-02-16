from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.authors import AuthorsTable
from seqmeta.objects.author import Author


@dataclass
class View(Page):


    def list_authors(self) -> list:
        at = AuthorsTable()
        return at.get_authors()


    def render_content(self) -> "html":
        return render_template("authors/view.html",
                               authors=self.list_authors())




@dataclass
class Edit(Page):

    author_id: int = None


    def __post_init__(self):
        self.author_id = int(self.author_id)


    def get_author(self):
        if self.author_id == 0: return Author()
        at = AuthorsTable()
        return at.select_author(self.author_id)


    def render_content(self) -> "html":
        author = self.get_author()
        return render_template("authors/edit.html",
                               author_id = author.id,
                               form_fields=author.get_input_fields())
