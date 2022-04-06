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
    type_: FieldType
    repos: List[RepoField] = field(default_factory=lambda: [])
    options: List[str] = field(default_factory=lambda: [])
    pattern: str = None
    template: str = None
    description: str = None
    default: any = None
    id: int = None


    def __post_init__(self):
        if self.default == "": self.default = None
