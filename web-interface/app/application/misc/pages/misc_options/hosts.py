from flask import render_template
from dataclasses import dataclass
from .base import _MiscOptionBase
from application.src.misc.host import Hosts



@dataclass
class Editor(_MiscOptionBase):

    id: str = "hosts";

    @classmethod
    def get_values(cls) -> list:
        return Hosts.fetch_list();


    @classmethod
    def render(cls):
        """Render basic options form for the object."""
        return render_template("misc/hosts.html", hosts=cls.get_values());


    @classmethod
    def save(cls, data: list) -> None:
        Hosts.save_by_procedure(data);
