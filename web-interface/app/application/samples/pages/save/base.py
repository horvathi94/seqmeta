from flask import redirect, url_for
from application.src.forms.form import Form
from application.src.samples.samples import Samples
from application.src.samples.extensions.collections import Collection
from application.src.samples.extensions.host import Host
from application.src.samples.extensions.health_status import HealthStatus
from application.src.samples.extensions.library import Library
from application.src.samples.extensions.location import Location
from application.src.samples.extensions.sampling import Sampling
from application.src.samples.extensions.sequencing import Sequencing
from application.src.samples.extensions.treatment import PatientTreatment
from application.src.samples.nametemplates.virusname_gisaid import \
    VirusnameGisaid
from application.src.samples.nametemplates.isolate_ena import \
    IsolateEna
from application.src.seqfiles.db import DBSeqFile
from application.src.seqfiles.types import SeqFileTypes
from application.src.seqfiles.seqfile_new import SeqFile

import sys

class _SaveBase:


    @classmethod
    def parse_request(cls, raw: "flask.request.form") -> list:
        pass;


    @classmethod
    def parse_list(cls, raw: "flask.request.form",\
                   files: "flask.request.files") -> list:
        sample_data = Form.parse_list(raw, "sample")[1:];
        collection = Form.parse_list(raw, "collection")[1:];
        location = Form.parse_list(raw, "location")[1:];
        host = Form.parse_list(raw, "host")[1:];
        treatment = Form.parse_list(raw, "treatment")[1:];
        health = Form.parse_list(raw, "health")[1:];
        sequencing = Form.parse_list(raw, "sequencing")[1:];
        sampling = Form.parse_list(raw, "sampling")[1:];
        library = Form.parse_list(raw, "library")[1:];
        fs = cls.parse_files(raw, files)[1:];

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
        return samples;


    @classmethod
    def save_sample_data(cls, sample_data: dict) -> int:
        """Saves data to the samples table, returns id."""
        sample_id = Samples.save_entry(sample_data);
        return sample_id;


    @classmethod
    def save_collection_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Collection.save_entry(data);


    @classmethod
    def save_location_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Location.save_entry(data);


    @classmethod
    def save_host_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Host.save_entry(data);


    @classmethod
    def save_treatment_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        PatientTreatment.save_entry(data);


    @classmethod
    def save_health_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        HealthStatus.save_entry(data);


    @classmethod
    def save_sampling_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Sampling.save_entry(data);


    @classmethod
    def save_sequencing_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Sequencing.save_entry(data);


    @classmethod
    def save_library_data(cls, data: dict, sample_id: int) -> None:
        data["sample_id"] = sample_id;
        Library.save_entry(data);


    @classmethod
    def save_virusname(cls, virusname: str, sample_id: int) -> None:
        if virusname == "":
            virusname = VirusnameGisaid.format_name(sample_id);
        Samples.update_virusname(sample_id, virusname);


    @classmethod
    def save_isolatename(cls, isolate: str, sample_id: int) -> None:
        if isolate == "":
            isolate = IsolateEna.format_name(sample_id);
        Samples.update_isolatename(sample_id, isolate);


    @classmethod
    def parse_file_bunch(cls, info: dict, files: dict, assemb: dict) -> list:

        data = [];

        for handle in info:

            fdata = {"filedata": None,
                     "assembly_method_id": None,
                     "file_type_id": None};

            if handle in SeqFileTypes.list_values():

                upload_name = files[handle].filename;
                fdata["seqtype"] = SeqFileTypes(handle);

                if upload_name != "":
                    fdata["filedata"] = files[handle];

                fdata["file_type_id"] = int(info[handle]);
                if handle in assemb:
                    fdata["assembly_method_id"] = int(assemb[handle]);

                data.append(fdata);

        return data;


    @classmethod
    def parse_files(cls, raw: "flask.request.form",
                    files: "flask.request.files") -> list:
        bunch_data = Form.parse_list(raw, "seqfile");
        bunch_files = Form.parse_list(files, "seqfile");
        bunch_assembly = Form.parse_list(raw, "seqfile_assembly");

        print(f"\nBunch data: {bunch_data}", file=sys.stderr);
        print(f"\nBunch assembly: {bunch_assembly}", file=sys.stderr);
        fdata = [];
        for bd, bf, ba in zip(bunch_data, bunch_files, bunch_assembly):
            fdata.append(cls.parse_file_bunch(bd, bf, ba));

        for fd in fdata[0]:
            print(f"Fdata: {fd}", file=sys.stderr);
        return fdata;


    @classmethod
    def save_seqfile_bunch(cls, seqfile_bunch: list, sample_id: int) -> None:
        for fdata in seqfile_bunch:

            seqfile = SeqFile(fdata["seqtype"], sample_id);
            do_save_data = False;
            do_save_file = False;

            if fdata["filedata"] is not None:
                # If user uploaded a file save it, and rewrite db data.
                do_save_file = True;
                do_save_data = True;

            if not do_save_data:
                # If file exists, then db data is rewritten.
                do_save_data = seqfile.check_exists();

            if do_save_data:
                # Save data:
                seqfile.assembly_method_id = fdata["assembly_method_id"];
                seqfile.file_type_id = fdata["file_type_id"];
                seqfile.save_data();

            if do_save_file:
                # Save file:
                seqfile = SeqFile(fdata["seqtype"], sample_id);
                seqfile.filedata = fdata["filedata"];
                seqfile.save_file();



    @classmethod
    def save_to_db(cls, submitted_samples: list) -> None:

        sample_ids = [];
        for submitted in submitted_samples:
            sample_id = cls.save_sample_data(submitted["sample"]);
            cls.save_collection_data(submitted["collection"], sample_id);
            cls.save_location_data(submitted["location"], sample_id);
            cls.save_host_data(submitted["host"], sample_id);
            cls.save_sampling_data(submitted["sampling"], sample_id);
            cls.save_treatment_data(submitted["treatment"], sample_id);
            cls.save_health_data(submitted["health"], sample_id);
            cls.save_sequencing_data(submitted["sequencing"], sample_id);
            cls.save_library_data(submitted["library"], sample_id);
            cls.save_virusname(submitted["sample"]["gisaid_virusname"],
                               sample_id);
            cls.save_isolatename(submitted["sample"]["isolate"], sample_id);

            if "seqfiles" in submitted:
                cls.save_seqfile_bunch(submitted["seqfiles"], sample_id);


    @classmethod
    def save(cls, data: "flask.request.form",
             files: "flask.request.files") -> "flask.redirect":
        submitted = cls.parse_request(data, files);
        cls.save_to_db(submitted);
        return redirect(url_for("samples_bp.show"));

