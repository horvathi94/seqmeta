from flask import render_template
from application.src.library import LibraryStrategies, \
    LibrarySelections, \
    LibrarySources


class LibraryDescription:

    styles=[{"filename":"library.css", "prefix":"misc"}];

    @classmethod
    def show(cls) -> "HTML":
        """Returns library descriptions page."""
        html = render_template("head.html", styles=cls.styles);
        html+= render_template("descriptions/library.html",
                               lib_strategies=LibraryStrategies.fetch_list(),
                               lib_sources=LibrarySources.fetch_list(),
                               lib_selections=LibrarySelections.fetch_list());
        html+= render_template("footer.html");
        return html;
