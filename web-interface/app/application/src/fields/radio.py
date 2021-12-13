from dataclasses import dataclass


@dataclass
class RadioValue:

    label: str = "N/A"
    value: int = 0
    dbval: int = None
    dbsave: bool = None


class RadioList:

    items = []

    @classmethod
    def get_list(cls):
        return cls.items


    @classmethod
    def get_item_from_dbvalue(cls, db_value: int) -> RadioValue:
        """Get item from db_value."""
        for item in cls.items:
            if item.dbval == db_value: return item
        return RadioValue()


    @classmethod
    def get_item_from_value(cls, value: int) -> RadioValue:
        """Get item from value."""
        for item in cls.items:
            if item.value == value: return item
        return RadioValue()
