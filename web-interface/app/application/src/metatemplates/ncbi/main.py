import os.path
from zipfile import ZipFile
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch
from .samples import NcbiSample


class NcbiMeta(TempFile):

    tempfilename = "last_generated_ncbi.zip";
    attachement_prefix = "ncbi_";
    extension = "zip";


    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_ncbi",
                                        sample_ids=selected);
        NcbiSample.write(samples);

        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(NcbiSample.get_tempfile(), "samples.xlsx");
