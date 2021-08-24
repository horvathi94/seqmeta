from flask import render_template

class Page:

    """Base class for pages."""

    styles = [];
    scripts = [];

    @classmethod
    def render_head(cls):
        return render_template("head.html", styles=cls.styles);


    @classmethod
    def render_footer(cls):
        return render_template("footer.html", scripts=cls.scripts);


    @classmethod
    def render_page(cls, *args, **kwargs) -> "HTML":
        pass;


    @classmethod
    def render(cls, *args, **kwargs):
        html = cls.render_head();
        html+= cls.render_page(*args, **kwargs);
        html+= cls.render_footer();
        return html;
