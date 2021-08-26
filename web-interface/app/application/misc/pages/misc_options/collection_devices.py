from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import CollectionDevices


@dataclass
class Editor(_MiscOptionBase):

    name = "Collection devices";
    id = "collection_devices";
    link = "misc_bp.submit_collection_devices";
    description = "Instrument or container used to collect sample" \
        "<em>e.g. swab.</em>";

    @classmethod
    def get_values(cls) -> list:
        return CollectionDevices.fetch_list();


    @classmethod
    def save(cls, data: list) -> None:
        CollectionDevices.save_by_procedure(data);

