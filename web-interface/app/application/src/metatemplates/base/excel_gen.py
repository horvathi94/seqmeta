from datetime import datetime
from openpyxl import Workbook
from .tempfile import TempFile


class ExcelGenerator(TempFile):

    @staticmethod
    def create_worksheet(title):
        wb = Workbook()
        ws = wb.active
        ws.title = title
        return wb, ws


    @classmethod
    def save_excel(cls, wb, filename):
        wb.save(filename=cls.get_tempfile())

