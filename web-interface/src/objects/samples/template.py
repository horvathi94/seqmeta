from .attribute import Attribute


class Template:


    def __init__(self):
        self.attributes = []


    def add_attribute(self, a: Attribute) -> None:
        self.attributes.append(a)
