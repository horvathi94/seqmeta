import csv
from ..base.tempfile import TempFile


class _EnaManifestBase(TempFile):

    tempfilename = "last_generated_ena_manifest.tsv";
    attachment_prefix = "ena";
    extension = "txt";


    @classmethod
    def clean(cls, sample: dict) -> dict:
        return sample;


    @classmethod
    def write(cls, sample):
        sample = cls.clean(sample);
        with open(cls.get_tempfile(), "w") as tsvf:
            tsvw = csv.writer(tsvf, delimiter="\t");
            for field in sample:
                if field == "sample_id": continue;
                tsvw.writerow([field, sample[field]]);






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


