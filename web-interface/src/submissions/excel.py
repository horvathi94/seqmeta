import pathlib
from openpyxl import Workbook


COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]


class ExcelFile:

    path = "/home/seqmeta/uploads/samples/"


    def __init__(self, filename="upload", title="Submission"):
        self._fname = filename
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.title = title


    @property
    def filename(self) -> str:
        return self._fname.split(".")[0] + ".xlsx"


    @filename.setter
    def filename(self, fname: str) -> None:
        self._fname = fname.split(".")[0] + ".xlsx"


    @property
    def file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.filename)


    def write_cell(self, rindex: int, cindex: int, val: any) -> None:
        ws_index = f"{COLUMNS[cindex-1]}{rindex}"
        self.worksheet[ws_index] = val


    def write(self) -> None:
        self.workbook.save(filename=self.file)
