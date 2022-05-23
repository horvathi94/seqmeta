from dataclasses import dataclass, field
from typing import List
from .enums import Requirement, FieldType
from .sampleattr import SampleAttribute



@dataclass
class Attribute:

    general_name: str
    label: str
    type_: FieldType = FieldType.TEXT
    options: List[str] = field(default_factory=lambda: [])
    pattern: str = None
    template: str = None
    description: str = None
    default: any = None
    ena_name: str = None
    ena_requirement: Requirement = Requirement.EXCLUDE
    ena_units: List[str] = field(default_factory=lambda: [])
    ena_read_files: bool = True
    gisaid_name: str = None
    gisaid_requirement: Requirement = Requirement.EXCLUDE
    gisaid_header: str = None
    value: any = None
    is_fixed: bool = False
    is_invisible: bool = False


    def __post_init__(self):
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)
        if not isinstance(self.ena_requirement, Requirement):
            self.ena_requirement = Requirement(self.ena_requirement)
        if not isinstance(self.gisaid_requirement, Requirement):
            self.gisaid_requirement = Requirement(self.gisaid_requirement)
        if not isinstance(self.options, list):
            self.options = self.options.split(",")


    def __eq__(self, other: "Attribute"):
        if self.general_name != other.general_name: return False
        return True


    @property
    def json_value(self) -> any:
        if self.type_ is FieldType.FILE:
            return str(self.value)
        return self.value


    def asjson(self) -> dict:
        return {
            "general_name": self.general_name,
            "label": self.label,
            "type_": self.type_.value,
            "options": self.options,
            "template": self.template,
            "pattern": self.pattern,
            "default": self.default,
            "description": self.description,
            "ena_name": self.ena_name,
            "ena_requirement": self.ena_requirement.value,
            "ena_units": self.ena_units,
            "gisaid_name": self.gisaid_name,
            "gisaid_requirement": self.gisaid_requirement.value,
            "gisaid_header": self.gisaid_header,
            "value": self.json_value,
            "is_fixed": self.is_fixed,
            "is_invisible": self.is_invisible,
        }


    def as_sample_attribute(self) -> SampleAttribute:
        sa = SampleAttribute(self.general_name)
        sa.ena_name = self.ena_name
        sa.ena_requirement = self.ena_requirement
        sa.ena_units = self.ena_units
        sa.gisaid_name = self.gisaid_name
        sa.gisaid_requirement = self.gisaid_requirement
        sa.gisaid_header = self.gisaid_header
        return sa
