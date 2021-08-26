from application.src.db.interface import DBInterface
from application.src.fields.radio import RadioValue, RadioList


class LibraryLayouts(RadioList):

    items = [
        RadioValue(),
        RadioValue("Paired-end", 1, 1, True),
        RadioValue("Single", 2, 0, False),
    ];



class LibraryStrategies(DBInterface):

    display_table_name = "library_strategies";

    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="item_key");




class LibrarySelections(DBInterface):

    display_table_name = "library_selections";

    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="item_key");




class LibrarySources(DBInterface):

    display_table_name = "library_sources";

    @classmethod
    def fetch_select_list(cls) -> list:
        return cls.fetch_list_labeled(replace_key="item_key");

