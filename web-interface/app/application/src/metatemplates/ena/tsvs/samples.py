import csv
from .base import _EnaTsvBase


class EnaTsvSamples(_EnaTsvBase):

    filename = "samples.tsv"

    taxonomy = {
        "tax_id": 2697049,
        "scientific_name": "Severe acute respiratory syndrome coronavirus 2",
        "common_name": "",
    }


    @classmethod
    def generate_header(cls, template_sample: dict) -> list:
        header = ["sample_alias", "tax_id", "scientific_name", "common_name"]
        ommit_keys = ["sample_id", "sample_name", "virus identifier"]
        for key in template_sample:
            if key not in ommit_keys:
                header.append(key)
        return header


    @classmethod
    def generate_units(cls, header: list) -> list:
        units = []
        for key in header:
            if key == "sample_alias": units.append("#units")
            elif key == "host age": units.append("years")
            elif key in ["geographic location (longitude)",
                         "geographic location (latitude)"]:
                units.append("DD")
            else: units.append("")
        return units


    @classmethod
    def generate_template(cls):
        return ["#template", cls.taxonomy["tax_id"],
                cls.taxonomy["scientific_name"],
                cls.taxonomy["common_name"],]


    @classmethod
    def generate_sample_data(cls, sample: dict) -> list:
        header = cls.generate_header(sample)
        sample["sample_alias"] = sample["sample_name"]
        sample["tax_id"] = cls.taxonomy["tax_id"]
        sample["scientific_name"] = cls.taxonomy["scientific_name"]
        sample["common_name"] = cls.taxonomy["common_name"]
        sample_data = [sample[key] for key in header]
        return sample_data


    @classmethod
    def write(cls, samples: dict) -> None:
        header = cls.generate_header(samples[0])
        units = cls.generate_units(header)
        template = cls.generate_template()
        with open(cls.get_tempfile(), "w") as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter="\t")
            tsv_writer.writerow(["#checklist_accession", "ERC000033"])
            tsv_writer.writerow(["#unique_name_prefix"])
            tsv_writer.writerow(header)
            tsv_writer.writerow(template)
            tsv_writer.writerow(units)
            for sample in samples:
                sample_row = cls.generate_sample_data(sample)
                tsv_writer.writerow(sample_row)


