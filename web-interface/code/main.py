from flask import Flask, render_template, request, redirect, url_for, \
    jsonify, make_response
from datetime import datetime

from src.cursor import Cursor
from src.samples import Samples
from src.authors import Authors, AuthorNameTag
from src.institutions import Institutions
from src.author_groups import AuthorGroups
from src.fast_files import Fasta
from src.excel_generator import excel_test
from src import funcs


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False;



@app.route("/")
def home():

    html = render_template("head.html");
    html+= render_template("index.html");
    html+= render_template("footer.html");
    return html;




# Samples
###############################################################################

@app.route("/samples")
def samples_list():

    samples = Samples();
    samples_list = samples.fetch_list();
    html = render_template("head.html", styles=["prompt.css", "samples.css"]);
    if len(samples_list) == 0:
        html+= render_template("samples/empty.html");
    else:
        html+= render_template("samples/list.html", samples=samples_list);

    scripts = ["sample_details.js"];
    html+= render_template("footer.html", scripts=scripts);

    test_data = samples.fetch_entry(sample_id=1);
    html+= str(test_data);
    return html;


@app.route("/sample/details")
def sample_details():

    sample_id = 0;
    if "id" in request.args:
        sample_id = int(request.args["id"]);

    samples = Samples();
    sample_details = samples.fetch_entry(sample_id=sample_id);

    return jsonify(sample_details);


@app.route("/samples/edit")
def samples_edit():

    sample_id = 0;
    if "id" in request.args:
        sample_id = int(request.args["id"]);


    html = render_template("head.html");

    samples = Samples();
    sample = samples.fetch_entry(sample_id=sample_id);

    author_groups = AuthorGroups();
    author_groups = author_groups.fetch_display_list();

    institutions = Institutions();
    institutions = institutions.fetch_list();

    html+= render_template("samples/edit.html",
                           sample=sample,
                           author_groups=author_groups,
                           institutions=institutions);

    html+= render_template("footer.html");

    return html;


@app.route("/samples/submit", methods=["POST"])
def samples_submit():

    form_data = request.form.to_dict();

    samples = Samples();
    samples.save_entry(form_data);
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

    selected = request.form.getlist("selected-samples");
    selected = [int(s) for s in selected];

    samples = Samples();
    sample_list = samples.fetch_entries(sample_ids=[1,2]);

    excel_test(sample_list);
    return jsonify(sample_list);


# Authors section
###############################################################################

@app.route("/authors")
def authors_page():

    authors = Authors();
    authors_list = authors.fetch_list();
    html = render_template("head.html");
    if len(authors_list) == 0:
        html+= render_template("authors/empty.html");
    else:
        html+= render_template("authors/list.html", authors=authors_list);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/edit")
def authors_edit():

    author_id = 0;
    if "id" in request.args:
        author_id = int(request.args["id"]);
    authors = Authors();
    author = authors.fetch_entry(id=author_id);
    html = render_template("head.html");
    html+= render_template("authors/edit.html", author=author);
    html+= render_template("footer.html");
    return html;


@app.route("/authors/submit", methods=["POST"])
def authors_submit():

    data = request.form.to_dict();
    authors = Authors();
    authors.save_entry(data);
    return redirect(url_for('authors_page'));


@app.route("/authors/groups")
def author_groups_list():

    groups = AuthorGroups();
    groups_list = groups.fetch_display_list();

    html = render_template("head.html");

    if len(groups_list) == 0:
        html+= render_template("author_groups/empty.html");
    else:
        html+= render_template("author_groups/list.html", groups=groups_list);

    html+= render_template("footer.html");
    return html;


@app.route("/authors/groups/edit")
def author_groups_edit():

    group_id = 0;
    if "id" in request.args:
        group_id = int(request.args["id"]);

    author_group = AuthorGroups();
    group = author_group.fetch_entry(group_id=group_id);

    authors = Authors();
    authors_list = authors.fetch_list();
    authors_list = sorted(authors_list, key=lambda k: k["last_name"]);
    for a in authors_list:
        tag = AuthorNameTag(a);
        a["name_tag"] = tag.abreviated_middle_name();


    html = render_template("head.html");
    html+= render_template("author_groups/edit.html",
                           group_id = group_id,
                           group=group,
                           authors_list=authors_list);
    html+= render_template("footer.html", scripts=["author_groups.js"]);
    return html;


@app.route("/authors/groups/submit", methods=["POST"])
def author_groups_submit():

    form_data = request.form.to_dict();

    authors_list = funcs.parse_form_list(form_data, "author");
    group = funcs.parse_form_simple(form_data, "group");

    author_groups = AuthorGroups();
    author_groups.save(group, authors_list);

    return redirect(url_for('author_groups_list'));

# Institutions
###############################################################################

@app.route("/institutions")
def institutions_list():

    institutions = Institutions();
    institutions_list = institutions.fetch_list();
    html = render_template("head.html");
    if len(institutions_list) == 0:
        html+= render_template("institutions/empty.html");
    else:
        html+= render_template("institutions/list.html",
                               institutions=institutions_list);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/edit")
def institutions_edit():

    institution_id = 0;
    if "id" in request.args:
        institution_id = int(request.args["id"]);
    institutions = Institutions();
    institution = institutions.fetch_entry(id=institution_id);

    html = render_template("head.html");
    html+= render_template("institutions/edit.html", institution=institution);
    html+= render_template("footer.html");
    return html;


@app.route("/institutions/submit", methods=["POST"])
def institutions_submit():

    data = request.form.to_dict();
    institutions = Institutions();
    institutions.save_entry(data);
    return redirect(url_for('institutions_list'));





@app.route("/test")
def test():

    html = render_template("head.html", styles=["test.css"]);
    html+= "<h2> This page is for running tests </h2>";

    cursor = Cursor();
    raw = cursor.select_all("sample_data");
    cursor.close();

    html+= str(raw);

    html+= render_template("footer.html", scripts=["authors_submit.js"]);

    return html;


if __name__ == "__main__":
   app.run("0.0.0.0", debug=True);
