import os
from zipfile import ZipFile
from .submission import GisaidExcel
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch import SeqFilesBunch

import sys

class GisaidMeta(TempFile):

    tempfilename = "last_generated_gisaid.zip";
    attachement_prefix = "gisaid_";
    extension = "zip";


    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);
        GisaidExcel.write_gisaid(samples);


        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(GisaidExcel.get_tempfile(), "submission.xlsx");

            for sample in samples:
                seqbunch = SeqFilesBunch(sample["sample_id"]);
                if not seqbunch.consensus_file.exists:
                    continue;

                path = "/uploads/samples/temp/";
                if not os.path.exists(path): os.makedirs(path);
                file = os.path.join(path, "temp_gisaid.fa");
                print(f"Path {path} ({os.path.exists(path)})", file=sys.stderr)
                seqbunch.write_gisiad_tempfile(file);
                zipObj.write(file, seqbunch.consensus_file.get_filename());

