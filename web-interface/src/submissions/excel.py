import pathlib
from openpyxl import Workbook


COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]


class ExcelFile:

    path = "/home/seqmeta/uploads/samples/"


    def __init__(self, filename="upload", title="Submission"):
        self.filename = filename
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.title = title


    @property
    def file(self) -> pathlib.Path:
        fname = self.filename.split(".")[0] + ".xlsx"
        return pathlib.Path(self.path, fname)


    def write_cell(self, rindex: int, cindex: int, val: any) -> None:
        ws_index = f"{COLUMNS[cindex-1]}{rindex}"
        self.worksheet[ws_index] = val


    def write(self) -> None:
        self.workbook.save(filename=self.file)
