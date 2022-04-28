from dataclasses import dataclass
from .enums import Requirement


@dataclass
class SampleAttribute:

    general_name: str
    ena_name: str = None
    ena_requirement: Requirement = None
    ena_units: str = None
    gisaid_name: str = None
    gisaid_requirement: Requirement = None
    gisaid_header: str = None
    value: any = None


    def asjson(self) -> dict:
        return {
            "general_name": self.general_name,
            "ena_name": self.ena_name,
            "ena_requirement": self.ena_requirement.value,
            "ena_units": self.ena_units,
            "gisaid_name": self.gisaid_name,
            "gisaid_requirement": self.gisaid_requirement.value,
            "gisaid_header": self.gisaid_header,
            "value": self.value,
        }


    def ena_include(self) -> bool:
        if self.ena_requirement is Requirement.EXCLUDE: return False
        return True


    def gisaid_include(self) -> bool:
        if self.gisaid_requirement is Requirement.EXCLUDE: return False
        return True
