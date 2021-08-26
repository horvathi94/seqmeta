from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import PurposesOfSequencing


@dataclass
class Editor(_MiscOptionBase):

    name = "Purpose of sequencing";
    id = "purpose_of_sequencing";
    link = "misc_bp.submit_purpose_of_sequencing";
    description = "The reason the sample was sequenced " \
        "<em>e.g. baseline surveillance (random sampling)</em>";

    @classmethod
    def get_values(cls) -> list:
        return PurposesOfSequencing.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        PurposesOfSequencing.save_by_procedure(data);

