from dataclasses import dataclass
from enum import Enum


class Importance(Enum):

    OPTIONAL = "optional"
    RECOMMENDED = "recommended"
    MANDATORY = "mandatory"



@dataclass
class Attribute:

    name: str
    importance: Importance
    description: str
    default: any = None
    id: int = None


    def __post_init__(self):
        self.importance = Importance(self.importance)
        if self.default == "": self.default = None
