from enum import Enum, auto
from application.src.forms.form import Form
from application.src.seqfiles.types import SeqFileTypes
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
from application.src.seqfiles.db import SeqFile


import sys




class _SaveBase:


    @classmethod
    def parse_request(cls, raw: "flask.request.form") -> list:
        pass;


    @classmethod
    def parse_list(cls, raw: "flask.request.form") -> list:
        sample_data = Form.parse_list(raw, "sample")[1:];
        collection = Form.parse_list(raw, "collection")[1:];
        location = Form.parse_list(raw, "location")[1:];
        host = Form.parse_list(raw, "host")[1:];
        treatment = Form.parse_list(raw, "treatment")[1:];
        health = Form.parse_list(raw, "health")[1:];
        sequencing = Form.parse_list(raw, "sequencing")[1:];
        sampling = Form.parse_list(raw, "sampling")[1:];
        library = Form.parse_list(raw, "library")[1:];
#        fs = parse_files_multiple(request)[1:];

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
#            save_data["seqfiles"] = fs[i];
            samples.append(save_data);
        return samples;


    @classmethod
    def parse_file_bunch(cls, info: dict, files: dict) -> dict:
        data = {"id": info["id"]};
        for handle in info:
            if handle in SeqFileTypes.list_values():
                if files[handle].filename == "": continue;
                data[handle] = {};
                data[handle]["type"] = handle;
                data[handle]["filename"] = files[handle].filename;
                data[handle]["filedata"] = files[handle];
        return data;


    @classmethod
    def parse_files(cls, raw: "flask.request.form",
                    files: "flask.request.files") -> list:
        bunch_data = Form.parse_list(raw, "seqfile");
        bunch_files = Form.parse_list(files, "seqfile");

        fdata = [];
        for bd, bf in zip(bunch_data, bunch_files):
            fdata.append(cls.parse_file_bunch(bd, bf));

        return fdata;


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
    def save_to_db(cls, submitted_samples: list) -> None:

        sample_ids = [];
        for submitted in submitted_samples:
            sample_id = cls.save_sample_data(submitted["sample"]);
            cls.save_collection_data(submitted["collection"], sample_id);
            cls.save_location_data(submitted["location"], sample_id);
            cls.save_host_data(submitted["host"], sample_id);
            cls.save_treatment_data(submitted["treatment"], sample_id);
            cls.save_health_data(submitted["health"], sample_id);
            cls.save_sequencing_data(submitted["sequencing"], sample_id);
            cls.save_library_data(submitted["library"], sample_id);
            cls.save_virusname(submitted["sample"]["gisaid_virusname"],
                               sample_id);
            cls.save_isolatename(submitted["sample"]["isolate"], sample_id);

#            if "seqfiles" in submitted:
#                seqfiles = submitted["seqfiles"];
#                save_files(seqfiles, sample_id);


    @classmethod
    def save(cls, data: "flask.request.form",
             files: "flask.request.files") -> None:
        submitted = cls.parse_request(data, files);
        cls.save_to_db(submitted);



class SaveSingle(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form",
                      files: "flask.request.files") -> list:
        save_data = {};
        save_data["sample"] = Form.parse_simple(raw, "sample");
        save_data["location"] = Form.parse_simple(raw, "location");
        save_data["collection"] = Form.parse_simple(raw, "collection");
        save_data["library"] = Form.parse_simple(raw, "library");
        save_data["host"] = Form.parse_simple(raw, "host");
        save_data["sampling"] = Form.parse_simple(raw, "sampling");
        save_data["health"] = Form.parse_simple(raw, "health");
        save_data["sequencing"] = Form.parse_simple(raw, "sequencing");
        save_data["treatment"] = Form.parse_simple(raw, "treatment");
        save_data["seqfiles"] = cls.parse_files(raw, files)[0];
        return [save_data];




class EditMultiple(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form") -> list:
        save_data = cls.parse_list();




class AddMultiple(_SaveBase):


    @classmethod
    def parse_request(cls, raw: "flask.request.form") -> list:
        save_data = cls.parse_list();
        for item in save_data:
            item["sample"]["sample_id"]: 0;






class Saver:



    @classmethod
    def parse_files(cls, raw: "flask.request.form") -> list:
        seqfiles = Form.parse_list(raw, "seqfile");
        pass;



    @classmethod
    def parse_multiple(cls, raw: "flask.request.form") -> list:
        """Parse data submitted from multiple samples editor."""



