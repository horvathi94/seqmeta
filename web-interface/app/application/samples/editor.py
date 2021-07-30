from flask import render_template
from application.src.samples.samples import Samples
from application.src.fields import Field
from application.src.defaults import DefaultValues
from application.src.seqfiles.seqfiles import SeqFilesBunch
from application.src.seqfiles.db import SeqFile, \
    AssemblyFileTypes, ReadFileTypes
from application.src.editor.dlist import get_dlist
from .editor_fields import FIELDS_LIST
from application.src.samples.samples import Samples


from flask import jsonify


class Editor:

    def __init__(self, sample_id):
        self.sample_id = sample_id;
        self.sample = Samples.fetch_entry_edit(id=self.sample_id,
                                                id_key="sample_id");


    def get_value(self, field):
        if field["field_type"] == "seqfile":
            ftype = field["db_key"].replace("_file", "");
            return SeqFile.fetch_filename(self.sample_id, ftype=ftype);
        if self.sample_id != 0:
            return self.sample[field["db_key"]];
        defs = DefaultValues.fetch();
        if field["db_key"] in defs:
            if defs[field["db_key"]] != None:
                return defs[field["db_key"]];
        if field["field_type"] in ["select", "radio"]:
            return 0;
        return "";


    def single(self, handle):
        dlist = get_dlist(handle);
        field = Field.fetch(handle);
        field["input"]["value"] = self.get_value(field);
        return render_template("samples/form/single/field.html",
                               info=field, dlist=dlist);


    def show(self):
        html = render_template("samples/form/single/head.html",
                               sample_id=self.sample_id);
        for fd in FIELDS_LIST:
            html+= self.single(fd);
        html+= render_template("samples/form/single/tail.html");
        return html;



class MultiEditor:

    def __init__(self, sample_ids=[]):
        self.head = [];
        self.all = [];
        self.template = [];
        self.sample_ids = sample_ids;
        self.sample_rows = [];


    @classmethod
    def get_value(cls, field):
        defs = DefaultValues.fetch();
        if field["db_key"] in defs:
            if defs[field["db_key"]] != None:
                return defs[field["db_key"]];
        return "";


    @classmethod
    def header_col(cls, info):
       return render_template("samples/form/multi/col_head.html", info=info);


    @classmethod
    def all_col(cls, info):
        dlist = [];
        val = cls.get_value(info);
        if info["field_type"] in ["text", "number"]:
            info["input"]["onchange"] = "updateColumn(this);";
        elif info["field_type"] in ["select", "radio"]:
            dlist = get_dlist(info["handle"]);
            if val == "": val = 0;
        info["input"]["value"] = val;
        return render_template("samples/form/multi/col_all.html",
                               info=info, dlist=dlist);


    @classmethod
    def template_col(cls, info):
        dlist = [];
        val = cls.get_value(info);
        info["input"]["onchange"] = "";
        if info["field_type"] in ["select", "radio", "seqfile"]:
            dlist = get_dlist(info["handle"]);
            if val == "": val = 0;
        if info["handle"] == "sample_name":
            info["input"]["onchange"] = "checkSampleNames();";
        if info["handle"] == "library_id":
            info["input"]["onchange"] = "checkLibraryNames();";
        info["input"]["value"] = val;
        return render_template("samples/form/multi/col_template.html",
                               info=info, dlist=dlist);


    @classmethod
    def sample_col(cls, info, sample):
        dlist = [];
        assemblies = ["assembly_file", "contigs_file", "scaffolds_file"];
        reads = ["fwread_file", "rvread_file"];
        if info["db_key"] not in assemblies + reads:
            val = sample[info["db_key"]];
        else:
            seqfiles = SeqFilesBunch(sample["sample_id"]);
            if info["db_key"] in assemblies:
                seqfile_types = AssemblyFileTypes.fetch_list_labeled(
                    replace_key="item_key");
            if info["db_key"] in reads:
                seqfile_types = ReadFileTypes.fetch_list_labeled(
                    replace_key="item_key");
            ftype = info["db_key"].replace("_file", "");
            val = SeqFile.fetch_filename(sample["sample_id"], ftype=ftype);
        info["input"]["multi_template"] = \
            info["input"]["multi_template"].replace(
                "+0+", "+"+str(sample["sample_id"])+"+")
        info["input"]["onchange"] = "";
        if info["field_type"] in ["select", "radio", "seqfile"]:
            dlist = get_dlist(info["handle"]);
            if val == "": val = 0;
        if info["handle"] == "sample_name":
            info["input"]["onchange"] = "checkSampleNames();";
        if info["handle"] == "library_id":
            info["input"]["onchange"] = "checkLibraryNames();";
        info["input"]["value"] = val;
        return render_template("samples/form/multi/col_sample.html",
                               info=info, dlist=dlist);


    def add_field(self, handle):
        field = Field.fetch(handle);
        self.head.append(self.header_col(field));
        self.all.append(self.all_col(field));
        self.template.append(self.template_col(field));


    def get_html(self):
        html = "<tr>";
        for col in self.head:
            html+= col;
        html+= "</tr>";
        html+= "<tr class='editor row all'>";
        for col in self.all:
            html+= col;
        html+= "</tr>";
        html+= "<tr class='editor row template' \
            style='visibility: collapse;'>";
        for col in self.template:
            html+= col;
        html+= "</tr>";
        for row in self.sample_rows:
            html+= "<tr>";
            for col in row:
                html+= col;
            html+= "</tr>";
        return html;


    def show(self, tp="add"):
        reg_samples = Samples.fetch_list();
        html = render_template("samples/form/multi/head.html",
                               form_type=tp,
                               reg_samples=reg_samples);
        for fd in FIELDS_LIST:
            self.add_field(fd);

        for sample_id in self.sample_ids:
            new_row = [];
            sample = Samples.fetch("view_samples_base", sample_id);
            for handle in FIELDS_LIST:
                field = Field.fetch(handle);
                new_row.append(self.sample_col(field, sample));
            self.sample_rows.append(new_row);

        html+= self.get_html();
        html+= render_template("samples/form/single/tail.html");
        return html;

