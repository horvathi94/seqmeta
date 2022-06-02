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


    def __eq__(self, other):
        if self.__class__ != other.__class__:
            raise ValueError
        if self.general_name == other.general_name: return True
        return False


    def is_file(self) -> bool:
        if self.seqfile_type is not None: return True
        return False


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


    def gisaid_include(self) -> bool:
        if self.gisaid_requirement is Requirement.EXCLUDE: return False
        return True


    def ena_include(self) -> bool:
        if self.ena_requirement is Requirement.EXCLUDE: return False
        return True


    def has_value(self) -> bool:
        if self.value is None: return False
        if len(self.value) == 0: return False
        return True


    def value_as_json(self) -> any:
        if not self.is_file():
            return self.value
        return [sf.as_json() for sf in self.value]


    def as_json(self) -> dict:
        return {
            "general_name": self.general_name,
            "value": self.value_as_json(),
            "ena_name": self.ena_name,
            "ena_requirement": self.ena_requirement.value,
            "ena_units": self.ena_units,
            "gisaid_name": self.gisaid_name,
            "gisaid_requirement": self.gisaid_requirement.value,
            "gisaid_header": self.gisaid_header,
            "seqfile_type": self.seqfile_type.value \
                if self.seqfile_type is not None else None,
        }
