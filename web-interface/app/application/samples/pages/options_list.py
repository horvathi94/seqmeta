from application.src.authors import Authors, AuthorGroups

class OptionList:

    @classmethod
    def get_list(cls) -> list:
        """Returns list of possibile values of the field."""
        pass;



class CollectorName(OptionList):

    @classmethod
    def get_list(cls) -> list:
        return Authors.fetch_list_labeled(
            replace_key="abbreviated_middle_name");
