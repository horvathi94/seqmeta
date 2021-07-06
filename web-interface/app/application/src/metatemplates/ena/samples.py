import csv
from ..base.excel_gen import ExcelGenerator
from ..base.tempfile import TempFile


class EnaTsv(TempFile):

    tempfilename = "last_generated_ena.tsv";
    attachment_prefix = "ena";
    extension = "tsv";

    taxonomy = {
        "tax_id": 2697049,
        "scientific_name": "Severe acute respiratory syndrome coronavirus 2",
        "common_name": "",
    };


    @classmethod
    def write_header(cls, head, template, units):
        with open(cls.get_tempfile(), "w") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t");
            tsv_writer.writerow(["#checklist_accession", "ERC000033"]);
            tsv_writer.writerow(["#unique_name_prefix"]);
            tsv_writer.writerow(head);
            tsv_writer.writerow(template);
            tsv_writer.writerow(units);


    @classmethod
    def generate_header(cls, sample):
        head = ["sample_alias",
                "tax_id",
                "scientific_name",
                "common_name"];
        template = ["#template",
                    cls.taxonomy["tax_id"],
                    cls.taxonomy["scientific_name"],
                    cls.taxonomy["common_name"],];
        units = ["#units", "", "", ""];
        for key in sample:
            if key == "sample_id": continue;
            if key == "sample_name": continue;
            if key == "virus identifier": continue;
            head.append(key);
            if key == "host age":
                units.append("years");
            elif key in ["geographic location (latitude)",
                         "geographic location (longitude)"]:
                units.append("DD");
            else:
                units.append("");
        return head, template, units;


    @classmethod
    def write(cls, samples):
        head, template, units = cls.generate_header(samples[0]);
        cls.write_header(head, template, units);
        with open(cls.get_tempfile(), "a") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t");
            for sample in samples:
                sample["sample_alias"] = sample["sample_name"];
                sample["tax_id"] = cls.taxonomy["tax_id"];
                sample["scientific_name"] = cls.taxonomy["scientific_name"];
                sample["common_name"] = cls.taxonomy["common_name"];
                row = [sample[key] for key in head];
                tsv_writer.writerow(row);


