from .cursor import Cursor
from .base import Base

class Institutions(Base):

    table_name = "institutions";

    def clean_entry(self, entry):
        pass;
