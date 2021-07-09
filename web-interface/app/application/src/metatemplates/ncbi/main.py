import os.path
from zipfile import ZipFile
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch
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

            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);

                if seqbunch.has_fwreads_file():
                    fwread = seqbunch.get_reads(tp="fwread");
                    zipObj.write(fwread,
                            "reads/"+seqbunch.forward_reads[0]["filename"]);

                if seqbunch.has_rvreads_file():
                    rvread = seqbunch.get_reads(tp="rvread");
                    zipObj.write(rvread,
                            "reads/"+seqbunch.reverse_reads[0]["filename"]);
