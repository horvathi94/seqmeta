from dataclasses import dataclass
from flask import render_template
from seqmeta.page import Page
from seqmeta.database.groups import GroupsTable
from seqmeta.database.authors import AuthorsTable
from seqmeta.objects.group import Group


@dataclass
class View(Page):

    def render_content(self) -> "html":
        return render_template("groups/view.html",
                               groups=GroupsTable.select_all())


@dataclass
class Edit(Page):

    group_id: int = None


    def __post_init__(self):
        self.group_id = int(self.group_id)
        self.styles.append("editor.css")
        self.scripts.append("editor.js")


    def get_group(self) -> Group:
        if self.group_id == 0: return Group()
        return GroupsTable.select(self.group_id)


    def render_content(self) -> "html":
        group = self.get_group()
        return render_template("groups/edit.html",
                               group_id=self.group_id,
                               group=group,
                               authors_list=AuthorsTable.select_all(),
                               form_fields=group.get_input_fields())
