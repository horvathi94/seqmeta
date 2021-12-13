from .base import _SaveBase


class EditMultiple(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form",
                      files: "flask.request.files") -> list:
        save_data = cls.parse_list(raw, files)
        return save_data




class AddMultiple(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form",
                      files: "flask.request.files") -> list:
        save_data = cls.parse_list(raw, files)
        for item in save_data:
            item["sample"]["sample_id"] = 0
        return save_data

