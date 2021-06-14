from application.src.samples.samples import Samples
from application.src.samples.extensions.collections import Collection
from application.src.samples.extensions.host import Host
from application.src.samples.extensions.health_status import HealthStatus
from application.src.samples.extensions.library import Library
from application.src.samples.extensions.location import Location
from application.src.samples.extensions.sampling import Sampling
from application.src.samples.extensions.sequencing import Sequencing


def save(submitted_samples):

    for submitted in submitted_samples:
        sample_data = submitted["sample"];
        sample_id = Samples.save_entry(sample_data);
        location = submitted["location"];
        location["sample_id"] = sample_id;
        Location.save_entry(location);
        collection = submitted["collection"];
        collection["sample_id"] = sample_id;
        Collection.save_entry(collection);
        library = submitted["library"];
        library["sample_id"] = sample_id;
        Library.save_entry(library);
        host = submitted["host"];
        host["sample_id"] = sample_id;
        Host.save_entry(host);
        sampling = submitted["sampling"];
        sampling["sample_id"] = sample_id;
        Sampling.save_entry(sampling);
        health = submitted["health"];
        health["sample_id"] = sample_id;
        HealthStatus.save_entry(health);
        sequencing = submitted["sequencing"];
        sequencing["sample_id"] = sample_id;
        Sequencing.save_entry(sequencing);