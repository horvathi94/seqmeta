import os.path
from zipfile import ZipFile
from .submission import GisaidExcel
from ..base.tempfile import TempFile
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunchNew


class GisaidMeta(TempFile):

    tempfilename = "last_generated_gisaid.zip";
    attachement_prefix = "gisaid_";
    extension = "zip";


    @classmethod
    def write_zip(cls, selected):

        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);
        print(f"GISAID: {samples}", file=sys.stderr)
        GisaidExcel.write_gisaid(samples);



        with ZipFile(cls.get_tempfile(), "w") as zipObj:
            zipObj.write(GisaidExcel.get_tempfile(), "submission.xlsx");

            for sample in samples:
                seqbunch = SeqFilesBunchNew(sample["sample_id"]);
                if not seqbunch.consensus_file.exists:
                    continue;

                file = os.path.join("/uploads/samples/temp", "temp_gisaid.fa");
                seqbunch.write_gisiad_tempfile(file);
                zipObj.write(file, seqbunch.consensus_file.filename);


