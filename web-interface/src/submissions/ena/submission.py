from .xml import XML
import xml.etree.ElementTree as ET


class SubmissionXML(XML):


    def __init__(self, fname="submission", action="ADD"):
        super().__init__(root="SUBMISSION", fname=fname)
        self.action = action
        self.create()


    def create(self) -> None:
        actions_tag = ET.SubElement(self.elemtree, "ACTIONS")
        action_tag = ET.SubElement(actions_tag, "ACTION")
        action = ET.SubElement(action_tag, self.action.upper())
