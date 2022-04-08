from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Requirement(Enum):

    NONE = "none"
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

    name: str
    label: str
    type_: FieldType
    repos: List[RepoField] = field(default_factory=lambda: [])
    options: List[str] = None
    pattern: str = None
    template_id: int = None
    template: str = None
    description: str = None
    default: any = None
    id: int = None


    def __post_init__(self):
        if self.default == "": self.default = None
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)
        if isinstance(self.options, str):
            self.options = self.options.split(",")


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
            "name": self.name,
            "label": self.label,
            "type_": self.type_.value,
            "options": self.options_csv,
            "template": self.template,
            "pattern": self.pattern,
            "description": self.description,
        }
