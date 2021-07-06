import os.path
from zipfile import ZipFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch
from ..base.tempfile import TempFile
from .samples import EnaTsv
from .experiment import EnaExperiment
from .manifest import EnaManifest

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

        samples = Samples.fetch_entries("view_samples_base",
                                        sample_ids=selected);

        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(EnaTsv.get_tempfile(), "samples.tsv");
            zipObj.write(EnaExperiment.get_tempfile(), "experiments.tsv");

            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                fwread = seqbunch.get_reads(tp="fwread");
                if not fwread is None:
                    zipObj.write(fwread,
                            "reads/"+seqbunch.forward_reads[0]["filename"]);
                rvread = seqbunch.get_reads(tp="rvread");
                if not rvread is None:
                    zipObj.write(rvread,
                            "reads/"+seqbunch.reverse_reads[0]["filename"]);

                manifest_sample ,= Samples.fetch_entries(
                    "view_samples_ena_manifest",
                    sample_ids=[sample["sample_id"]]);
                EnaManifest.write(manifest_sample);
                zipObj.write(EnaManifest.get_tempfile(),
                             "assemblies/manifest_"+sample["sample_name"]+".txt");

                assembly = seqbunch.get_assembly_file();
                if not assembly is None:
                    zipObj.write(assembly,
                            "assemblies/"+seqbunch.assembly_file["filename"]);
