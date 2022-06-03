from dataclasses import dataclass, field
from typing import List
from .enums import FieldType, Requirement
from .sample_attr import SampleAttribute


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
    _ena_requirement: str = "exclude"
    ena_units: str = ""
    gisaid_name: str = ""
    _gisaid_requirement: str = "exclude"
    gisaid_header: str = ""
    has_fixed_name: bool = False
    _is_unique: bool = False
    must_be_unique: bool = False
    is_mandatory: bool = False


    def __post_init__(self):
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)


    @property
    def is_unique(self) -> bool:
        return self._is_unique or self.must_be_unique


    @is_unique.setter
    def is_unique(self, is_unqiue: bool) -> None:
        self._is_unique = is_unique


    @property
    def gisaid_requirement(self) -> Requirement:
        return Requirement(self._gisaid_requirement)


    @gisaid_requirement.setter
    def gisaid_requirement(self, req: any) -> None:
        if isinstance(req, Requirement):
            req = req.value
        self._gisaid_requirement = req


    @property
    def ena_requirement(self) -> Requirement:
        return Requirement(self._ena_requirement)


    @ena_requirement.setter
    def ena_requirement(self, req: any) -> None:
        if isinstance(req, Requirement):
            req = req.value
        self._ena_requirement = req


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
            "has_fixed_name": self.has_fixed_name,
            "is_unique": self.is_unique,
            "must_be_unique": self.must_be_unique,
            "is_mandatory": self.is_mandatory,
        }


    @classmethod
    def from_dict(cls, data: dict) -> "AttributeField":
        a = AttributeField(data["general_name"], data["label"],
                type_=data["type_"])
        if "options" in data: a.options = data["options"]
        if "template" in data: a.template = data["template"]
        if "pattern" in data: a.pattern = data["pattern"]
        if "default" in data: a.default = data["default"]
        a.description = data["description"]
        a.ena_name = data["ena_name"]
        a.ena_requirement = data["ena_requirement"]
        a.ena_units = data["ena_units"]
        a.gisaid_name = data["gisaid_name"]
        a.gisaid_requirement = data["gisaid_requirement"]
        a.gisaid_header = data["gisaid_header"]
        return a


    def as_sample_attribute(self) -> SampleAttribute:
        attr = SampleAttribute(self.general_name, ena_name=self.ena_name,
                ena_units=self.ena_units, gisaid_name=self.gisaid_name,
                gisaid_header=self.gisaid_header)
        attr.gisaid_requirement = self.gisaid_requirement
        attr.ena_requirement = self.ena_requirement
        return attr
