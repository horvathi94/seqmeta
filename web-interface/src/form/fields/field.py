from dataclasses import dataclass
from enum import Enum


class FieldType(Enum):

    TEXT = "text"
    NUMBER = "number"



@dataclass
class Field:

    input_type: FieldType
    name: str = None
    label: str = None
    value: any = None
    required: bool = True
    minval: any = None
    maxval: any = None


    def __post_init__(self):
        self._format_label()
        if self.input_type == FieldType.TEXT:
            self._format_text_field()


    def _format_name(self) -> None:
        if self.name is None:
            self.name = self.label.lower().replace(" ", "_")


    def _format_label(self) -> None:
        if self.label is None:
            self.label = self.name.capitalize().replace("_", " ")


    def _format_text_field(self) -> None:
        if self.value is None: self.value = ""
        else: self.value = str(self.value)
        if self.minval is not None: self.minval = int(self.minval)
        if self.maxval is not None: self.maxval = int(self.maxval)


    @property
    def type(self) -> str:
        return self.input_type.value
