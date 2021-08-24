from ..base.excel_gen import ExcelGenerator
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid

class GisaidExcel(ExcelGenerator):

    tempfilename = "last_generated_gisaid.xlsx";
    attachement_prefix = "gisaid";
    extension = "xlsx";

    @classmethod
    def populate_gisaid(cls, ws, samples):
        for indx, sample in enumerate(samples):
            i = indx+3;
            ws["A{:d}".format(i)] = "Submitter"          # Submitter
            ws["B{:d}".format(i)] = sample["seqfilename"];
            ws["C{:d}".format(i)] = sample["gisaid_virusname"];
            ws["D{:d}".format(i)] = "betacoronavirus"    # Leave as default
            ws["E{:d}".format(i)] = sample["passage_details"]
            ws["F{:d}".format(i)] = str(sample["collection_date"]);
            ws["G{:d}".format(i)] = sample["location"];
            ws["H{:d}".format(i)] = sample["additional_location_info"];
            ws["I{:d}".format(i)] = sample["host"];
            ws["J{:d}".format(i)] = sample["additional_host_info"];
            ws["K{:d}".format(i)] = sample["sampling_strategy"];
            ws["L{:d}".format(i)] = sample["patient_gender_gisaid"]
            ws["M{:d}".format(i)] = sample["patient_age"];
            ws["N{:d}".format(i)] = sample["patient_status"];
            ws["O{:d}".format(i)] = sample["specimen_source"];
            ws["P{:d}".format(i)] = sample["outbreak"];
            ws["Q{:d}".format(i)] = sample["last_vaccinated"];
            ws["R{:d}".format(i)] = sample["treatment"];
            ws["S{:d}".format(i)] = sample["sequencing_technology"];
            ws["T{:d}".format(i)] = sample["assembly_method"];
            ws["U{:d}".format(i)] = sample["coverage"];
            ws["V{:d}".format(i)] = sample["originating_lab_name"];
            ws["W{:d}".format(i)] = sample["originating_lab_address"];
            ws["X{:d}".format(i)] = sample["originating_lab_sample_name"];
            ws["Y{:d}".format(i)] = sample["submitting_lab_name"];
            ws["Z{:d}".format(i)] = sample["submitting_lab_address"];
            ws["AA{:d}".format(i)] = sample["submitting_lab_sample_name"];
            ws["AB{:d}".format(i)] = sample["authors_list"];


    @classmethod
    def write_gisaid(cls, samples):
        wb, ws = cls.create_worksheet("Submissions");
        cls.populate_gisaid(ws, samples);
        cls.save_excel(wb, cls.get_tempfile());
        wb.close();

