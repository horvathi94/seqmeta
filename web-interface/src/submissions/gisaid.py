import pathlib
from typing import List
from openpyxl import Workbook
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]


class Metadata:

    title = "Submission"
    filename = "test.xlsx"
    path = "/home/seqmeta/uploads/samples"

    def __init__(self):
        self.sample_count = 0
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.title = self.title
        self.records = []


    @property
    def file(self) -> pathlib.PurePath:
        return pathlib.PurePath(self.path, self.filename)


    def write_cell(self, rindex: int, cindex: int, val: any) -> None:
        ws_index = f"{COLUMNS[cindex-1]}{rindex}"
        self.worksheet[ws_index] = val


    def create_header(self, sample: "Sample") -> None:
        for index, a in enumerate(sample.list_gisaid()):
            self.write_cell(1, index, a.gisaid_header)
            self.write_cell(2, index, a.gisaid_name)


    @property
    def row_index(self) -> int:
        return self.sample_count + 3


    def append_assembly(self, sample: "Sample") -> None:
        assembly_file = sample.load_gisaid_assembly()
        rec = SeqIO.read(assembly_file.file, "fasta")
        self.records.append(rec.seq)
        print(assembly_file)
        print(rec)
        print(f"Virusname: {sample.gisaid_virusname}")
#        print(rec.seq)


    def add_sample(self, sample: "Sample") -> None:
        self.append_assembly(sample)
        for index, a in enumerate(sample.list_gisaid()):
            self.write_cell(self.row_index, index, a.value)
        self.sample_count += 1


    def add_samples(self, samples: List["Sample"]) -> None:
        self.create_header(samples[0])
        for s in samples:
            self.add_sample(s)


    def write(self) -> None:
        self.workbook.save(filename=self.file)
