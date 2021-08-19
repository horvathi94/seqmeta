from flask import render_template, redirect, url_for
from dataclasses import dataclass
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna


@dataclass
class VirusnameTemplateEditor:

    html_source: str = ""
    available_db_keys = [];
    redirect_after_save = "misc_bp.edit";


    @classmethod
    def get_format(cls) -> str:
        """Fetch virusname format string from the database."""
        pass;

    @classmethod
    def render(cls) -> "HTML":
        return render_template(cls.html_source,
                               virusname_format=cls.get_format(),
                               available_db_keys=cls.available_db_keys);


    @classmethod
    def save(cls, virusname: str) -> None:
        """Save virusname to the database."""
        pass;


    @classmethod
    def save_and_redirect(cls, virusname: str) -> "flask.redirect":
        """Save virusname and redirect"""
        cls.save(virusname);
        return redirect(url_for(cls.redirect_after_save));



@dataclass
class GisaidVirusnameEditor(VirusnameTemplateEditor):

    html_source = "misc/virusname.html";
    available_db_keys = VirusnameGisaid.available_db_keys();


    @classmethod
    def get_format(cls) -> str:
        return VirusnameGisaid.fetch_format_string()

    @classmethod
    def save(cls, virusname: str) -> None:
        VirusnameGisaid.call_save_procedure(virusname);



@dataclass
class EnaVirusnameEditor(VirusnameTemplateEditor):

    html_source = "misc/isolate_ena.html";
    available_db_keys = IsolateEna.available_db_keys();

    @classmethod
    def get_format(cls) -> str:
        return IsolateEna.fetch_format_string();

    @classmethod
    def save(cls, virusname: str) -> None:
        IsolateEna.call_save_procedure(virusname);
