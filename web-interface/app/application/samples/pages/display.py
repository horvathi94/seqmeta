from flask import render_template
from application.src.pages.display import DisplayBase
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfiles import SeqFilesBunch


class DisplayPage(DisplayBase):

    name_plural = "samples";
    description = "Here you can register the samples and sequencing data."
    editor_link = "samples_bp.edit";
    styles = [{"filename":"prompt.css"},
              {"filename": "samples.css", "prefix":"samples"}];
    scripts = [{"filename": "details.js", "prefix":"samples"},
               {"filename": "delete-sample.js", "prefix": "samples"},
               {"filename": "submitguide.js", "prefix": "samples"}];


    @classmethod
    def get_list(cls) -> list:
        samples = Samples.fetch_list();
        for sample in samples:
            seqbunch = SeqFilesBunch(sample["sample_id"]);
            sample["seqfiles"] = seqbunch.todict();
        return samples;


    @classmethod
    def render_list(cls, items: list) -> "HTML":
        return render_template("samples/list.html", samples=items);


    @classmethod
    def show_empty(cls) -> "HTML":
        html = render_template("empty_list.html",
                               name_plural=cls.name_plural,
                               link=cls.editor_link);
        html+= render_template("samples/add_multiple_button.html");
        return html;


