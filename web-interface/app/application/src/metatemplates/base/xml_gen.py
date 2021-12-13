from .tempfile import TempFile
import xml.etree.ElementTree as ET


class XMLGenerator(TempFile):

    attribute_tag = ""

    @classmethod
    def create_attr(cls, tag, value, units=""):
        attr = ET.Element(cls.attribute_tag)
        t = ET.SubElement(attr, "TAG")
        t.text = tag
        v = ET.SubElement(attr, "VALUE")
        v.text = value
        if units:
            u = ET.SubElement(attr, "UNITS")
            u.text = units
        return attr


    @classmethod
    def write_xml(cls, xml_data):
        with open(cls.get_tempfile(), "w") as f:
            xml_data.write(f, encoding="unicode")

