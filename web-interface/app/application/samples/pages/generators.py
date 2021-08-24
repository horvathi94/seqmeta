from flask import send_file, redirect, url_for
from application.src.metatemplates.gisaid.main import GisaidMeta
from application.src.metatemplates.ena.main import EnaMeta
from application.src.metatemplates.ncbi.main import NcbiMeta
from application.src.seqfiles.seqfile_bunch import SeqFilesBunch



class GeneratorBase:


    @classmethod
    def write_zip(cls, selected: list) -> None:
        """Write zip files which will be sent."""
        pass;


    @classmethod
    def get_zip(cls) -> "zipfile":
        """Returns the zip file which will be sent."""
        pass;


    @classmethod
    def get_attachment_name(cls) -> str:
        """Returns the filename of the attachement."""
        pass;


    @classmethod
    def redirect_if_empty(cls) -> "flask.redirect":
        """Redirect to this page if there are no selected values."""
        return redirect(url_for("samples_bp.show"));


    @classmethod
    def render(cls, selected: list) -> "flask.send_file":
        """Returns flask.send_file of zipped data."""
        if len(selected) == 0:
            return cls.redirect_if_empty();
        cls.write_zip(selected);
        return send_file(cls.get_zip(),
                         attachment_filename=cls.get_attachment_name());



class Gisaid(GeneratorBase):


    @classmethod
    def write_zip(cls, selected: list) -> None:
        GisaidMeta.write_zip(selected);


    @classmethod
    def get_zip(cls) -> "zipfile":
        return GisaidMeta.get_tempfile();


    @classmethod
    def get_attachment_name(cls) -> str:
        return GisaidMeta.get_attachment_filename();




class Ena(GeneratorBase):


    @classmethod
    def write_zip(cls, selected: list) -> None:
        EnaMeta.write_zip(selected);


    @classmethod
    def get_zip(cls) -> "zipfile":
        return EnaMeta.get_tempfile();


    @classmethod
    def get_attachment_name(cls) -> str:
        return EnaMeta.get_attachment_filename();





class Ncbi(GeneratorBase):


    @classmethod
    def write_zip(cls, selected: list) -> None:
        NcbiMeta.write_zip(selected);


    @classmethod
    def get_zip(cls) -> "zipfile":
        return NcbiMeta.get_tempfile();


    @classmethod
    def get_attachment_name(cls) -> str:
        return NcbiMeta.get_attachment_filename();




class ConcatConsensus(GeneratorBase):


    @classmethod
    def render(cls, selected: list) -> str:
        if len(selected) == 0:
            return cls.redirect_if_empty();
        concat = "";
        for sid in selected:
            seqbunch = SeqFilesBunch(sid);
            concat+= str(seqbunch.get_consensus_sequence());
        return concat;

