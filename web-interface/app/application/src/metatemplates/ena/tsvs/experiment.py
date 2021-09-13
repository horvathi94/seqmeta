from .base import _EnaTsvBase
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from application.src.seqfiles.types import SeqFileTypes


class EnaTsvExperiment(_EnaTsvBase):

    filename = "experiments.tsv";


    @classmethod
    def generate_header(cls, is_paired: bool) -> list:
        header = [
            "sample_alias",
            "instrument_model",
            "library_name",
            "library_source",
            "library_selection",
            "library_strategy",
            "design_description",
            "library_construction_protocol",
            "insert_size"];
        if is_paired:
            header += [
                "forward_file_name",
                "forward_file_md5",
                "reverse_file_name",
                "reverse_file_md5"];
        return header;


    @classmethod
    def generate_sample_data(cls, sample: dict) -> list:
        header = cls.generate_header(sample["is_paired"]);
        if sample["is_paired"]:
            seqbunch = SeqFilesBunch(sample["sample_id"]);
            sample["forward_file_name"] = \
                seqbunch.get_read_name(SeqFileTypes.FWREAD);
            sample["reverse_file_name"] = \
                seqbunch.get_read_name(SeqFileTypes.RVREAD);
        sample_data = [sample[key] for key in header];
        return sample_data;


    @classmethod
    def write(cls, samples: dict) -> None:
        cls.write_header(samples[0]["is_paired"]);
        cls.write_sample_data(samples);
