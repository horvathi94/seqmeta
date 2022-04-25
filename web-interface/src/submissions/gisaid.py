import pathlib
from typing import List
from openpyxl import Workbook


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


    @property
    def file(self) -> pathlib.PurePath:
        return pathlib.PurePath(self.path, self.filename)


    def write_cell(self, rindex: int, cindex: int, val: any) -> None:
        ws_index = f"{COLUMNS[cindex-1]}{rindex}"
        self.worksheet[ws_index] = val


    def create_header(self, sample: "Sample") -> None:
        for a in sample.gisaid_attributes:
            self.write_cell(2, a["index"], a["tag"])


    @property
    def row_index(self) -> int:
        return self.sample_count + 3


    def add_sample(self, sample: "Sample") -> None:
        for a in sample.gisaid_attributes:
            self.write_cell(self.row_index, a["index"], a["value"])
        self.sample_count += 1


    def add_samples(self, samples: List["Sample"]) -> None:
        self.create_header(samples[0])
        for s in samples:
            self.add_sample(s)


    def write(self) -> None:
        self.workbook.save(filename=self.file)
