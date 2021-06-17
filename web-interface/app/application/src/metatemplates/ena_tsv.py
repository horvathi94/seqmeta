import csv
from .base.excel_gen import ExcelGenerator
from .base.tempfile import TempFile

class EnaTsv(TempFile):

    tempfilename = "last_generated_ena.tsv";
    attachment_prefix = "ena";
    extension = "tsv";

    taxonomy = {
        "tax_id": 2697049,
        "scientific_name": "Severe acute respiratory syndrome coronavirus 2",
    };


    @classmethod
    def write_header(cls, head, units):
        with open(cls.get_tempfile(), "w") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t");
            tsv_writer.writerow(["#checklist_accession", "ERC000033"]);
            tsv_writer.writerow(["#unique_name_prefix"]);
            tsv_writer.writerow(head);
            tsv_writer.writerow(units);
            tsv_writer.writerow(["#units"]);


    @classmethod
    def generate_header(cls, sample):
        head = ["sample_alias", "tax_id", "scientific_name"];
        units = ["#template",
                 "2697049",
                 "Severe acute respiratory syndrome coronavirus 2"];
        for key in sample:
            if key == "sample_id":
                continue;
            head.append(key);
            if key == "host age":
                units.append("years");
            elif key in ["geographic location (latitude)",
                         "geographic location (longitude)"]:
                units.append("DD");
            else:
                units.append("");
        return head, units;


    @classmethod
    def write(cls, samples):
        head, units = cls.generate_header(samples[0]);
        cls.write_header(head, units);
        with open(cls.get_tempfile(), "a") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t");
            for sample in samples:
                sample["sample_alias"] = sample["sample_name"];
                sample["tax_id"] = cls.taxonomy["tax_id"];
                sample["scientific_name"] = cls.taxonomy["scientific_name"];
                row = [sample[key] for key in head];
                tsv_writer.writerow(row);


