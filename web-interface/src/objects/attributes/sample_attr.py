from dataclasses import dataclass


@dataclass
class SampleAttribute:

    general_name: str
    value: any = None
    ena_name: str = ""
    ena_requirement: str = "exclude"
    ena_units: str = ""
    gisaid_name: str = ""
    gisaid_requirement: str = "exclude"
    gisaid_header: str = ""
