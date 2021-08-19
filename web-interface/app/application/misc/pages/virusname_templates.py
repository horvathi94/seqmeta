from flask import render_template
from dataclasses import dataclass
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna


@dataclass
class VirusnameTemplateEditor:

    html_source: str = ""
    virusname_format: str = "";
    available_db_keys = [];

    @classmethod
    def render(cls) -> "HTML":
        return render_template(cls.html_source,
                               virusname_format=cls.virusname_format,
                               available_db_keys=cls.available_db_keys);


@dataclass
class GisaidVirusnameEditor(VirusnameTemplateEditor):

    html_source = "misc/virusname.html";
    virusname_format = VirusnameGisaid.fetch_format_string();
    available_db_keys = VirusnameGisaid.available_db_keys();



@dataclass
class EnaVirusnameEditor(VirusnameTemplateEditor):

    html_source = "misc/isolate_ena.html";
    virusname_format = IsolateEna.fetch_format_string();
    available_db_keys = IsolateEna.available_db_keys();
