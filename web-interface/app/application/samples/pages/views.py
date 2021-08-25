from flask import jsonify
from application.src.samples.samples import Samples


class SampleViewBase:

    view_name = "";

    @classmethod
    def fetch_data(cls, sample_id: int) -> dict:
        """Fetch information from the database."""
        return Samples.fetch(cls.view_name, sample_id=sample_id);


    @classmethod
    def get_json(cls, sample_id: int) -> "json":
        """Return JSON format of requested data."""
        return jsonify(cls.fetch_data(sample_id));



class BasicView(SampleViewBase):

    view_name = "view_samples_base";



class ImportView(SampleViewBase):

    view_name = "view_samples_import";



class DetailsView(SampleViewBase):

    @classmethod
    def fetch_data(cls, sample_id: int) -> dict:
        sample = Samples.fetch_details(sample_id=sample_id);

        return sample;


