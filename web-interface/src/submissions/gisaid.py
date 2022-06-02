import pathlib
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from .repo_sub import RepoSubmission
from .excel import ExcelFile


class GisaidSubmission(RepoSubmission):


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
        excel = ExcelFile(filename="gisaid", title="Submission")
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                excel.write_cell(i+1, j+1, cell)
        excel.write()


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


    def generate(self) -> any:
        self.write_excel()
        self.write_assemblies()
        return self.get_excel_data()
