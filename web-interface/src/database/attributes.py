from seqmeta.database.connect import Connect
from seqmeta.objects.samples import Attribute


class AttributesTable:

    @staticmethod
    def select_all():
        pass


    @staticmethod
    def select():
        pass


    @staticmethod
    def save(attr: Attribute) -> None:
        print(f"\nSaving attribute: {attr}")
#        conn = Connect()
