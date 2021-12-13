from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import PurposesOfSampling


@dataclass
class Editor(_MiscOptionBase):

    name = "Purpose of sampling"
    id = "purpose_of_sampling"
    link = "misc_bp.submit_purpose_of_sampling"
    description = "The reason the sample was collected " \
        "<em>e.g. diagnostic testing</em>"

    @classmethod
    def get_values(cls) -> list:
        return PurposesOfSampling.fetch_list()


    @classmethod
    def save(cls, data: list) -> None:
        PurposesOfSampling.save_by_procedure(data)

