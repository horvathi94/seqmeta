from .db.interface import DBInterface


class LibraryStrategies(DBInterface):

    display_table_name = "library_strategies";


class LibrarySelections(DBInterface):

    display_table_name = "library_selections";


class LibrarySources(DBInterface):

    display_table_name = "library_sources";

