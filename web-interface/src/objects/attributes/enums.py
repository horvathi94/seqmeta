from enum import Enum


class Requirement(Enum):

    EXCLUDE = "exclude"
    OPTIONAL = "optional"
    RECOMMENDED = "recommended"
    MANDATORY = "mandatory"


    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


    @property
    def index(self) -> int:
        return Requirement.list().index(self.value)


    def __lt__(self, other):
        if self.index < other.index: return True
        return False


    def __gt__(self, other):
        if self.index > other.index: return True
        return False




class FieldType(Enum):

    TEXT = "text"
    DATE = "date"
    SELECT = "select"
    TEMPLATE = "template"
    FILE = "file"
