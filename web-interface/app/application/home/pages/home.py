from flask import render_template
from application.src.pages.page import Page


class Home(Page):

    @classmethod
    def render_page(cls) -> "HTML":
        return render_template("index.html")
