import pathlib
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from .repo_sub import RepoSubmission
from .excel import ExcelFile
from zipfile import ZipFile


class GisaidSubmission(RepoSubmission):

    zipname = "gisaid_submission.zip"
    excelname = "gisaid"


    def __init__(self, template_name: str, sample_names: str):
        super().__init__(template_name, sample_names)
        self.excel = ExcelFile(filename=self.excelname, title="Submission")


    @property
    def assemblies_filename(self) -> str:
        fname = self.samples[0].get_value("gisaid_filename")
        if fname is None:
            raise ValueError
        return fname.split(".")[0] + ".fa"


    @property
    def assemblies_file(self) -> pathlib.Path:
        return pathlib.Path(self.path, self.assemblies_filename)


    def get_excel_data(self) -> list:
        data = []
        for i, sample in enumerate(self.samples):
            atts = sample.list_gisaid_attributes().copy()
            if i == 0:
                data.append([a.gisaid_header for a in atts])
                data.append([a.gisaid_name for a in atts])

            row = []
            for a in atts:
                if a.general_name == "gisaid_filename":
                    val = self.assemblies_filename
                else:
                    val = a.value
                row.append(val)
            data.append(row)
        return data


    def write_excel(self) -> None:
        data = self.get_excel_data()
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                self.excel.write_cell(i+1, j+1, cell)
        self.excel.write()


    def write_assemblies(self) -> None:
        sequences = []
        for sample in self.samples:
            seqfile = sample.get_value("assembly_file")[0]
            rec = SeqIO.read(seqfile.file, seqfile.seqio_type)
            rec.id = sample.get_value("virus_name")
            rec.name = sample.get_value("virus_name")
            rec.description = ""
            sequences.append(rec)
        SeqIO.write(sequences, self.assemblies_file, "fasta")


    def write_zipfile(self) -> None:
        with ZipFile(self.zipfile, "w") as z:
            z.write(self.excel.file, "submission.xlsx")
            z.write(self.assemblies_file, self.assemblies_filename)


    def generate(self) -> pathlib.Path:
        self.write_excel()
        self.write_assemblies()
        self.write_zipfile()
        return self.zipfile


