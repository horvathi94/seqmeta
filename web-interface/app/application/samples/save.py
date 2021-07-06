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


def save(submitted_samples):

    sample_ids = [];
    for submitted in submitted_samples:
        sample_data = submitted["sample"];
        sample_id = Samples.save_entry(sample_data);
        sample_ids.append(sample_id);
        collection = submitted["collection"];
        collection["sample_id"] = sample_id;
        Collection.save_entry(collection);
        location = submitted["location"];
        location["sample_id"] = sample_id;
        Location.save_entry(location);
        host = submitted["host"];
        host["sample_id"] = sample_id;
        Host.save_entry(host);
        treatment = submitted["treatment"];
        treatment["sample_id"] = sample_id;
        PatientTreatment.save_entry(treatment);
        health = submitted["health"];
        health["sample_id"] = sample_id;
        HealthStatus.save_entry(health);
        sampling = submitted["sampling"];
        sampling["sample_id"] = sample_id;
        Sampling.save_entry(sampling);
        sequencing = submitted["sequencing"];
        sequencing["sample_id"] = sample_id;
        Sequencing.save_entry(sequencing);
        library = submitted["library"];
        library["sample_id"] = sample_id;
        Library.save_entry(library);
        sample_data["sample_id"] = sample_id;
        if sample_data["gisaid_virusname"] == "":
            sample_data["gisaid_virusname"] = \
                VirusnameGisaid.format_name(sample_id);
            sample_id = Samples.save_entry(sample_data);
        if sample_data["isolate"] == "":
            sample_data["isolate"] = \
                IsolateEna.format_name(sample_id);
            sample_id = Samples.save_entry(sample_data);

    return sample_ids;
