import os
from openpyxl import Workbook
from .samples import Samples


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


