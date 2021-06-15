import csv
from .base.excel_gen import ExcelGenerator
from .base.tempfile import TempFile

class EnaTsv(TempFile):

    tempfilename = "last_generated_ena.tsv";
    attachment_prefix = "ena";
    extension = "tsv";


    @classmethod
    def write_header(cls, head, units):
        with open(cls.get_tempfile(), "w") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t");
            tsv_writer.writerow(["#checklist_accession"]);
            tsv_writer.writerow(["ERC000033"]);
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
                row = [sample[key] for key in head[3:]];
                row = [sample["sample_name"]] + [""]*2 + row;
                tsv_writer.writerow(row);



class EnaExcel(ExcelGenerator):

    tempfilename = "last_generated_ena.xls";
    attachment_prefix = "ena";
    extension = "xls";

    @classmethod
    def populate(cls, ws, samples):
        ws["A1"] = "#checklist_accession";
        ws["B1"] = "ERC000033";
        ws["A2"] = "#unique_name_prefix";
        ws["A3"] = "sample_alias";
        ws["B3"] = "tax_id";
        ws["A4"] = "#template";
        ws["B4"] = "2697049";
        ws["A5"] = "#units";


    @classmethod
    def write(cls, samples):
        wb, ws = cls.create_worksheet("Submissions");
        cls.populate(ws, samples);
        cls.save_excel(wb, cls.get_tempfile());
        wb.close();
