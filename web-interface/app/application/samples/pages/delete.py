from flask import render_template
from application.src.pages.page import Page
from application.src.samples.samples import Samples


class Validate(Page):

    styles = [{"filename":"smbasicform.css"}];

    @classmethod
    def render_page(cls, sample_ids: list):
        samples = Samples.fetch_entries("view_samples_details",
                                        sample_ids=sample_ids);
        return render_template("samples/validate_delete.html",
                               samples=samples);


