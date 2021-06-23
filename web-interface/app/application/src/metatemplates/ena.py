import os.path
from zipfile import ZipFile
from application.src.samples.samples import Samples
from .base.tempfile import TempFile
from .ena_sample_set import SampleSet
from .ena_experiment_set import ExperimentSet
from .ena_tsv import EnaTsv
from .ena_experiment import EnaExperiment

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


#        SampleSet.save_xml(samples);
#
#        experiments = Samples.fetch_entries("view_samples_ena_experiment",
#                                     sample_ids=selected);
#        ExperimentSet.save_xml(experiments);
#
#        with ZipFile(cls.get_tempfile(), "w") as zipObj:
#            zipObj.write(SampleSet.get_tempfile(), "sample_set.xml");
#            zipObj.write(ExperimentSet.get_tempfile(), "experiment_set.xml");
#
