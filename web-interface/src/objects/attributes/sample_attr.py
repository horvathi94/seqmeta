from dataclasses import dataclass
from .file_types import SeqFileType
from .enums import Requirement


@dataclass
class SampleAttribute:

    general_name: str
    value: any = None
    ena_name: str = ""
    _ena_requirement: str = "exclude"
    ena_units: str = ""
    gisaid_name: str = ""
    _gisaid_requirement: str = "exclude"
    gisaid_header: str = ""
    seqfile_type: SeqFileType = None


    @property
    def gisaid_requirement(self) -> Requirement:
        return Requirement(self._gisaid_requirement)


    @gisaid_requirement.setter
    def gisaid_requirement(self, req: any) -> None:
        if isinstance(req, Requirement):
            req = req.value
        self._gisaid_requirement = req


    @property
    def ena_requirement(self) -> Requirement:
        return Requirement(self._ena_requirement)


    @ena_requirement.setter
    def ena_requirement(self, req: any) -> None:
        if isinstance(req, Requirement):
            req = req.value
        self._ena_requirement = req

