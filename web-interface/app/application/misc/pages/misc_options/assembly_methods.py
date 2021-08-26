from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sequencing import AssemblyMethods


@dataclass
class Editor(_MiscOptionBase):

    name = "Assembly methods";
    id = "assembly_methods";
    link = "misc_bp.submit_assembly_methods";
    description = "Programs with which the assembly " \
        "of the sequences was performed.";

    @classmethod
    def get_values(cls) -> list:
        return AssemblyMethods.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        AssemblyMethods.save_by_procedure(data);
