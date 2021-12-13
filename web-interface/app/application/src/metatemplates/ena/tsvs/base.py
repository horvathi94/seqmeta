import csv
from application.src.metatemplates.base.tempfile import TempFile


class _EnaTsvBase(TempFile):

    tempfilename = "last_generated_ena.tsv"
    attachment_prefix = "ena"
    extension = "tsv"


    @classmethod
    def generate_header(cls, *args, **kwargs) -> list:
        pass


    @classmethod
    def write_header(cls, *args, **kwargs) -> None:
        header = cls.generate_header(*args, **kwargs)
        with open(cls.get_tempfile(), "w") as tsv_file:
            tsvw = csv.writer(tsv_file, delimiter="\t")
            tsvw.writerow(header)


    @classmethod
    def generate_sample_data(cls, sample: dict) -> list:
        pass


    @classmethod
    def write_sample_data(cls, samples: list) -> None:
        with open(cls.get_tempfile(), "a") as tsv_file:
            tsvw = csv.writer(tsv_file, delimiter="\t")
            for sample in samples:
                tsvw.writerow(cls.generate_sample_data(sample))


    @classmethod
    def write(cls, samples) -> None:
        cls.write_header()
        cls.write_sample_data(samples)
