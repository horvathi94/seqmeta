from dataclasses import dataclass, field
from typing import List


@dataclass
class Sample:

    id: int = None
    name: str = None
    template_id: int = None
    attributes: dict = field(default_factory=lambda: {})
    short_description: str = None


    def add_attribute(self, name: str, val: any) -> None:
        if name in self.attributes: return
        self.attributes[name] = val
