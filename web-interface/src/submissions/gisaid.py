import pathlib
from typing import List
from openpyxl import Workbook
from zipfile import ZipFile
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from .excel import ExcelFile


COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]


class Metadata:

    path = "/home/seqmeta/uploads/samples"

    def __init__(self):
        self.sample_count = 0
        self.excel = ExcelFile(filename="upload", title="Submission")
        self.sequences = []
        self.assemblies_filename = "all"


    @property
    def assemblies_file(self) -> pathlib.Path:
        fname = self.assemblies_filename.split(".")[0] + ".fasta"
        return pathlib.Path(self.path, fname)


    def create_header(self, sample: "Sample") -> None:
        for index, a in enumerate(sample.list_gisaid()):
            self.excel.write_cell(1, index, a.gisaid_header)
            self.excel.write_cell(2, index, a.gisaid_name)


    @property
    def row_index(self) -> int:
        return self.sample_count + 3


    def append_assembly(self, sample: "Sample") -> None:
        assembly_file = sample.load_gisaid_assembly()
        rec = SeqIO.read(assembly_file.file, "fasta")
        rec.id = sample.gisaid_virusname
        rec.name = sample.gisaid_virusname
        rec.description = ""
        self.sequences.append(rec)


    def add_sample(self, sample: "Sample") -> None:
        self.append_assembly(sample)
        for index, a in enumerate(sample.list_gisaid()):
            self.excel.write_cell(self.row_index, index, a.value)
        self.sample_count += 1


    def add_samples(self, samples: List["Sample"]) -> None:
        self.create_header(samples[0])
        self.assemblies_filename = samples[0].gisaid_filename
        for s in samples:
            self.add_sample(s)


    def write(self) -> None:
        self.excel.write()
        SeqIO.write(self.sequences, self.assemblies_file, "fasta")
