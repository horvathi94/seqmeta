from .cursor import Cursor
from .base import Base

class Institutions(Base):

    view_table_name = "institutions";
    submit_table_name = "institutions";

    def clean_entry(self, entry):
        pass;
