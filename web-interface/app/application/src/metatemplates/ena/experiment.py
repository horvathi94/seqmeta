import csv
from ..base.excel_gen import ExcelGenerator
from ..base.tempfile import TempFile


class EnaExperiment(TempFile):

    tempfilename = "last_generated_ena_experiments.tsv";
    attachment_prefix = "ena";
    extension = "tsv";


    @classmethod
    def generate_header(cls, is_paired, seq_instrument):
        header = [
            "sample_alias",
            "instrument_model",
            "library_name",
            "library_source",
            "library_selection",
            "library_strategy",
            "design_description",
            "library_construction_protocol",
            "insert_size"];
        if is_paired:
            header += [
                "forward_file_name",
                "forward_file_md5",
                "reverse_file_name",
                "reverse_file_md5"];
        return header;


    @classmethod
    def write(cls, samples):
        template_sample = samples[0]
        head = cls.generate_header(template_sample["is_paired"],
                                   template_sample["instrument_model"]);
        with open(cls.get_tempfile(), "w") as tsvf:
            tsvw = csv.writer(tsvf, delimiter="\t");
            tsvw.writerow(head);
            for sample in samples:
                row = [sample[key] for key in head];
                tsvw.writerow(row);
