import os.path
from zipfile import ZipFile
import gzip
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch import SeqFilesBunch
from ..base.tempfile import TempFile
from .samples import EnaTsv
from .experiment import EnaExperiment
from .manifest import EnaManifest
from .runs_manifest import EnaManifestRun
from . import assemblies_manifest as assembman


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
                sb = SeqFilesBunch(sample["sample_id"]);
                if not sb.has_reads():
                    continue;
                EnaManifestRun.write(sample);
                zipObj.write(EnaManifestRun.get_tempfile(),
                    EnaManifestRun.manifest_in_zip(sample["sample_alias"]));
                for read in sb.read_files:
                    zipObj.write(read.get_file(),
                        f"{EnaManifestRun.zip_dir}/{read.get_filename()}");


            # Write assembly files:
            for sample in assembly_samples:
                sb = SeqFilesBunch(sample["sample_id"]);
                sname = sample["sample_name"];

                if sb.contigs_file.exists:
                    assembman.EnaContigs.write(sample);
                    zipObj.write(assembman.EnaContigs.get_tempfile(),
                                 assembman.EnaContigs.manifest_in_zip(sname));

                    tempfile = "ena_contigs_file.fa.gz";
                    file = os.path.join("/uploads/samples/temp", tempfile);
                    sb.write_ena_contigs_tempfile(file);
                    zipObj.write(file,
                                 f"{assembman.EnaContigs.zip_dir}/" \
                                 f"{sb.contigs_file.get_filename()}.gz");


                if sb.scaffolds_file.exists:
                    assembman.EnaScaffolds.write(sample);
                    zipObj.write(assembman.EnaScaffolds.get_tempfile(),
                                assembman.EnaScaffolds.manifest_in_zip(sname));
                    tempfile = "ena_scaffolds_file.fa.gz";
                    file = os.path.join("/uploads/samples/temp", tempfile);
                    sb.write_ena_contigs_tempfile(file);
                    zipObj.write(file,
                                 f"{assembman.EnaScaffolds.zip_dir}/" \
                                 f"{sb.scaffolds_file.get_filename()}.gz");

