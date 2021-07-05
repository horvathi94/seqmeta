import csv
from ..base.tempfile import TempFile


class EnaManifest(TempFile):

    tempfilename = "last_generated_ena_manifest.tsv";
    attachment_prefix = "ena";
    extension = "txt";


    @classmethod
    def write(cls, sample):
        with open(cls.get_tempfile(), "w") as tsvf:
            tsvw = csv.writer(tsvf, delimiter="\t");
            for field in sample:
                if field == "sample_id": continue;
                tsvw.writerow([field, sample[field]]);


