import xml.etree.ElementTree as ET
from .base.xml_gen import XMLGenerator


class SampleSet(XMLGenerator):

    attribute_tag = "SAMPLE_ATTRIBUTE";
    tempfilename = "last_generated_sample_set.xml";

    @classmethod
    def gen_sample_xml(cls, sample_data):
        sample = ET.Element("SAMPLE");
        sample.set("alias", sample_data["sample_name"]);
        attr = cls.create_attr("ENA-CHECKLIST", "ERC000033");
        sample.append(attr);
        for key in sample_data:
            if key == "sample_id":
                continue;
            if key == "host age":
                attr = cls.create_attr(key,
                                       str(sample_data[key]), units="years");
            elif key in ["geographic location (latitude)",
                         "geographic location (longitude)"]:
                attr = cls.create_attr(key,
                                       str(sample_data[key]), units="DD");
            elif sample_data[key]:
                attr = cls.create_attr(key, sample_data[key]);
            else:
                continue;
            sample.append(attr);

        return sample;


    @classmethod
    def generate_xml(cls, samples):
        sample_set = ET.Element("SAMPLE_SET");
        for sample in samples:
            sample_set.append(cls.gen_sample_xml(sample));
        return ET.ElementTree(sample_set);


    @classmethod
    def save_xml(cls, samples):
        sample_set = cls.generate_xml(samples);
        cls.write_xml(sample_set);
