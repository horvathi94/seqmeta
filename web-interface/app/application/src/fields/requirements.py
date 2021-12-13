from dataclasses import dataclass
from enum import Enum


class RequirementLevels(Enum):

    optional = 1
    recommended = 2
    mandatory = 3



class RequirementRepos(Enum):

    GIASID = "gisaid"
    ENA = "ena"
    NCBI = "ncbi"



@dataclass
class Requirement:

    repo: str = ""
    level: str = ""

