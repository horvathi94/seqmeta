from .xml import XML
from xml.dom import minidom


class SubmissionXML(XML):


    def __init__(self, fname="submission", action="ADD"):
        super().__init__(root="SUBMISSION", fname=fname)
        self.action = action
        self.create()


    def create(self) -> None:
        actions = self.create_element("ACTIONS")
        self.append_element(actions)
        action = self.create_element("ACTION")
        actions.appendChild(action)
        a = self.create_element(self.action.upper())
        action.appendChild(a)
