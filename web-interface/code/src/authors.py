from .base import Base

DOUBLE_CHARACTERS = ["sz", "zs"];

class Authors(Base):

    table_name = "authors";

    def clean_entry(self, entry):

        if entry["middle_name"] == None:
            entry["middle_name"] = "";


class AuthorNameTag:

    def __init__(self, od):

        self.first_name = od["first_name"];
        self.middle_name = "";
        if "middle_name" in od and od["middle_name"]:
            self.middle_name = od["middle_name"];
        self.last_name = od["last_name"];


    def abreviate(self, name):

        if not name:
            return "";

        abrev = name[:1];
        if name.lower() in DOUBLE_CHARACTERS:
            abrev = name[:2];
        abrev+= ".";
        return abrev;


    def full_name(self):
        tag = self.first_name + " ";
        tag+= self.middle_name + " ";
        tag+= self.last_name;
        return tag;


    def abreviated_middle_name(self):
        tag = self.first_name + " ";
        tag+= self.abreviate(self.middle_name) + " ";
        tag+= self.last_name + " ";
        return tag;
