from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.sampling import HostBodyProducts



@dataclass
class Editor(_MiscOptionBase):

    name = "Host body products"
    id = "host_body_products"
    link = "misc_bp.submit_host_body_products"
    description = "Substance produced by the host" \
        "<em>e.g. stool mucus</em>, where the sample was obtained from."

    @classmethod
    def get_values(cls) -> list:
        return HostBodyProducts.fetch_list()


    @classmethod
    def save(cls, data: list) -> None:
        HostBodyProducts.save_by_procedure(data)

