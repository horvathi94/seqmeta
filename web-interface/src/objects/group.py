from dataclasses import dataclass, field
from typing import List, Dict
from .author import Author
from seqmeta.form.fields.field import Field, FieldType
from seqmeta.database.authors import AuthorsTable


@dataclass
class AuthorInGroup:

    author: Author
    order: int


    @property
    def nametag(self) -> str:
        return self.author.full_name



class AuthorIter:

    def __init__(self, authors: List[AuthorInGroup]):
        self._index = 0
        self._last_order = -1
        self._authors = authors


    def __next__(self):
        if self._index >= len(self._authors):
            raise StopIteration

        self._index += 1
        orders_list = [a.order for a in self._authors]
        orders = list(filter(lambda oi: oi > self._last_order, orders_list))
        o = min(orders)

        author = None
        for a in self._authors:
            if a.order == o:
                author = a
                self._last_order = o
        return author



@dataclass
class Group:

    id: int = 0
    name: str = None
    authors: List[AuthorInGroup] = field(default_factory=lambda: [])

    def __post_init__(self):
        self.id = int(self.id)


    def __iter__(self):
        return AuthorIter(self.authors)


    def add_author(self, author: Author, order: int) -> None:
        orders =[a.order for a in self]
        if order in orders: order = max(orders) + 1
        author = AuthorInGroup(author=author, order=order)
        self.authors.append(author)


    @property
    def members_count(self) -> int:
        return len(self.authors)


    @property
    def display_members(self) -> str:
        return ", ".join([a.nametag for a in self.authors])


    @property
    def name_field(self) -> Field:
        return Field(input_type=FieldType.TEXT,
                     name="name",
                     label="Group name",
                     value=self.name,
                     maxval=100)


    def get_input_fields(self) -> List[Field]:
        return [self.name_field]



    @staticmethod
    def create_from_form(data: dict) -> "Group":
        group_data = {"id": data.pop("id"), "name": data.pop("name")}
        group = Group(**group_data)

        authors_data = []
        for raw_key, raw_val in data.items():
            general_key, row_index, key = raw_key.split("+")
            if general_key != "author": continue

            row_index = int(row_index)
            if row_index == 0: continue

            is_registered = False
            for a in authors_data:
                if a["row_index"] == row_index:
                    a[key] = int(raw_val)
                    is_registered = True
                    break

            if is_registered: continue
            authors_data.append({"row_index": row_index, key: int(raw_val)})

        for ad in authors_data:
            author = AuthorsTable.select(ad["id"])
            group.add_author(author, ad["order"])

        return group
