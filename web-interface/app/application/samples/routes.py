from flask import Blueprint, request, redirect, url_for, jsonify
from application.src.samples.extensions.library import Library
from application.src.samples.samples import Samples
from .pages.editor import Editor
from .pages.multi_editor import MultiEditor, MultiEditorAdd
from .pages.display import DisplayPage
from .pages import views
from .pages import generators
from .pages import save
from .pages import delete



samples_bp = Blueprint("samples_bp", __name__,
                       template_folder="templates",
                       static_folder="static",
                       static_url_path="/static/samples/");




@samples_bp.route("/samples/view")
def show():
    return DisplayPage.render();


@samples_bp.route("/samples/submit", methods=["POST"])
def submit():
    return save.SaveSingle.save(request.form, request.files);


@samples_bp.route("/samples/submit-multiple", methods=["POST"])
def submit_multiple():
    return save.AddMultiple.save(request.form, request.files);


@samples_bp.route("/samples/submit-edit-multiple", methods=["POST"])
def submit_edit_multiple():
    return save.EditMultiple.save(request.form, request.files);



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


@samples_bp.route("/samples/generate", methods=["POST"])
def generate():
    return generators.GeneratorBase.render([]);


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
    return Editor.render(sample_id);


@samples_bp.route("/samples/add-multiple", methods=["GET"])
def add_multiple():
    return MultiEditorAdd.render();


@samples_bp.route("/samples/edit-multiple", methods=["POST"])
def edit_multiple():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return MultiEditor.render(selected);



@samples_bp.route("/samples/validate-delete", methods=["POST"])
def validate_delete():
    selected = [int(i) for i in request.form.getlist("selected-samples")];
    return delete.Validate.render(selected);


@samples_bp.route("/samples/delete", methods=["POST"])
def delete_samples():
    selected = [int(i) for i in request.form.getlist("samples-to-delete")];
    for sample_id in selected:
        Samples.delete(sample_id);
    return redirect(url_for('samples_bp.show'));
