import pathlib
import xml.etree.ElementTree as ET
from xml.dom import minidom

PATH = "/home/seqmeta/uploads/samples"


class XML:

    def __init__(self, root, fname="tmp", path=PATH):
        self.fname = fname
        self.path = path
        self.elemtree = ET.Element(root)
        self.xmltree = ET.ElementTree(self.elemtree)


    @property
    def filename(self) -> str:
        return self.fname.split(".")[0] + ".xml"


    @filename.setter
    def filename(self, fname: str) -> None:
        self.fname = fname.split(".")[0] + ".xml"


    @property
    def file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.filename)


    @property
    def xml_string(self) -> str:
        return ET.tostring(self.elemtree)


    def write(self) -> None:
        xml = minidom.parseString(self.xml_string).toprettyxml(indent="  ",
                                                               encoding="UTF-8")
        with open(self.file, "wb") as f:
            f.write(xml)
