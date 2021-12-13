from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import HostAnatomicalMaterials


@dataclass
class Editor(_MiscOptionBase):

    name = "Host anatomical materials"
    id = "host_anatomical_materials"
    link = "misc_bp.submit_host_anatomical_materials"
    description = "Host anatomical material or substance produced by the " \
        "body where the sample was obtained "\
        "<em>e.g., stool, mucus, saliva</em>"

    @classmethod
    def get_values(cls) -> list:
        return HostAnatomicalMaterials.fetch_list()


    @classmethod
    def save(cls, data: list) -> None:
        HostAnatomicalMaterials.save_by_procedure(data)

