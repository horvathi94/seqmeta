import os
from datetime import datetime
from openpyxl import Workbook
from .samples import Samples

SAVE_DIR = "/app/temp";


def excel_test(samples):

    wb = Workbook();
    ws = wb.active;
    ws.title = "Excel test";
    filename = os.path.join("/app/temp", "test01.xlsx")

    for indx, sample in enumerate(samples):
        i = indx+1;
        ws["A{:d}".format(i)] = sample["sample_name"];
        ws["B{:d}".format(i)] = sample["collection_date"];

    wb.save(filename=filename);


def gisaid_sample_sheet(samples):

    wb = Workbook();
    ws = wb.active;
    ws.title = "Submissions";
    today = datetime.today().strftime("%Y%m%d");
    filename = "{:s}_gisaid_submission_data.xls".format(today);
    excel_file = os.path.join(SAVE_DIR, filename);


    for indx, sample in enumerate(samples):

        i = indx+3;

        ws["A{:d}".format(i)] = "Submitter"          # Submitter
        ws["B{:d}".format(i)] = "filename";          # Filename
        ws["C{:d}".format(i)] = "virus-name";        # Virus name
        ws["D{:d}".format(i)] = "betacoronavirus"    # Leave as default
        ws["E{:d}".format(i)] = "passage details"    # Passage details

        collection_date = sample["collection_date"];
        ws["F{:d}".format(i)] = str(collection_date);
        ws["G{:d}".format(i)] = "location"           # Location
        ws["H{:d}".format(i)] = "";                 # Additional location info
        ws["I{:d}".format(i)] = "Host";             # Host
        ws["J{:d}".format(i)] = "";                 # Additional host info
        ws["K{:d}".format(i)] = "Sampling strategy";# Sampling strategy
        ws["L{:d}".format(i)] = sample["patient_gender"];     # Patient gender
        ws["M{:d}".format(i)] = sample["patient_age"];        # Patient age
        ws["N{:d}".format(i)] = "Status";           # Patient status
        ws["O{:d}".format(i)] = "Specimen source";  # Specimen source
        ws["P{:d}".format(i)] = "";                 # Outbreak
        ws["Q{:d}".format(i)] = "";                 # Last vaccinated
        ws["R{:d}".format(i)] = "";                 # Treatment
        ws["S{:d}".format(i)] = "Seq techno";       # Sequencing technology
        ws["T{:d}".format(i)] = "Assemby method";
        ws["U{:d}".format(i)] = "Coverage";
        ws["V{:d}".format(i)] = sample["originating_lab_name"];
        ws["W{:d}".format(i)] = "Addr";
        ws["X{:d}".format(i)] = sample["sample_name"];
        ws["Y{:d}".format(i)] = sample["submitting_lab_name"];
        ws["Z{:d}".format(i)] = "Addr";
        ws["AA{:d}".format(i)] = sample["sample_name"];
        ws["AB{:d}".format(i)] = sample["authors"];

    wb.save(filename=excel_file);
