import os
from Bio import SeqIO
from zipfile import ZipFile
from .submission import GisaidExcel
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch

import sys

class GisaidMeta(TempFile):

    tempfilename = "last_generated_gisaid.zip";
    attachement_prefix = "gisaid_";
    extension = "zip";

    files_temp_dir = "/uploads/samples/temp"

    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);
        GisaidExcel.write_gisaid(samples);


        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(GisaidExcel.get_tempfile(), "submission.xlsx");


            tempfile = cls.get_sample_temp_file("temp_gisaid.fasta");

            sequences = [];
            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                if not seqbunch.consensus_file.check_exists():
                    continue;

                sequences.append(seqbunch.get_consensus_sequence());

            SeqIO.write(sequences, tempfile, "fasta")
            zipObj.write(tempfile, GisaidExcel.sequences_file);
