from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify
from application.src.samples.extensions.library import Library
from application.src.samples.samples import Samples
from application.src.forms.form import Form
from .save import save
from .editor import Editor, MultiEditor



samples_bp = Blueprint("samples_bp", __name__,
                       template_folder="templates",
                       static_folder="static",
                       static_url_path="/static/samples/");


from .pages.display import DisplayPage
from .pages import views
from .pages import generators


@samples_bp.route("/samples/view")
def show():
    return DisplayPage.show();


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    save_data = {};
    save_data["sample"] = Form.parse_simple(request.form, "sample");
    save_data["location"] = Form.parse_simple(request.form, "location");
    save_data["collection"] = Form.parse_simple(request.form, "collection");
    save_data["library"] = Form.parse_simple(request.form, "library");
    save_data["host"] = Form.parse_simple(request.form, "host");
    save_data["sampling"] = Form.parse_simple(request.form, "sampling");
    save_data["health"] = Form.parse_simple(request.form, "health");
    save_data["sequencing"] = Form.parse_simple(request.form, "sequencing");
    save_data["treatment"] = Form.parse_simple(request.form, "treatment");
    save_data["seqfiles"] = parse_files_multiple(request)[0];
    sample_ids = save([save_data]);
    sample_id = sample_ids[0];
    return redirect(url_for('samples_bp.show'));



def parse_files_multiple(request):
    seqfile_types = Form.parse_list(request.form, "seqfile");
    seqfiles = Form.parse_list(request.files, "seqfile");

    fdata = [];
    FTYPES = ["assembly_file", "fwread_file", "rvread_file",
              "contigs_file", "scaffolds_file"];
    for f, ftype in zip(seqfiles, seqfile_types):
        d = {"id": ftype["id"]};
        for handle in FTYPES:
            d[handle] = {"type": ftype[handle],
                        "filename": f[handle].filename,
                        "filedata": f[handle]};
        fdata.append(d);
    return fdata;


@samples_bp.route("/samples/submit-multiple", methods=["POST"])
def submit_multiple():
    sample_data = Form.parse_list(request.form, "sample")[1:];
    collection = Form.parse_list(request.form, "collection")[1:];
    location = Form.parse_list(request.form, "location")[1:];
    host = Form.parse_list(request.form, "host")[1:];
    treatment = Form.parse_list(request.form, "treatment")[1:];
    health = Form.parse_list(request.form, "health")[1:];
    sequencing = Form.parse_list(request.form, "sequencing")[1:];
    sampling = Form.parse_list(request.form, "sampling")[1:];
    library = Form.parse_list(request.form, "library")[1:];
    fs = parse_files_multiple(request)[1:];

    samples = [];
    for i, sd in enumerate(sample_data):
        save_data = {};
        save_data["sample"] = sd;
        save_data["sample"]["sample_id"] = 0;
        save_data["location"] = location[i];
        save_data["collection"] = collection[i];
        save_data["host"] = host[i];
        save_data["health"] = health[i];
        save_data["sequencing"] = sequencing[i];
        save_data["sampling"] = sampling[i];
        save_data["library"] = library[i];
        save_data["treatment"] = treatment[i];
        save_data["seqfiles"] = fs[i];
        samples.append(save_data);
    save(samples);
    return redirect(url_for('samples_bp.show'));


@samples_bp.route("/samples/submit-edit-multiple", methods=["POST"])
def submit_edit_multiple():
    sample_data = Form.parse_list(request.form, "sample")[1:];
    collection = Form.parse_list(request.form, "collection")[1:];
    location = Form.parse_list(request.form, "location")[1:];
    host = Form.parse_list(request.form, "host")[1:];
    treatment = Form.parse_list(request.form, "treatment")[1:];
    health = Form.parse_list(request.form, "health")[1:];
    sequencing = Form.parse_list(request.form, "sequencing")[1:];
    sampling = Form.parse_list(request.form, "sampling")[1:];
    library = Form.parse_list(request.form, "library")[1:];
    fs = parse_files_multiple(request)[1:];

    samples = [];
    for i, sd in enumerate(sample_data):
        save_data = {};
        save_data["sample"] = sd;
        save_data["sample"]["sample_id"] = int(sd["id"]);
        save_data["location"] = location[i];
        save_data["collection"] = collection[i];
        save_data["host"] = host[i];
        save_data["health"] = health[i];
        save_data["sequencing"] = sequencing[i];
        save_data["sampling"] = sampling[i];
        save_data["library"] = library[i];
        save_data["treatment"] = treatment[i];
        save_data["seqfiles"] = fs[i];
        samples.append(save_data);
    save(samples);
    return redirect(url_for('samples_bp.show'));




