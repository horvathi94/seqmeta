from flask import Blueprint, request, jsonify
from .authors import View as ViewAuthors, Edit as EditAuthors
from seqmeta.objects.author import Author
from seqmeta.database.authors import AuthorsTable


authors_bp = Blueprint("authors_bp", __name__, template_folder="templates")


@authors_bp.route("/authors")
@authors_bp.route("/authors/view")
def view():
    page = ViewAuthors()
    return page.render()


@authors_bp.route("/authors/<aid>")
def edit(aid: int):
    editor = EditAuthors(author_id=aid)
    return editor.render()


@authors_bp.route("/authors/<aid>/save", methods=["POST"])
def save(aid: int):
    data = dict(request.form)
    data["id"] = aid
    author = Author(**data)
    atab = AuthorsTable()
    atab.save(author)
    return jsonify(data)
