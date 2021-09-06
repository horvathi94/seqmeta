from flask import jsonify
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from application.src.misc.health import ReceivedTreatment, PriorInfection


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


    @classmethod
    def fetch_data(cls, sample_id: int) -> dict:
        """Fetch information from the database."""
        sample = Samples.fetch(cls.view_name, sample_id=sample_id);
        if "geo-loc-longitude" in sample:
            sample["geo-loc-longitude"] = float(sample["geo-loc-longitude"]);
        if "geo-loc-latitude" in sample:
            sample["geo-loc-latitude"] = float(sample["geo-loc-latitude"]);

        key = "prior-sars-cov-2-antiviral-treat";
        if key in sample:
            treat = ReceivedTreatment.get_item_from_dbvalue(sample[key]);
            sample[key] = treat.value;

        key = "prior-sars-cov-2-infection";
        if key in sample:
            infect = PriorInfection.get_item_from_value(sample[key]);
            sample[key] = infect.dbsave;

        return sample;



class DetailsView(SampleViewBase):

    @classmethod
    def fetch_data(cls, sample_id: int) -> dict:
        sample = Samples.fetch_details(sample_id=sample_id);
        seqbunch = SeqFilesBunch(sample_id);
        sample["seqbunch"] = seqbunch.get_details_display();
        return sample;


