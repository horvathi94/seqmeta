from .base import _SaveBase
from application.src.forms.form import Form


class SaveSingle(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form",
                      files: "flask.request.files") -> list:
        save_data = {};
        save_data["sample"] = Form.parse_simple(raw, "sample");
        save_data["location"] = Form.parse_simple(raw, "location");
        save_data["collection"] = Form.parse_simple(raw, "collection");
        save_data["library"] = Form.parse_simple(raw, "library");
        save_data["host"] = Form.parse_simple(raw, "host");
        save_data["sampling"] = Form.parse_simple(raw, "sampling");
        save_data["health"] = Form.parse_simple(raw, "health");
        save_data["sequencing"] = Form.parse_simple(raw, "sequencing");
        save_data["treatment"] = Form.parse_simple(raw, "treatment");
        save_data["seqfiles"] = cls.parse_files(raw, files)[0];
        return [save_data];
