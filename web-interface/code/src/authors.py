from .base import Base

class Authors(Base):

    table_name = "authors";

    def clean_entry(self, entry):

        if entry["middle_name"] == None:
            entry["middle_name"] = "";

