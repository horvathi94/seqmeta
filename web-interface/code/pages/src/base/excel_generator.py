import os
from datetime import datetime
from openpyxl import Workbook


class ExcelGenerator:

    save_dir = "/app/temp";
    temp_filenames = {
        "gisaid": "last_generated_gisaid.xls",
    }

    def __init__(self):
        pass;


    @staticmethod
    def create_worksheet(title):
        wb = Workbook();
        ws = wb.active;
        ws.title = title;
        return wb, ws;


    @classmethod
    def save_excel(cls, wb, filename):
        excel_file = os.path.join(cls.save_dir, filename);
        wb.save(filename=excel_file);


    @classmethod
    def get_temp_filename(cls):
        return os.path.join(cls.save_dir, cls.temp_filename);

