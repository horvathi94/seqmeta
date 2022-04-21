from dataclasses import dataclass, field, asdict
from typing import List
from seqmeta.database.templates import TemplatesTable





@dataclass
class Sample:

    id: int = None
    name: str = None
    template_id: int = None
    attributes: dict = field(default_factory=lambda: {})
    short_description: str = None
    status: str = None


    def __post_init__(self):
        if self.status == "new": self.id = 0


    def add_attribute(self, name: str, value: any) -> None:
        if name in self.attributes: return
        if value is not None: value = value.strip()
        self.attributes[name] = value if value != "" else None


    @property
    def template_name(self) -> str:
        return TemplatesTable.select(self.template_id).name


    def asdict(self) -> dict:
        return {
            "name": self.name,
            "template_id": self.template_id,
            "short_description": self.short_description
        }


    def asjson(self) -> dict:
        return asdict(self)
