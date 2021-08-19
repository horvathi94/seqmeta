from flask import render_template

class DisplayBase:

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
    def show(cls) -> "HTML":
        """Display empty message or show the list of registered items."""

        html = render_template("head.html");
        items = cls.get_list();

        if len(items) == 0:
            html+= render_template("empty_list.html",
                                   name_plural=cls.name_plural,
                                   link=cls.editor_link,
                                   description=cls.description);
        else:
            html+= cls.render_list(items);

        html+= render_template("footer.html");
        return html;
