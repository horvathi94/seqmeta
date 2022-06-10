from typing import List
from .attr_field import AttributeField
from .builtin_fields import basic
from .builtin_fields import gisaid
from .builtin_fields import ena


def list_fields(which: str) -> List[AttributeField]:
    if which == "empty":
        return [AttributeField("", "")]
    elif which == "basic":
        return [AttributeField(**d) for d in basic.ALL_FIELDS]
    elif which == "gisaid_assembly":
        return [AttributeField(**d) for d in gisaid.ALL_FIELDS]
    elif which == "ena_read":
        return [AttributeField(**d) for d in ena.ALL_FIELDS]
    return []
