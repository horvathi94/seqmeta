from .xml import XML
import xml.etree.ElementTree as ET


class SampleSetXML(XML):


    def __init__(self, fname="sample_set"):
        super().__init__(root="SAMPLE_SET", fname=fname)


    def create_attribute_xml(self, name: str, value: any,
                             units: str="") -> ET.Element:
        xml = ET.Element("SAMPLE_ATTRIBUTE")
        tag = ET.SubElement(xml, "TAG")
        tag.text = name
        value_tag = ET.SubElement(xml, "VALUE")
        value_tag.text = value
        if units:
            units_tag = ET.SubElement(xml, "UNITS")
            units_tag.text = units
        return xml


    def sample_attribute_xml(self, attr: "SampleAttribute") -> ET.Element:
        return self.create_attribute_xml(attr.ena_name, attr.value,
                                         attr.ena_units)


    def create_sample_xml(self, sample: "Sample") -> ET.Element:
        xml = ET.Element("SAMPLE")
        xml.set("alias", sample.name)
        title = ET.SubElement(xml, "TITLE")
        title.text = sample.ena_title
        sample_name = ET.SubElement(xml, "SAMPLE_NAME")
        taxon_id = ET.SubElement(sample_name, "TAXON_ID")
        taxon_id.text = sample.taxonomy.taxonomy_id
        scientific_name = ET.SubElement(sample_name, "SCIENTIFIC_NAME")
        scientific_name.text = sample.taxonomy.scientific_name
        if sample.taxonomy.common_name:
            common_name = ET.SubElement(sample_name, "COMMON_NAME")
            common_name.text = sample.taxonomy.common_name
        sample_attributes = ET.SubElement(xml, "SAMPLE_ATTRIBUTES")
        for attr in sample.list_ena():
            attr_xml = self.sample_attribute_xml(attr)
            sample_attributes.append(attr_xml)

        print(sample.ena_checklist)
        checklist = self.create_attribute_xml("ENA-CHECKLIST",
                                              sample.ena_checklist)
        sample_attributes.append(checklist)
        return xml


    def add_sample(self, sample: "Sample") -> None:
        sample_xml = self.create_sample_xml(sample)
        self.elemtree.append(sample_xml)

