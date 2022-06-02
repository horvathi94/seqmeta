from .xml import XML
from xml.dom import minidom


class SampleSetXML(XML):


    def __init__(self, fname="sample_set"):
        super().__init__(root="SAMPLE_SET", fname=fname)


    def attr_xml(self, tag: str, value: str, units: str="") -> minidom.Element:
        xml = self.create_element("SAMPLE_ATTRIBUTE")
        tag_xml = self.create_element("TAG", text=tag)
        xml.appendChild(tag_xml)
        value_xml = self.create_element("VALUE", text=value)
        xml.appendChild(value_xml)
        if units:
            units_xml = self.create_element("UNITS", text=units)
            xml.appendChild(units_xml)
        return xml


    def sample_name_xml(self, taxon: "Taxonomy") -> minidom.Element:
        sample_name = self.create_element("SAMPLE_NAME")
        tid = self.create_element("TAXON_ID", text=taxon.taxonomy_id)
        sample_name.appendChild(tid)
        sn = self.create_element("SCIENTIFIC_NAME", text=taxon.scientific_name)
        sample_name.appendChild(sn)
        cn = self.create_element("COMMON_NAME", text=taxon.common_name)
        sample_name.appendChild(cn)
        return sample_name


    def sample_xml(self, sample: "Sample") -> minidom.Element:
        xml = self.create_element("SAMPLE")
        xml.setAttribute("alias", sample.name)
        title = self.create_element("TITLE",text=sample.get_value("ena_title"))
        xml.appendChild(title)
        xml.appendChild(self.sample_name_xml(sample.taxonomy))
        attrs_xml = self.create_element("SAMPLE_ATTRIBUTES")
        for attr in sample.list_ena_sample_attributes():
            attr_xml = self.attr_xml(attr.ena_name, attr.value, attr.ena_units)
            attrs_xml.appendChild(attr_xml)
        xml.appendChild(attrs_xml)
        checklist = self.attr_xml("ENA-CHECKLIST", sample.ena_checklist)
        attrs_xml.appendChild(checklist)
        return xml


    def add_sample(self, sample: "Sample") -> None:
        sample_xml = self.sample_xml(sample)
        self.append_element(sample_xml)

