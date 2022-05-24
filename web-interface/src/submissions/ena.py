import pathlib
from typing import List
import xml.etree.ElementTree as ET


class Metadata:

    path = "/home/seqmeta/uploads/samples/"
    tmp_manifest = "tmp.txt"

    def __init__(self):
        self._samples_xml_filename = "ena_upload"
        self.sample_set = ET.Element("SAMPLE_SET")
        self.xml_tree = ET.ElementTree(self.sample_set)


    @property
    def samples_xml_filename(self) -> str:
        return self._samples_xml_filename.split(".")[0] + ".xml"


    @samples_xml_filename.setter
    def samples_xml_filename(self, fname: str) -> None:
        self._samples_xml_filename = fname.split(".")[0] + ".xml"


    @property
    def samples_xml_file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.samples_xml_filename)


    @property
    def tmp_manifest_file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.tmp_manifest)


    def create_attribute_xml(self, attr: "SampleAttribute") -> ET.Element:
        xml = ET.Element("SAMPLE_ATTRIBUTE")
        tag = ET.SubElement(xml, "TAG")
        tag.text = attr.ena_name
        value = ET.SubElement(xml, "VALUE")
        value.text = attr.value
        if attr.ena_units:
            units = ET.SubElement(xml, "UNITS")
            units.text = attr.ena_units
        return xml


    def create_sample_xml(self, sample: "Sample") -> ET.Element:
        xml = ET.Element("SAMPLE")
        title = ET.SubElement(xml, "TITLE")
        sample_name = ET.SubElement(xml, "SAMPLE_NAME")
        taxon_id = ET.SubElement(xml, "TAXON_ID")
        taxon_id.text = sample.taxonomy.taxonomy_id
        scientific_name = ET.SubElement(sample_name, "SCIENTIFIC_NAME")
        scientific_name.text = sample.taxonomy.scientific_name
        if sample.taxonomy.common_name:
            common_name = ET.SubElement(sample_name, "COMMON_NAME")
            common_name.text = sample.taxonomy.common_name

        sample_attributes = ET.SubElement(xml, "SAMPLE_ATTRIBUTES")
        for attr in sample.list_ena():
            attr_xml = self.create_attribute_xml(attr)
            sample_attributes.append(attr_xml)
        return xml



    def add_sample(self, sample: "Sample") -> None:
        sample_xml = self.create_sample_xml(sample)
        self.sample_set.append(sample_xml)
        self.write_experiment_manifest(sample)


    def add_samples(self, samples: List["Sample"]) -> None:
        for sample in samples:
            self.add_sample(sample)


    @property
    def xml(self) -> str:
        return ET.tostring(self.sample_set)


    def write(self) -> None:
        self.xml_tree.write(self.samples_xml_file)


    def write_experiment_manifest(self, sample: "Sample") -> None:
        with open(self.tmp_manifest_file, "w") as mf:
            for item in sample.list_ena_experiment():
                mf.write(f"{item['name']} {item['value']}\n")

