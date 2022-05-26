import pathlib
from xml.dom import minidom

PATH = "/home/seqmeta/uploads/samples"


class XML:

    def __init__(self, root, fname="tmp", path=PATH):
        self.fname = fname
        self.path = path
        self.root = minidom.Document()
        self.xml = self.root.createElement(root)
        self.root.appendChild(self.xml)


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
        return self.root.toprettyxml(indent=" "*3)


    def create_element(self, name: str, text: str="") -> minidom.Element:
        elem = self.root.createElement(name)
        if not text:
            return elem
        text_node = self.root.createTextNode(text)
        elem.appendChild(text_node)
        return elem


    def append_element(self, elem: minidom.Element) -> None:
        self.xml.appendChild(elem)


    def write(self) -> None:
        with open(self.file, "w") as f:
            f.write(self.xml_string)
