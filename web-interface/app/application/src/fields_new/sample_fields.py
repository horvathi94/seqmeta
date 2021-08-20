from enum import Enum


class SampleFields(Enum):

    """Mapping of field handles form the database to custom Enum class."""

    NONE = "";
    SAMPLE_NAME = "sample_name";
    COLLECTOR_NAME = "collector_name";
    LOC_CONTINENT = "location_continent";

    @classmethod
    def list_for_editor(cls) -> list:
        """List fields for editor."""
        items = [];
        for e in cls:
            if e != cls.NONE: items.append(e);
        return items;

