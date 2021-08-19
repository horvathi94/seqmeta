from enum import Enum, auto
from application.src.authors import Authors, AuthorGroups
from application.src import misc


class Fields:

    continents = auto();
    collector_name = auto();


class OptionsList:

    @staticmethod
    def get(handle: Fields) -> list:
        """Fetch list of possible values for the field."""
        if handle == Fields.continents:
            return misc.Continents.fetch_list();
        if handle == Fields.collector_name:
            return Authors.fetch_list_labeled(
                replace_key="abbreviated_middle_name");
