from .db.interface import DBInterface

class Countries(DBInterface):

    display_table_name = "countries";


class Continents(DBInterface):

    display_table_name = "continents";
