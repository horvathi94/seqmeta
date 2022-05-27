from dataclasses import dataclass, field
from typing import List
from .enums import FieldType, Requirement


@dataclass
class AttributeField:

    """Attribute fields for creating templates."""

    general_name: str
    label: str
    type_: FieldType = FieldType.TEXT
    description: str = ""
    default: any = None
    _options: List[str] = field(default_factory=lambda: [])
    _pattern: str = ""
    _template: str = ""
    ena_name: str = ""
    ena_requirement: Requirement = Requirement.EXCLUDE
    ena_units: str = ""
    gisaid_name: str = ""
    gisaid_requirement: Requirement = Requirement.EXCLUDE
    gisaid_header: str = ""
    is_hidden: bool = False
    is_unique: bool = False
    is_fixed: bool = False


    def __post_init__(self):
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)
        if not isinstance(self.ena_requirement, Requirement):
            self.ena_requirement = Requirement(self.ena_requirement)
        if not isinstance(self.gisaid_requirement, Requirement):
            self.gisaid_requirement = Requirement(self.gisaid_requirement)


    @property
    def options(self) -> list:
        if not self.type_ is FieldType.SELECT: return []
        return self._options


    @options.setter
    def options(self, opts: list) -> None:
        if not isinstance(opts, list): opts = opts.split(",")
        self._options = opts


    @property
    def pattern(self) -> str:
        if not self.type_ is FieldType.TEXT: return ""
        return self._pattern


    @pattern.setter
    def pattern(self, p: str) -> None:
        self._pattern = p


    @property
    def template(self) -> str:
        if not self.type_ is FieldType.TEMPLATE: return ""
        return self._template


    @template.setter
    def template(self, t: str) -> None:
        self._template = t


    def set_mandatory(self) -> None:
        self.gisaid_requirement = Requirement.MANDATORY
        self.ena_requirement = Requirement.MANDATORY


    def as_json(self) -> dict:
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
            "is_hidden": self.is_hidden,
            "is_unique": self.is_unique,
            "is_fixed": self.is_fixed,
        }
