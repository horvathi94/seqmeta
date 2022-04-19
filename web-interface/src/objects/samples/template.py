from dataclasses import dataclass, field, asdict
from typing import List
from .attribute import Attribute


@dataclass
class Template:

    id: int = None
    name: str = None
    attributes: List[Attribute] = field(default_factory=lambda: [])


    def __post_init__(self):
        if self.id is not None: self.id = int(self.id)


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)


    def asdict(self) -> dict:
        return asdict(self)


    def asjson(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "attributes": [a.asjson() for a in self.attributes]
        }

    @property
    def attribute_count(self) -> int:
        return len(self.attributes)
