from typing import List
import xml.etree.ElementTree as ET


def sample_set(samples: List["Sample"]) -> "xml":

    sample_set = ET.Element("SAMPLE_SET")
    for s in samples:
        sample = ET.SubElement(sample_set, "SAMPLE")
        title = ET.SubElement(sample, "TITLE")
        sample_name = ET.SubElement(sample, "SAMPLE_NAME")
        taxon_id = ET.SubElement(sample_name, "TAXON_ID")
        scientific_name = ET.SubElement(sample_name, "SCIENTIFIC_NAME")
        common_name = ET.SubElement(sample_name, "COMMON_NAME")

        sample_attributes = ET.SubElement(sample, "SAMPLE_ATTRIBUTES")
        for a in s.ena_list:
            sample_attribute = ET.SubElement(sample_attributes,
                                             "SAMPLE_ATTRIBUTE")
            tag = ET.SubElement(sample_attribute, "TAG")
            tag.text = a["tag"]
            value = ET.SubElement(sample_attribute, "VALUE")
            value.text = a["value"]

    return ET.tostring(sample_set)
