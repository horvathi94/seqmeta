import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, \
    jsonify, make_response, send_from_directory, send_file
from flask_caching import Cache

from src.samples import Samples
from src.institutions import Institutions
from src.author_groups import AuthorGroups
from src.custom_options import Hosts, SamplingStrategies, PassageDetails, \
    SequencingTechs, AssemblyMethods, PatientStatuses, SpecimenSources
from src.virusname import VirusnameGisaid
from src import ena
from src.locations import Countries, Continents

from src.base.excel_generator import ExcelGenerator
from src.fast_files import Fasta
from src import funcs


config = {
    "DEBUG" : True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 200,
    "JSON_SORT_KEYS": False,};

app = Flask(__name__)
app.config.from_mapping(config);


import pages_authors
import pages_author_groups
import pages_institutions
import pages_ena


@app.route("/")
def home():
    html = render_template("head.html");
    html+= render_template("index.html");
    html+= render_template("footer.html");
    return html;


@app.route("/favicon.ico")
def favicon():
    path = os.path.join(app.root_path, 'static', 'assets');
    return send_from_directory(path, 'favicon.ico',
                               mimetype='image/x-icon');


### Samples
###############################################################################

@app.route("/samples")
def samples_list():
    samples_list = Samples.fetch_list();
    html = render_template("head.html", styles=["prompt.css", "samples.css"]);
    if len(samples_list) == 0:
        html+= render_template("list_is_empty.html",
                               name_plural="samples",
                               link="samples_edit");
    else:
        html+= render_template("samples/list.html", samples=samples_list);

    scripts = ["sample_details.js"];
    html+= render_template("footer.html", scripts=scripts);
    return html;


@app.route("/sample/details")
def sample_details():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    sample_details = Samples.fetch_details(sample_id=sample_id);
    return jsonify(sample_details);


@app.route("/samples/edit")
def samples_edit():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    html = render_template("head.html");
    html+= render_template(
        "samples_edit.html",
        sample=Samples.fetch_entry_edit(id=sample_id, id_key="sample_id"),
        author_groups=AuthorGroups.fetch_list_labeled(
            replace_key="group_name",
            replace_id="group_id"),
        institutions=Institutions.fetch_list_labeled(),
        hosts=Hosts.fetch_list(),
        sampling_strategies=SamplingStrategies.fetch_list(),
        passage_details=PassageDetails.fetch_list(),
        assembly_methods=AssemblyMethods.fetch_list(),
        sequencing_technologies=SequencingTechs.fetch_list(),
        patient_statuses=PatientStatuses.fetch_list(),
        specimen_sources=SpecimenSources.fetch_list(),
        countries=Countries.fetch_list(),
        continents=Continents.fetch_list());
    html+= render_template("footer.html", scripts=["sample_edit.js"]);
    return html;


@app.route("/samples/submit", methods=["POST"])
def samples_submit():
    form_data = request.form.to_dict();
    Samples.save_entry(form_data);
    return redirect(url_for('samples_list'));


@app.route("/samples/fasta")
def samples_fasta():

    sample_id = 0;
    if "id" in request.args:
        sample_id = int(request.args["id"]);

    samples = Samples();
    sample = samples.fetch_entry(sample_id=sample_id);

    fasta = Fasta(sample["sample_name"]);
    sequences = fasta.read_fasta();

    if not fasta.has_fasta:
        resp_string = "fasta file was not found.";
    else:
        seq = sequences[0].seq;
        resp_string = str(seq);

    response = make_response(resp_string, 200);
    response.mimetype = "text/fasta";
    return response;


@app.route("/samples/generate", methods=["POST"])
def samples_generate():
    sub_types = request.form.getlist("submission_types");
    if len(sub_types) == 0:
        return "No files selected";

    selected = request.form.getlist("selected-samples");
    selected = [int(s) for s in selected];
    if len(selected) == 0:
        return "No files selected;"

    if "gisaid" in sub_types:
        filename = request.form["submission_filename_gisaid"];
        samples = Samples.fetch_entries("view_samples_gisaid",
                                        sample_ids=selected);

        if filename == "": filename = str(datetime.now()) + "_gisaid";
        ExcelGenerator.write_gisaid(samples);
        excel_file = os.path.join(ExcelGenerator.get_temp_filename("gisaid"));
        return send_file(excel_file, attachment_filename=filename+".xls")


    return "Finished";





### Other options
###############################################################################

@app.route("/set-options")
def set_options_list():
    hosts = Hosts.fetch_list();
    sampling_strategies = SamplingStrategies.fetch_list();
    passage_details = PassageDetails.fetch_list();
    sequencing_techs = SequencingTechs.fetch_list();
    assembly_methods = AssemblyMethods.fetch_list();

    html = render_template("head.html", styles=["options.css"]);
    html+= render_template("options/hosts.html",
                           hosts=hosts);
    html+= render_template("options/assembly_methods.html",
                           assembly_methods=assembly_methods);
    html+= render_template("options/passage_details.html",
                           passage_details=passage_details);
    html+= render_template("options/sequencing_technologies.html",
                           sequencing_technologies=sequencing_techs);
    html+= render_template("options/sampling_strategies.html",
                           samp_strats=sampling_strategies);
    html+= render_template("footer.html");
    return html;


@app.route("/set-options/hosts", methods=["POST"])
def hosts_submit():
    items_list = funcs.parse_form_list(request.form, "hosts");
    Hosts.save_by_procedure(items_list);
    return redirect(url_for("set_options_list"));


@app.route("/set-options/sampling-strategies", methods=["POST"])
def samp_strats_submit():
    items_list = funcs.parse_form_list(request.form, "samp_strats");
    SamplingStrategies.save_by_procedure(items_list);
    return redirect(url_for("set_options_list"));


@app.route("/set-options/passage-details", methods=["POST"])
def passage_details_submit():
    items_list = funcs.parse_form_list(request.form, "passage_details");
    PassageDetails.save_by_procedure(items_list);
    return redirect(url_for("set_options_list"));


@app.route("/set-options/assembly-methods", methods=["POST"])
def assembly_methods_submit():
    items_list = funcs.parse_form_list(request.form, "assembly_methods");
    AssemblyMethods.save_by_procedure(items_list);
    return redirect(url_for("set_options_list"));


@app.route("/set-options/sequencing-technologies", methods=["POST"])
def sequencing_technologies_submit():
    items_list = funcs.parse_form_list(request.form,
                                       "sequencing_technologies");
    Sequencingtehcnologies.save_by_procedure(items_list);
    return redirect(url_for("set_options_list"));




@app.route("/test")
def tests():

    samples = Samples.fetch_entries("view_samples_gisaid", sample_ids=[1]);
    sample = samples[0];

    available = VirusnameGisaid.available_db_keys();

    html = render_template("head.html", styles=["virusname.css"]);
    html+= render_template("virusname_edit.html",
                virusname_format=VirusnameGisaid.fetch_format_string(),
                available_db_keys=available);
    html+= render_template("footer.html");

    html+= VirusnameGisaid.create_name(sample);
    return html;


@app.route("/test/submit", methods=["POST"])
def tests_submit():

    virusname = request.form.to_dict()["virusname"];
    VirusnameGisaid.call_save_procedure(virusname);
    return jsonify(virusname);



if __name__ == "__main__":

    app.jinja_env.cache = {}
    app.run("0.0.0.0", debug=True);
