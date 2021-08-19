from flask import render_template


class EditorBase:

    """Base class for simple editor pages."""

    styles = [];
    scripts = [];


    @classmethod
    def render_editor(cls, item_id: int) -> "HTML":
        """Return the content of the editor page."""
        pass;


    @classmethod
    def show(cls, item_id: int=0) -> "HTML":
        """Returns HTML of basic editor."""

        html = render_template("head.html", styles=cls.styles);
        html+= cls.render_editor(item_id);
        html+= render_template("footer.html", scripts=cls.scripts);
        return html;
