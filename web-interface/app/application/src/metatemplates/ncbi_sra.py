from .base.excel_gen import ExcelGenerator


class NcbiSra(ExcelGenerator):

    tempfilename = "last_generated_ncbi_sra.xls"
    extension = "xls"


    @classmethod
    def write_sra(cls, sra_data):
        pass
