from flask import Blueprint, request, redirect, url_for
from .authors import View as ViewAuthors, Edit as EditAuthors
from .groups import View as ViewGroups, Edit as EditGroups
from seqmeta.objects.author import Author
from seqmeta.objects.group import Group
from seqmeta.database.authors import AuthorsTable
from seqmeta.database.groups import GroupsTable


authors_bp = Blueprint("authors_bp", __name__, template_folder="templates")

# ------ Authors
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
    data["id"] = int(aid)
    author = Author(**data)
    AuthorsTable.save(author)
    return redirect(url_for("authors_bp.view"))



# ------ Groups
@authors_bp.route("/groups")
@authors_bp.route("/groups/view")
def view_groups():
    page = ViewGroups()
    return page.render()


@authors_bp.route("/groups/<gid>")
def edit_group(gid: int):
    page = EditGroups(group_id=gid)
    return page.render()


@authors_bp.route("/groups/<gid>/save", methods=["POST"])
def save_group(gid: int):
    data = dict(request.form)
    data["id"] = int(gid)
    group = Group.create_from_form(data)
    GroupsTable.save(group)
    return redirect(url_for("authors_bp.view_groups"))
