from dataclasses import dataclass
from typing import List
from seqmeta.form.fields.field import Field, FieldType


@dataclass
class Author:

    id: int = 0
    first_name: str = None
    last_name: str = None
    middle_name: str = None


    def __post_init__(self):
        self.id = int(self.id)
        if self.middle_name == "": self.middle_name = None


    @property
    def first_name_field(self) -> Field:
        return Field(input_type=FieldType.TEXT,
                     name="first_name",
                     value=self.first_name,
                     maxval=100)


    @property
    def last_name_field(self) -> Field:
        return Field(input_type=FieldType.TEXT,
                     name="last_name",
                     value=self.last_name,
                     maxval=100)


    @property
    def middle_name_field(self) -> Field:
        return Field(input_type=FieldType.TEXT,
                     name="middle_name",
                     value=self.middle_name,
                     maxval=100)


    def get_input_fields(self) -> List[Field]:
        return [self.first_name_field,
                self.middle_name_field,
                self.last_name_field]
