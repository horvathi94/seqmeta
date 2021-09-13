import os.path
from zipfile import ZipFile
import gzip
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from application.src.seqfiles.types import SeqFileTypes
from .tsvs.samples import EnaTsvSamples
from .tsvs.experiment import EnaTsvExperiment
from .manifests.runs import EnaManifestRun
from .manifest import EnaManifest
#from .runs_manifest import EnaManifestRun
from . import assemblies_manifest as assembman


import sys


class EnaMeta(TempFile):

    tempfilename = "last_generated_ena.zip";
    attachement_prefix = "ena_";
    extension = "zip";


    @classmethod
    def write_contigs_manifest(cls, zipObj: "zip", sample: Samples) -> None:
        sample_name = sample["sample_name"];
        assembman.EnaContigs.write(sample);
        zipObj.write(assembman.EnaContigs.get_tempfile(),
                     assembman.EnaContigs.manifest_in_zip(sample_name));


    @classmethod
    def write_contigs_file(cls, zipObj: "zip",
                           seqbunch: SeqFilesBunch) -> None:
        tempname = os.path.join(cls.samples_temp_dir, "ena_contigs_file");
        tempfile = seqbunch.write_tempfile_ena(SeqFileTypes.CONTIGS, tempname);
        file_in_zip = os.path.join(assembman.EnaContigs.zip_dir,
                                   seqbunch.contigs_file.get_ena_filename());
        zipObj.write(tempfile, file_in_zip);


    @classmethod
    def write_contigs_data(cls, zipObj: "zip",
                           seqbunch: SeqFilesBunch, sample: Samples) -> None:
        cls.write_contigs_manifest(zipObj, sample);
        cls.write_contigs_file(zipObj, seqbunch);


    @classmethod
    def write_scaffolds_manifest(cls, zipObj: "zip", sample: Samples) -> None:
        sample_name = sample["sample_name"];
        assembman.EnaScaffolds.write(sample);
        zipObj.write(assembman.EnaScaffolds.get_tempfile(),
                    assembman.EnaScaffolds.manifest_in_zip(sample_name));


    @classmethod
    def write_scaffolds_file(cls, zipObj: "zip",
                             seqbunch: SeqFilesBunch) -> None:
        tempname = os.path.join(cls.samples_temp_dir, "ena_scaffolds_file");
        tempfile = seqbunch.write_tempfile_ena(SeqFileTypes.SCAFFOLDS,
                                               tempname);
        file_in_zip = os.path.join(assembman.EnaScaffolds.zip_dir,
                            seqbunch.scaffolds_file.get_ena_filename());
        zipObj.write(tempfile, file_in_zip);


    @classmethod
    def write_scaffolds_data(cls, zipObj: "zip",
                             seqbunch: SeqFilesBunch, sample: Samples) -> None:
        cls.write_scaffolds_manifest(zipObj, sample);
        cls.write_scaffolds_file(zipObj, seqbunch);


    @classmethod
    def write_samples_tsv(cls, samp_ids: list) -> None:
        """Write samples.tsv for samples submission."""
        samp_tab = "view_samples_ena";
        samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids);
        EnaTsvSamples.write(samples);
        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(EnaTsvSamples.get_tempfile(), EnaTsvSamples.filename);


    @classmethod
    def write_experiments_tsv(cls, samp_ids: list) -> None:
        """Write experiments.tsv for experiments data submission"""
        samp_tab = "view_samples_ena_experiment";
        run_samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids);
        EnaTsvExperiment.write(run_samples);
        with ZipFile(cls.get_tempfile(), "a") as zipObj:
            zipObj.write(EnaTsvExperiment.get_tempfile(),
                         EnaTsvExperiment.filename);


    @classmethod
    def write_read_file(cls, zipObj: "zip", seqbunch: SeqFilesBunch,
                         sample: Samples) -> None:
        sample_alias = sample["sample_alias"];
        EnaManifestRun.write(sample);
        zipObj.write(EnaManifestRun.get_tempfile(),
            EnaManifestRun.manifest_in_zip(sample_alias));
        for read in seqbunch.reads:
            in_zip = f"{EnaManifestRun.zip_dir}/{read.get_filename()}";
            zipObj.write(read.get_file(), in_zip);



    @classmethod
    def write_reads_data(cls, samp_ids: list) -> None:
        """Write read files and manifest files to zip file."""
        samp_tab = "view_samples_ena_experiment";
        run_samples = Samples.fetch_entries(samp_tab, sample_ids=samp_ids);

        with ZipFile(cls.get_tempfile(), "a") as zipObj:
            for sample in run_samples:
                sample_alias = sample["sample_alias"];
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                if not seqbunch.check_reads(): continue;

                read_file_names = [];
                for read in seqbunch.reads:
                    read_name = read.get_filename();
                    in_zip = EnaManifestRun.in_zip(read_name);
                    read_file_names.append(read_name);
                    zipObj.write(read.get_file(), in_zip);

                EnaManifestRun.write(sample, read_file_names);
                zipObj.write(EnaManifestRun.get_tempfile(),
                             EnaManifestRun.manifest_in_zip(sample_alias));




    @classmethod
    def write_zip(cls, selected):

        cls.write_samples_tsv(selected);
        cls.write_experiments_tsv(selected);
        cls.write_reads_data(selected);

        assembly_samples = Samples.fetch_entries(
            "view_samples_ena_manifest_assembly", sample_ids=selected);
        samples = Samples.fetch_entries("view_samples_base",
                                        sample_ids=selected);


#        with ZipFile(cls.get_tempfile(), "w") as zipObj:
#            zipObj.write(EnaTsvSamples.get_tempfile(),
#                         EnaTsvSamples.filename);
#            zipObj.write(EnaTsvExperiment.get_tempfile(),
#                         EnaTsvExperiment.filename);

            # Write read files: 
#            for sample in run_samples:
#                seqbunch = SeqFilesBunch(sample["sample_id"]);
#                if not seqbunch.check_reads(): continue;
#                cls.write_reads_data(zipObj, seqbunch, sample);

            # Write assembly files:
#            for sample in assembly_samples:
#                seqbunch = SeqFilesBunch(sample["sample_id"]);
#                if seqbunch.contigs_file.check_exists():
#                    cls.write_contigs_data(zipObj, seqbunch, sample);
#                if seqbunch.scaffolds_file.check_exists():
#                    cls.write_scaffolds_data(zipObj, seqbunch, sample);
#

