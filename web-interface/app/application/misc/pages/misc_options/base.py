from flask import render_template, redirect, url_for
from dataclasses import dataclass
from application.src.forms.form import Form


@dataclass
class _MiscOptionBase:

    name: str = ""
    id: str = ""
    link: str = ""
    description: str = ""
    redirect_after_save = "misc_bp.edit"


    @classmethod
    def get_values(cls) -> list:
        """Get values stored in the database."""
        pass


    @classmethod
    def render(cls):
        """Render basic options form for the object."""
        return render_template("misc/basic_options.html",
                               info=cls, vals=cls.get_values())


    @classmethod
    def save(cls, data: list) -> None:
        """Save to database"""
        pass


    @classmethod
    def parse_and_save(cls, form_data: list) -> "flask.redirect":
        """Parse the submitted form data and save to the database."""
        parsed = Form.parse_list(form_data, cls.id)[1:]
        cls.save(parsed)
        return redirect(url_for(cls.redirect_after_save))


