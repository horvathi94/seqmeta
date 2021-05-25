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
