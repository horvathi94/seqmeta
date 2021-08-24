import os.path
from zipfile import ZipFile
import gzip
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunchNew
from ..base.tempfile import TempFile
from .samples import EnaTsv
from .experiment import EnaExperiment
from .manifest import EnaManifest
from .runs_manifest import EnaManifestRun
from .assemblies_manifest import EnaManifestAssembly

class EnaMeta(TempFile):

    tempfilename = "last_generated_ena.zip";
    attachement_prefix = "ena_";
    extension = "zip";

    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_ena",
                                        sample_ids=selected);
        EnaTsv.write(samples);

        run_samples = Samples.fetch_entries("view_samples_ena_experiment",
                                        sample_ids=selected);

        assembly_samples = Samples.fetch_entries(
            "view_samples_ena_manifest_assembly", sample_ids=selected);
        EnaExperiment.write(run_samples);

        samples = Samples.fetch_entries("view_samples_base",
                                        sample_ids=selected);


        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(EnaTsv.get_tempfile(), "samples.tsv");
            zipObj.write(EnaExperiment.get_tempfile(), "experiments.tsv");

            # Write read files: 
            for sample in run_samples:
                EnaManifestRun.write(sample);
                zipObj.write(EnaManifestRun.get_tempfile(),
                    EnaManifestRun.manifest_in_zip(sample["sample_alias"]));
                sb = SeqFilesBunchNew(sample["sample_id"]);
                for read in sb.read_files:
                    zipObj.write(read.get_file(),
                                 f"{EnaManifestRun.zip_dir}/{read.filename}");

#            for sample in assembly_samples:
#                EnaManifestAssembly.write(sample, "contigs");
#                zipObj.write(EnaManifestAssembly.get_tempfile(),
#                  f"assemblies/contigs/{sample['sample_name']}_manifest.txt");
#
#            for sample in assembly_samples:
#                EnaManifestAssembly.write(sample, "scaffolds");
#                zipObj.write(EnaManifestAssembly.get_tempfile(),
#                  f"assemblies/scaffolds/{sample['sample_name']}_manifest.txt");
#
#            for sample in samples:
#
#                seqbunch = SeqFilesBunch(sample["sample_id"]);
#
#                if seqbunch.has_fwreads_file():
#                    fwread = seqbunch.get_reads(tp="fwread");
#                    zipObj.write(fwread,
#                            "reads/"+seqbunch.forward_reads[0]["filename"]);
#
#                if seqbunch.has_rvreads_file():
#                    rvread = seqbunch.get_reads(tp="rvread");
#                    zipObj.write(rvread,
#                            "reads/"+seqbunch.reverse_reads[0]["filename"]);
#
##                manifest_sample ,= Samples.fetch_entries(
##                    "view_samples_ena_manifest",
##                    sample_ids=[sample["sample_id"]]);
##                EnaManifest.write(manifest_sample);
##                zipObj.write(EnaManifest.get_tempfile(),
##                        "assemblies/manifest_"+sample["sample_name"]+".txt");
#
#                if seqbunch.has_assembly_file():
#                    assembly = seqbunch.get_assembly_file();
#                    zipObj.write(assembly,
#                            "assemblies/"+seqbunch.assembly_file["filename"]);
