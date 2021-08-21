from application.src.forms.form import Form



class Saver:


    @classmethod
    def parse_files(cls, raw: "flask.request.form") -> list:
        seqfiles = Form.parse_list(raw, "seqfile");
        pass;


    @classmethod
    def parse_single(cls, raw: "flask.request.form") -> dict:
        """Parse data submitted from single sample editor."""
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
#        save_data["seqfiles"] = parse_files_multiple(request)[0];
        return save_data;

    @classmethod
    def parse_multiple(cls, raw: "flask.request.form") -> list:
        """Parse data submitted from multiple samples editor."""
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



