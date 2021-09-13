import os
import csv
from application.src.metatemplates.base.tempfile import TempFile


class _EnaManifestBase(TempFile):

    tempfilename = "last_generated_ena_manifest.tsv";
    attachment_prefix = "ena";
    extension = "txt";
    zip_dir = None;


    @classmethod
    def in_zip(cls, file: str) -> str:
        """Returns file and path in zip"""
        return os.path.join(cls.zip_dir, file);


    @classmethod
    def manifest_in_zip(cls, name: str) -> str:
        """Returns manifest file and path in zip"""
        return cls.in_zip(f"{name}_manifest.txt");


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




