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
    FILE = "file"
