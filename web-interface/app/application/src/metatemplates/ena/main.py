import os.path
from zipfile import ZipFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch
from ..base.tempfile import TempFile
from .samples import EnaTsv
from .experiment import EnaExperiment

class EnaMeta(TempFile):

    tempfilename = "last_generated_ena.zip";
    attachement_prefix = "ena_";
    extension = "zip";

    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_ena",
                                        sample_ids=selected);
        EnaTsv.write(samples);

        samples = Samples.fetch_entries("view_samples_ena_experiment",
                                        sample_ids=selected);
        EnaExperiment.write(samples);

        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(EnaTsv.get_tempfile(), "samples.tsv");
            zipObj.write(EnaExperiment.get_tempfile(), "experiments.tsv");

            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                fwread = seqbunch.get_reads(tp="fwread");
                if not fwread is None:
                    zipObj.write(fwread,
                                 seqbunch.forward_reads[0]["filename"]);
                rvread = seqbunch.get_reads(tp="rvread");
                if not rvread is None:
                    zipObj.write(rvread,
                                 seqbunch.reverse_reads[0]["filename"]);


