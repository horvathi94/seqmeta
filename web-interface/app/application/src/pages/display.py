from flask import render_template
from .page import Page

class DisplayBase(Page):

    """Base class for display pages"""

    name_plural = "";
    description = "";
    editor_link = "";


    @classmethod
    def get_list(cls) -> list:
        """Fetch the list of all registered items."""
        pass;


    @classmethod
    def render_list(cls, items: list) -> list:
        """Render HTML from list of items."""
        pass;


    @classmethod
    def show_empty(cls) -> "HTML":
        """Page to display if no items registered in the database."""
        return render_template("empty_list.html",
                                name_plural=cls.name_plural,
                                link=cls.editor_link,
                                description=cls.description);



    @classmethod
    def show_list(cls, items: list) -> "HTML":
        """Page to display of there are items registered in the database."""
        return cls.render_list(items);


    @classmethod
    def render_page(cls) -> "HTML":
        items = cls.get_list();

        html = "";
        if len(items) == 0:
            html+= cls.show_empty();
        else:
            html+= cls.show_list(items);

        return html;
