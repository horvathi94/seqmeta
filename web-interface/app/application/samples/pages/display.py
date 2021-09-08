from flask import render_template
from application.src.pages.display import DisplayBase
from application.src.samples.samples import Samples
from application.src.seqfiles.seqfile_bunch_new import SeqFilesBunch
from . import filters as sampfilters


import sys

class DisplayPage(DisplayBase):

    name_plural = "samples";
    description = "Here you can register the samples and sequencing data."
    editor_link = "samples_bp.edit";
    styles = [{"filename":"prompt.css"},
              {"filename": "samples.css", "prefix":"samples"}];
    scripts = [{"filename": "details.js", "prefix":"samples"},
               {"filename": "delete-sample.js", "prefix": "samples"},
               {"filename": "submitguide.js", "prefix": "samples"},
               {"filename": "toggle-select-all.js", "prefix": "samples"}];



    @classmethod
    def filter_submitted_to_gisaid(cls, samples: list,
                                   filt: sampfilters.GisaidSubmission) -> list:

        if filt == sampfilters.GisaidSubmission.NONE:
            return samples;

        filtered = [];
        for sample in samples:
            if filt == sampfilters.GisaidSubmission.SUBMITTED:
                if sample["gisaid_accession"] != "":
                    filtered.append(sample);
            elif filt == sampfilters.GisaidSubmission.NOT_SUBMITTED:
                if sample["gisaid_accession"] == "":
                    filtered.append(sample);

        return filtered;


    @classmethod
    def filter_consensus_files(cls, samples: list,
                               filt: sampfilters.HasConsensus) -> list:

        if filt == sampfilters.HasConsensus.NONE:
            return samples;

        filtered = [];
        for sample in samples:
            if filt == sampfilters.HasConsensus.HAS_FILE:
                if sample["seqfiles"]["consensus"]["exists"]:
                    filtered.append(sample);
            elif filt == sampfilters.HasConsensus.NO_FILE:
                if not sample["seqfiles"]["consensus"]["exists"]:
                    filtered.append(sample);
        return filtered;


    @classmethod
    def filter(cls, samples: list, filters: dict={}) -> list:
        """Filters sample data fetched from the database"""
        if len(filters) == 0: return samples;

        print(f"Filters: {filters}", file=sys.stderr);

        for filter_key in filters:
            if filter_key == "filter-gisaid":
                filt = sampfilters.GisaidSubmission(int(filters[filter_key]));
                samples = cls.filter_submitted_to_gisaid(samples, filt);
            if filter_key == "filter-consensus":
                filt = sampfilters.HasConsensus(int(filters[filter_key]));
                samples = cls.filter_consensus_files(samples, filt);
        return samples;


    @classmethod
    def get_list(cls, filters: list=[]) -> list:
        samples = Samples.fetch_list();
        for sample in samples:
            seqbunch = SeqFilesBunch(sample["sample_id"]);
            sample["seqfiles"] = seqbunch.get_list_display();
        samples = cls.filter(samples, filters=filters);
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


    @classmethod
    def render_page(cls, filters: "flask.request.form"={}) -> "HTML":
        if len(filters) != 0:
            filters = filters.to_dict();
        items = cls.get_list(filters=filters);

        html = "";
        if len(items) == 0:
            html+= cls.show_empty();
        else:
            html+= cls.show_list(items);

        return html;
