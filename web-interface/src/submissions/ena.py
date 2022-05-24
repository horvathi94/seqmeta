import pathlib
from typing import List
import xml.etree.ElementTree as ET


class Metadata:

    path = "/home/seqmeta/uploads/samples/"


    def __init__(self):
        self.filename = "ena_upload"


    def file(self) -> pathlib.Path:
        fname = self.filename.split(".")[0] + ".xml"
        return pathlib.Path(self.path, fname)

    


def attribute_xml(a: "SampleAttribute") -> ET.Element:

    sample_attribute = ET.Element("SAMPLE_ATTRIBUTE")
    tag = ET.SubElement(sample_attribute, "TAG")
    tag.text = a.ena_name
    value = ET.SubElement(sample_attribute, "VALUE")
    value.text = a.value
    if a.ena_units:
        units = ET.SubElement(sample_attribute, "UNITS")
        units.text = a.ena_units

    return sample_attribute


def sample_xml(s: "Sample") -> ET.Element:

    sample = ET.Element("SAMPLE")
    title = ET.SubElement(sample, "TITLE")
    sample_name = ET.SubElement(sample, "SAMPLE_NAME")
    taxon_id = ET.SubElement(sample_name, "TAXON_ID")
    taxon_id.text = s.taxonomy.taxonomy_id
    scientific_name = ET.SubElement(sample_name, "SCIENTIFIC_NAME")
    scientific_name.text = s.taxonomy.scientific_name
    if s.taxonomy.common_name:
        common_name = ET.SubElement(sample_name, "COMMON_NAME")
        common_name.text = s.taxonomy.common_name

    sample_attributes = ET.SubElement(sample, "SAMPLE_ATTRIBUTES")
    for a in s.list_ena():
        attr = attribute_xml(a)
        sample_attributes.append(attr)

    return sample



def sample_set(samples: List["Sample"]) -> "xml":

    sample_set = ET.Element("SAMPLE_SET")
    for s in samples:
        sample = sample_xml(s)
        sample_set.append(sample)

    """
        for a in s.ena_list:


        sample_attribute = ET.SubElement(sample_attributes, "SAMPLE_ATTRIBUTE")
        tag = ET.SubElement(sample_attribute, "TAG")
        tag.text = "ENA-CHECKLIST"
        value = ET.SubElement(sample_attribute, "VALUE")
        value.text = s.ena_checklist
    """

    return ET.tostring(sample_set)
