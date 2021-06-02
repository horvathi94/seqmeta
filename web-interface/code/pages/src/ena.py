from .cursor import Cursor
from .db_interface import DBInterface
import xml.etree.ElementTree as ET


class Studies(DBInterface):

    display_table_name = "ena_studies";
    edit_table_name = "ena_studies";
    submit_table_name = "ena_studies";


    @classmethod
    def create_xml(cls, study_id):
        study = cls.fetch_entry(id=study_id);
        project_set = ET.Element("PROJECT_SET");
        project = ET.SubElement(project_set, "PROJECT");
        project.set("alias", study["project_alias"]);
        project_name = ET.SubElement(project, "NAME");
        project_name.text = study["project_name"];
        project_title = ET.SubElement(project, "TITLE");
        project_title.text = study["project_title"];
        project_description = ET.SubElement(project, "DESCRIPTION");
        project_description.text = study["project_description"];

        if study["project_link_db"] and study["project_link_id"]:
            project_links = ET.SubElement(project, "PROJECT_LINKS");
            project_link = ET.SubElement(project_links, "PROJECT_LINK")
            xref = ET.SubElement(project_link, "XREF_LINK");
            db = ET.SubElement(xref, "DB");
            db.text = study["project_link_db"];
            dbid = ET.SubElement(xref, "ID");
            dbid.text = study["project_link_id"];

        xml_data = ET.tostring(project_set);
        return xml_data;



class SampleSet(DBInterface):

    @staticmethod
    def attr(tag, value, units=""):
        attr = ET.Element("SAMPLE_ATTRIBUTE");
        t = ET.SubElement(attr, "TAG");
        t.text = tag;
        v = ET.SubElement(attr, "VALUE");
        v.text = value;
        if units:
            u = ET.SubElement(attr, "UNITS");
            u.text = units;
        return attr;


    @classmethod
    def create_sample_xml(cls, sample_id):
        sample ,= Cursor.select("view_samples_ena",
                    clauses="WHERE `sample_id` = {:d}".format(sample_id));

        sample_tag = ET.Element("SAMPLE");
        sample_tag.set("alias", sample["sample_name"]);
        attr = cls.attr("ENA-CHECKLIST", "ERC000033");
        sample_tag.append(attr);

        for key in sample:
            if key == "sample_id":
                continue;

            if key == "host age":
                attr = cls.attr(key, str(sample[key]), units="years");
            elif key in ["geographic location (latitude)",
                         "geographic location (longitude)"]:
                attr = cls.attr(key, str(sample[key]), units="DD");
            elif sample[key]:
                attr = cls.attr(key, sample[key]);
            else:
                continue;

            sample_tag.append(attr);

        return sample_tag;


    @classmethod
    def create_xml(cls, sample_ids):

        sample_set = ET.Element("SAMPLE_SET");
        for sample_id in sample_ids:
            sample_set.append(cls.create_sample_xml(sample_id));
        return ET.tostring(sample_set);



class ExperimentSet(DBInterface):

    display_table_name = "view_samples_ena_experiment";


    @classmethod
    def create_experiment_xml(cls, sample_id):
        experiment = ET.Element("EXPERIMENT");
        sample ,= Cursor.select("view_samples_ena_experiment",
                    clauses="WHERE `sample_id` = {:d}".format(sample_id));
        title = ET.SubElement(experiment, "TITLE");
        study_ref = ET.SubElement(experiment, "STUDY_REF");
        design = ET.SubElement(experiment, "DESIGN");
        design_description = ET.SubElement(design, "DESIGN_DESCRIPTION");
        sample_descriptor = ET.SubElement(design, "SAMPLE_DESCRIPTOR");
        sample_descriptor.set("refname", sample["sample_name"]);
        lib_descript  = ET.SubElement(design, "LIBRARY_DESCRIPTOR");
        lib_name = ET.SubElement(lib_descript, "LIBRARY_NAME");
        lib_strategy = ET.SubElement(lib_descript, "LIBRARY_STRATEGY");
        lib_strategy.text = sample["library_strategy"];
        lib_source = ET.SubElement(lib_descript, "LIBRARY_SOURCE");
        lib_source.text = sample["library_source"];
        lib_selection = ET.SubElement(lib_descript, "LIBRARY_SELECTION");
        lib_selection.text = sample["library_selection"];
        lib_layout = ET.SubElement(design, "LIBRARY_LAYOUT");
        if sample["is_paired"]:
            paired = ET.SubElement(lib_layout, "PAIRED");
        else:
            single = ET.SubElement(lib_layout, "SINGLE");
        lib_construct= ET.SubElement(design, "LIBRARY_CONSTRUCTION_PROTOCOL");
        lib_construct.text = sample["library_design_description"];
        platform_wrap = ET.SubElement(experiment, "PLATFORM");
        platform = ET.SubElement(platform_wrap, sample["sequencing_platform"]);
        instrument = ET.SubElement(platform, "INSTRUMENT_MODEL");
        instrument.text = sample["sequencing_instrument"];
        exp_attrs = ET.SubElement(experiment, "EXPERIMENT_ATTRIBUTES");
        exp_attr = ET.SubElement(exp_attrs, "EXPERIMENT_ATTRIBUTE");
        prep_date_tag = ET.SubElement(exp_attr, "TAG");
        prep_date_tag.text = "library preparation date";
        prep_date_value = ET.SubElement(exp_attr, "VALUE");
        prep_date_value.text = sample["library_preparation_date"];
        return experiment;


    @classmethod
    def create_xml(cls, sample_ids):
        experiment_set = ET.Element("EXPERIMENT_SET");
        for sample_id in sample_ids:
            experiment = cls.create_experiment_xml(sample_id);
            experiment_set.append(experiment);
        return ET.tostring(experiment_set);
