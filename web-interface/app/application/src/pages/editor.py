from flask import render_template
from .page import Page


class EditorBase(Page):

    """Base class for simple editor pages."""

    styles = [];
    scripts = [];


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":
        """Return the content of the editor page."""
        pass;


    @classmethod
    def render_page(cls, item_id: int) -> "HTML":
        return cls.render_editor(item_id=item_id);

