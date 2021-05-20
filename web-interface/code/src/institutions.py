from .cursor import Cursor
from .db_interface import DBInterface

class Institutions(DBInterface):

    display_table_name = "view_institutions";
    edit_table_name = "institutions";
    submit_table_name = "institutions";

