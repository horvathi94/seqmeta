from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import SamplingStrategies


@dataclass
class Editor(_MiscOptionBase):

    name = "Sampling strategies";
    id = "sampling_strategies";
    link = "misc_bp.submit_sampling_strategies";
    description = "The sampling strategy used to select the sample.";

    @classmethod
    def get_values(cls) -> list:
        return SamplingStrategies.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        SamplingStrategies.save_by_procedure(data);