@samples_bp.route("/samples/view/base")
def samples_view_base():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    return views.BasicView.get_json(sample_id);


@samples_bp.route("/samples/details")
def sample_details():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    return views.DetailsView.get_json(sample_id);


@samples_bp.route("/samples/view/import")
def samples_view_import():
    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    return views.ImportView.get_json(sample_id);





@samples_bp.route("/samples/generate/gisaid", methods=["POST"])
def gen_gisaid_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return generators.Gisaid.render(selected);


@samples_bp.route("/samples/generate/ncbi", methods=["POST"])
def gen_ncbi_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return generators.Ncbi.render(selected);


@samples_bp.route("/samples/generate/ena", methods=["POST"])
def gen_ena_meta():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return generators.Ena.render(selected);


@samples_bp.route("/samples/generate/concat-assemblies", methods=["POST"])
def gen_concat_assemblies():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return generators.ConcatConsensus.render(selected);


@samples_bp.route("/samples/registered/sample-names", methods=["GET"])
def reg_sample_names():
    sample_names = [s["sample_name"] for s in Samples.fetch_list()];
    return jsonify(sample_names);


@samples_bp.route("/samples/registered/library-names", methods=["GET"])
def reg_library_names():
    lib_ids = [lid["library_id"] for lid in Library.select_library_ids()];
    return jsonify(lib_ids);




@samples_bp.route("/samples/edit")
def edit():

    sample_id = int(request.args["id"]) if "id" in request.args else 0;
    editor = Editor(sample_id);

    styles = [{"filename": "edit.css", "prefix": "samples"},
              {"filename": "markers.css"}];
    scripts = [{"filename": "validate-sample-name.js", "prefix": "samples"},
               {"filename": "edit-sample.js", "prefix": "samples"}];
    html = render_template("head.html", styles=styles);
    html+= editor.show();
    html+= render_template("footer.html", scripts=scripts);
    return html;




@samples_bp.route("/samples/add-multiple", methods=["GET"])
def add_multiple():

    styles = [{"filename": "add-multiple.css", "prefix": "samples"},
              {"filename": "markers.css"},
              {"filename": "tooltips.css"},
              {"filename": "info.css"}];
    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"},
               {"filename": "import-data.js", "prefix": "samples"}];

    html = "";
    html+= render_template("head.html", styles=styles);

    editor = MultiEditor();
    html+= editor.show(tp="add");

    html+= render_template("footer.html", scripts=scripts);
    return html;



@samples_bp.route("/samples/edit-multiple", methods=["POST"])
def edit_multiple():

    styles = [{"filename": "add-multiple.css", "prefix": "samples"},
              {"filename": "markers.css"},
              {"filename": "tooltips.css"},
              {"filename": "info.css"}];
    scripts = [{"filename": "edit-multiple.js", "prefix": "samples"},
               {"filename": "validate-samples.js", "prefix": "samples"}];


    selected = [int(i) for i in request.form.getlist("selected-samples")];
    if len(selected) == 0: return "Nothing selected";

    html = "";
    html+= render_template("head.html", styles=styles);

    editor = MultiEditor(sample_ids=selected);
    html+= editor.show(tp="edit");

    html+= render_template("footer.html", scripts=scripts);
    return html;



@samples_bp.route("/samples/validate-delete", methods=["POST"])
def validate_delete():

    styles = [{"filename":"smbasicform.css"}];

    selected = [int(i) for i in request.form.getlist("selected-samples")];
    samples = Samples.fetch_entries("view_samples_details",
                                    sample_ids=selected);

    html = "";
    html+= render_template("head.html", styles=styles);
    html+= render_template("samples/validate_delete.html",
                           samples=samples);
    html+= render_template("footer.html");
    return html;


@samples_bp.route("/samples/delete", methods=["POST"])
def delete_samples():

    selected = [int(i) for i in request.form.getlist("samples-to-delete")];
    for sample_id in selected:
        Samples.delete(sample_id);

    return redirect(url_for('samples_bp.show'));

