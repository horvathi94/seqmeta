import xml.etree.ElementTree as ET
from .base.xml_gen import XMLGenerator


class ExperimentSet(XMLGenerator):

    attribute_tag = ""
    tempfilename = "last_generated_experiment_set.xml"

    @classmethod
    def gen_experiment_xml(cls, exp_data):
        experiment = ET.Element("EXPERIMENT")
        title = ET.SubElement(experiment, "TITLE")
        study_ref = ET.SubElement(experiment, "STUDY_REF")
        design = ET.SubElement(experiment, "DESIGN")
        design_description = ET.SubElement(design, "DESIGN_DESCRIPTION")
        sample_descriptor = ET.SubElement(design, "SAMPLE_DESCRIPTOR")
        sample_descriptor.set("refname", exp_data["sample_name"])
        lib_descript  = ET.SubElement(design, "LIBRARY_DESCRIPTOR")
        lib_name = ET.SubElement(lib_descript, "LIBRARY_NAME")
        lib_strategy = ET.SubElement(lib_descript, "LIBRARY_STRATEGY")
        lib_strategy.text = exp_data["library_strategy"]
        lib_source = ET.SubElement(lib_descript, "LIBRARY_SOURCE")
        lib_source.text = exp_data["library_source"]
        lib_selection = ET.SubElement(lib_descript, "LIBRARY_SELECTION")
        lib_selection.text = exp_data["library_selection"]
        lib_layout = ET.SubElement(design, "LIBRARY_LAYOUT")
        if exp_data["is_paired"]:
            paired = ET.SubElement(lib_layout, "PAIRED")
        else:
            single = ET.SubElement(lib_layout, "SINGLE")
        lib_construct= ET.SubElement(design, "LIBRARY_CONSTRUCTION_PROTOCOL")
        lib_construct.text = exp_data["library_design_description"]
        platform_wrap = ET.SubElement(experiment, "PLATFORM")
        platform = ET.SubElement(platform_wrap, exp_data["sequencing_platform"])
        instrument = ET.SubElement(platform, "INSTRUMENT_MODEL")
        instrument.text = exp_data["sequencing_instrument"]
        exp_attrs = ET.SubElement(experiment, "EXPERIMENT_ATTRIBUTES")
        exp_attr = ET.SubElement(exp_attrs, "EXPERIMENT_ATTRIBUTE")
        prep_date_tag = ET.SubElement(exp_attr, "TAG")
        prep_date_tag.text = "library preparation date"
        prep_date_value = ET.SubElement(exp_attr, "VALUE")
        prep_date_value.text = exp_data["library_preparation_date"]
        return experiment


    @classmethod
    def generate_xml(cls, experiments):
        experiment_set = ET.Element("SAMPLE_SET")
        for experiment in experiments:
            experiment_set.append(cls.gen_experiment_xml(experiment))
        return ET.ElementTree(experiment_set)


    @classmethod
    def save_xml(cls, experiments):
        experiment_set = cls.generate_xml(experiments)
        cls.write_xml(experiment_set)
