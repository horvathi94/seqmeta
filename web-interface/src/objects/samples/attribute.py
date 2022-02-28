from dataclasses import dataclass
from enum import Enum


class Level(Enum):

    OPTIONAL = 1
    RECOMMENDED = 2
    MANDATORY = 3



@dataclass
class Attribute:

    name: str
    level: Level
    description: str
    default: any = None
    id: int = None


    def __post_init__(self):
        self.level = Level(int(self.level))
        if self.default == "": self.default = None
