import os.path
from zipfile import ZipFile
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from .samples import NcbiSample
from .experiment import NcbiExperiment


class NcbiMeta(TempFile):

    tempfilename = "last_generated_ncbi.zip"
    attachement_prefix = "ncbi_"
    extension = "zip"


    @classmethod
    def write_samples(cls, samp_ids: list) -> None:
        samp_tab = "view_samples_ncbi"
        samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids)
        NcbiSample.write(samples)
        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(NcbiSample.get_tempfile(), NcbiSample.filename)


    @classmethod
    def write_experiment(cls, samp_ids: list) -> None:
        samp_tab = "view_samples_ncbi_experiment"
        samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids)
        for sample in samples:
            seqbunch = SeqFilesBunch(sample["sample_id"])
            if not seqbunch.check_reads(): continue
            for i, r in enumerate(seqbunch.reads):
                key = f"filename{i}" if i > 0 else "filename"
                sample[key] = r.get_filename()


        NcbiExperiment.write(samples)
        with ZipFile(cls.get_tempfile(), "a") as zipObj:
            zipObj.write(NcbiExperiment.get_tempfile(),
                         NcbiExperiment.filename)


    @classmethod
    def write_reads_data(cls, samp_ids: list) -> None:
        samp_tab = "view_samples_ncbi_experiment"
        samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids)

        with ZipFile(cls.get_tempfile(), "a") as zipObj:
            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"])
                if not seqbunch.check_reads(): continue
                for read in seqbunch.reads:
                    in_zip = f"reads/{read.get_filename()}"
                    zipObj.write(read.get_file(), in_zip)


    @classmethod
    def write_zip(cls, selected):

        cls.write_samples(selected)
        cls.write_experiment(selected)
        cls.write_reads_data(selected)


#            # Write read files: 
