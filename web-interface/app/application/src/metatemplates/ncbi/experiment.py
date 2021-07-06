from ..base.excel_gen import ExcelGenerator

class NcbiExperiment(ExcelGenerator):

    tempfilename = "last_generated_ncbi_experiments.xlsx";
    attachement_prefix = "ncbi";
    extension = "xlsx";

    @classmethod
    def populate(cls, ws, samples):
        for indx, sample in enumerate(samples):
            i = indx+2;
            ws[f"A{i}"] = sample["sample_name"];
            ws[f"B{i}"] = sample["library_id"];
            ws[f"C{i}"] = sample["title"];
            ws[f"D{i}"] = sample["library_strategy"];
            ws[f"E{i}"] = sample["library_source"];
            ws[f"F{i}"] = sample["library_selection"];
            ws[f"G{i}"] = sample["library_layout"];
            ws[f"H{i}"] = sample["platform"];
            ws[f"I{i}"] = sample["instrument_model"];
            ws[f"J{i}"] = sample["design_description"];
            ws[f"K{i}"] = sample["filetype"];
            ws[f"L{i}"] = sample["filename"];
            ws[f"M{i}"] = sample["filename2"];


    @classmethod
    def write(cls, samples):
        wb, ws = cls.create_worksheet("SRA-data");
        cls.populate(ws, samples);
        cls.save_excel(wb, cls.get_tempfile());
        wb.close();
