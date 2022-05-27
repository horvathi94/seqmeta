from dataclasses import dataclass, field
from typing import List
from .pickle import PickleFile
from .taxonomy import Taxonomy
from .attributes.attr_field import AttributeField


@dataclass
class SampleTemplate(PickleFile):

    name: str
    description: str = "No description available."
    extenstions: str = "template"
    fields: List[AttributeField] = field(default_factory=lambda: [])


