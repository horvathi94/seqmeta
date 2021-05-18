from .base import Base


class Authors(Base):

    view_table_name = "view_authors";
    submit_table_name = "authors";

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


    def check_if_exists(self):

        if self.first_name == None and \
                self.last_name == None:
                    return False;
        return True;


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
        if self.middle_name != "":
            tag+= self.middle_name + " ";
        tag+= self.last_name;
        return tag;


    def abreviated_middle_name(self):
        tag = self.first_name + " ";
        if self.middle_name != "":
            tag+= self.abreviate(self.middle_name) + " ";
        tag+= self.last_name;
        return tag;
