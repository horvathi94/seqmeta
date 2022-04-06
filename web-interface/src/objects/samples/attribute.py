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
    has_options: bool = False
    options: List[str] = field(default_factory=lambda: [])
    pattern: str = None
    template_id: int = None
    description: str = None
    default: any = None
    id: int = None


    def __post_init__(self):
        if self.default == "": self.default = None
        if not isinstance(self.type_, FieldType):
            self.type_ = FieldType(self.type_)
        self._check_has_options()


    def _check_has_options(self) -> None:
        if self.has_options is not None:
            self.has_options = bool(self.has_options)
            return
        if self.type_ is FieldType.SELECT and len(self.options) > 0:
            self.has_options = True
        self.has_options = False


    def asdict(self) -> dict:
        return {
            "template_id": self.template_id,
            "name": self.name,
            "label": self.label,
            "type_": self.type_.value,
            "has_options": self.has_options,
            "description": self.description,
        }
