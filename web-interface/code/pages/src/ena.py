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



class Sample(DBInterface):

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
    def create_xml(cls, sample_id):
        sample ,= Cursor.select("view_samples_ena",
                    clauses="WHERE `sample_id` = {:d}".format(sample_id));

        sample_set = ET.Element("SAMPLE_SET");
        attr = cls.attr("ENA-CHECKLIST", "ERC000033");
        sample_set.append(attr);

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

            sample_set.append(attr);

        return ET.tostring(sample_set);
