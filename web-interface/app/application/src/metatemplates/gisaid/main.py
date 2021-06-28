import os.path
from zipfile import ZipFile
from .submission import GisaidExcel
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch

class GisaidMeta(TempFile):

    tempfilename = "last_generated_gisaid.zip";
    attachement_prefix = "gisaid_";
    extension = "zip";


    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);
        GisaidExcel.write_gisaid(samples);

        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(GisaidExcel.get_tempfile(), "submission.xlsx");
            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                seqbunch.write_gisiad_tempfile();
                if seqbunch.has_assembly_file():
                    zipObj.write(seqbunch.get_tempfile(),
                                 seqbunch.assembly_file["filename"]);


