from dataclasses import dataclass
from .enums import FieldType


@dataclass
class AttribField:

    general_name: str
    label: str
    type_: FieldType = FieldType.TEXT

