import os.path
from zipfile import ZipFile
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunchNew
from .samples import NcbiSample
from .experiment import NcbiExperiment


class NcbiMeta(TempFile):

    tempfilename = "last_generated_ncbi.zip";
    attachement_prefix = "ncbi_";
    extension = "zip";


    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_ncbi",
                                        sample_ids=selected);
        NcbiSample.write(samples);

        samples = Samples.fetch_entries("view_samples_ncbi_experiment",
                                        sample_ids=selected);

        NcbiExperiment.write(samples);

        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(NcbiSample.get_tempfile(), "samples.xlsx");
            zipObj.write(NcbiExperiment.get_tempfile(), "sra.xlsx");

            # Write read files: 
            for sample in samples:
                sb = SeqFilesBunchNew(sample["sample_id"]);
                if not sb.has_reads():
                    continue;

                for read in sb.read_files:
                    zipObj.write(read.get_file(),
                                 f"reads/{read.filename}");

