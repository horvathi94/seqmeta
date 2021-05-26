import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, \
    jsonify, make_response, send_from_directory, send_file
from flask_caching import Cache


from pages.src import funcs


config = {
    "DEBUG" : True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 200,
    "JSON_SORT_KEYS": False,};


app = Flask(__name__)
app.config.from_mapping(config);


from pages import samples
from pages import authors
from pages import author_groups
from pages import institutions
from pages import ena


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
