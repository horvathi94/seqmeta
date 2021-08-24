from flask import render_template
from application.src.pages.page import Page
from application.src import library


class LibraryDescription(Page):

    styles=[{"filename":"library.css", "prefix":"misc"}];


    @classmethod
    def render_page(cls) -> "HTML":
        lib_strategies = library.LibraryStrategies.fetch_list();
        lib_sources = library.LibrarySources.fetch_list();
        lib_selections = library.LibrarySelections.fetch_list();
        return render_template("descriptions/library.html",
                               lib_strategies=lib_strategies,
                               lib_sources=lib_sources,
                               lib_selections=lib_selections);
