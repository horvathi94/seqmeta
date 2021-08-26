from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import SpecimenSources


@dataclass
class Editor(_MiscOptionBase):

    name = "Specimen sources";
    id = "specimen_sources";
    link = "misc_bp.submit_specimen_sources";
    description = "Source of the specimen.";

    @classmethod
    def get_values(cls) -> list:
        return SpecimenSources.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        SpecimenSources.save_by_procedure(data);


