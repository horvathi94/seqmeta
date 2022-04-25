from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Requirement(Enum):

    EXCLUDE = "exclude"
    OPTIONAL = "optional"
    RECOMMENDED = "recommended"
    MANDATORY = "mandatory"


class FieldType(Enum):

    TEXT = "text"
    DATE = "date"
    SELECT = "select"
    TEMPLATE = "template"


class Repo(Enum):

    ENA = "ena"
    GISAID = "gisaid"


@dataclass
class RepoField:

    repo: Repo
    name: str
    requirement: Requirement = Requirement.OPTIONAL




@dataclass
class Attribute:

    general_name: str
    label: str
    type_: FieldType
    options: List[str] = field(default_factory=lambda: [])
    pattern: str = None
    template_id: int = None
    template: str = None
    description: str = None
    default: any = None
    id: int = None
    ena_name: str = None
    ena_requirement: str = None
    gisaid_name: str = None
    gisaid_requirement: str = None

    status: str = "new"
    deleted: bool = False
    value: any = None


    def __post_init__(self):
        if self.default == "" and self.type_ is not FieldType.SELECT:
            self.default = None
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)
        self._clean_options()
        self._clean_pattern()
        self._ena_requirement()
        self._gisaid_requirement()
        self.deleted = bool(int(self.deleted))


    def _clean_options(self) -> None:
        if self.options is None: self.options = []
        if isinstance(self.options, str):
            self.options = self.options.split(",")


    def _clean_pattern(self) -> None:
        if self.pattern == "":
            self.pattern = None
        if self.type_ is not FieldType.TEXT:
            self.pattern = None


    def _ena_requirement(self) -> None:
        if self.ena_name is None or self.ena_name == "":
            self.ena_requirement = "exclude"
        if self.ena_requirement is None or self.ena_requirement == "":
            self.ena_requirement = "exclude"
        self.ena_requirement = Requirement(self.ena_requirement)


    def _gisaid_requirement(self) -> None:
        if self.gisaid_name is None or self.gisaid_name == "":
            self.gisaid_requirement = "exclude"
        if self.gisaid_requirement is None or self.gisaid_requirement == "":
            self.gisaid_requirement = "exclude"
        self.gisaid_requirement = Requirement(self.gisaid_requirement)


    @property
    def form_name(self) -> str:
        fname = self.name.replace(" ", "__")
        fname = fname.replace("/", "___")
        fname = fname.replace("(", "____")
        fname = fname.replace(")", "____")
        return fname


    @property
    def options_csv(self) -> str:
        if self.options is None: return None
        return ",".join(self.options)


    def asdict(self) -> dict:
        return {
            "template_id": self.template_id,
            "general_name": self.general_name,
            "label": self.label,
            "type_": self.type_.value,
            "options": self.options_csv,
            "template": self.template,
            "pattern": self.pattern,
            "default": self.default,
            "description": self.description,
            "ena_name": self.ena_name,
            "ena_requirement": self.ena_requirement.value,
            "gisaid_name": self.gisaid_name,
            "gisaid_requirement": self.gisaid_requirement.value,
        }


    def asjson(self) -> dict:
        data = self.asdict()
        data["id"] = self.id
        data["options"] = self.options
        return data


    @property
    def upsert_values(self) -> tuple:
        return (self.id, self.template_id, self.deleted, self.general_name,
                self.label, self.type_.value, self.description, self.template,
                self.default, self.pattern, self.options_csv,
                self.ena_name, self.ena_requirement.value,
                self.gisaid_name, self.gisaid_requirement.value)
