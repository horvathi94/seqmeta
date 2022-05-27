from .xml import XML
from xml.dom import minidom


class ExperimentSetXML(XML):

    def __init__(self, fname="experiment"):
        super().__init__(root="EXPERIMENT_SET", fname=fname)


    def library_xml(self, sample: "Sample") -> minidom.Element:
        lib = self.create_element("LIBRARY_DESCRIPTOR")
        name = self.create_element("LIBRARY_NAME")
        lib.appendChild(name)
        strategy = self.create_element("LIBRARY_STRATEGY",
                text=sample.get_attribute_value("library_strategy"))
        lib.appendChild(strategy)
        source = self.create_element("LIBRARY_SOURCE",
                text=sample.get_attribute_value("library_source"))
        lib.appendChild(source)
        selection = self.create_element("LIBRARY_SELECTION",
                text=sample.get_attribute_value("library_selection"))
        lib.appendChild(selection)
        layout = self.create_element("LIBRARY_LAYOUT")
        ltype = self.create_element(sample.library_layout.upper())
        ltype.setAttribute("NOMINAL_LENGTH",
                           sample.get_attribute_value("insert_size"))
        layout.appendChild(ltype)
        lib.appendChild(layout)
        construct = self.create_element("LIBRARY_CONSTRUCTION_PROTOCOL",
            text=sample.get_attribute_value("ena_experiment_description"))
        lib.appendChild(construct)
        return lib


    def platform_xml(self, sample: "Sample") -> minidom.Element:
        platform = self.create_element("PLATFORM")
        pname = self.create_element(
            sample.get_attribute_value("platform").upper())
        platform.appendChild(pname)
        model = self.create_element("INSTRUMENT_MODEL",
                                text=sample.get_attribute_value("instrument"))
        pname.appendChild(model)
        return platform


    def experiment_attributes_xml(self, sample: "Sample") -> minidom.Element:
        attrs = self.create_element("EXPERIMENT_ATTRIBUTES")
        attr = self.create_element("EXPERIMENT_ATTRIBUTE")
        prep_date_tag = self.create_element("TAG",
                                    text="library preparation date")
        attr.appendChild(prep_date_tag)
        prep_date_val = self.create_element("VALUE",
                                    text="sample.get_attribute_value()")
        attr.appendChild(prep_date_val)
        attrs.appendChild(attr)
        return attrs


    def experiment_xml(self, sample: "Sample") -> minidom.Element:
        exp = self.create_element("EXPERIMENT")
        exp.setAttribute("alias",
                         sample.get_attribute_value("ena_experiment_name"))
        title = self.create_element("TITLE", text="EXPERIMENT TITLE")
        exp.appendChild(title)
        study = self.create_element("STUDY_REF")
        study.setAttribute("accession",
                           sample.get_attribute_value("ena_study"))
        exp.appendChild(study)
        design = self.create_element("DESIGN")
        design_descript = self.create_element("DESIGN_DESCRIPTION")
        design.appendChild(design_descript)
        sample_descript = self.create_element("SAMPLE_DESCRIPTOR")
        sample_descript.setAttribute("accession", "sample.accession")
        design.appendChild(sample_descript)
        design.appendChild(self.library_xml(sample))
        exp.appendChild(design)
        exp.appendChild(self.platform_xml(sample))
        exp.appendChild(self.experiment_attributes_xml(sample))
        return exp


    def add_sample(self, sample: "Sample") -> None:
        experiment_xml = self.experiment_xml(sample)
        self.append_element(experiment_xml)
