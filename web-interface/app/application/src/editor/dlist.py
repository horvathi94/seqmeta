from application.src.authors import Authors, AuthorGroups
from application.src.institutions import Institutions
from application.src import misc
from application.src import library as lib
from application.src.samples.extensions.host import Host,\
    PATIENT_GENDERS
from application.src.samples.extensions.health_status import HealthStatus,\
    HOSPITALISATIONS
from application.src.samples.extensions.library import Library,\
    LIBRARY_LAYOUTS
from application.src.samples.extensions.treatment import \
    ANTIVIRAL_TREAT, \
    PRIOR_INFECTION
from application.src.seqfiles.db import SeqFileTypes


DLIST = {

    "collector_name": Authors.fetch_list_labeled(
        replace_key="abbreviated_middle_name"),
    "location_continent": misc.Continents.fetch_list(),
    "location_country": misc.Countries.fetch_list(),
    "host": misc.Hosts.fetch_list(),
    "patient_gender": PATIENT_GENDERS,
    "patient_status": misc.PatientStatuses.fetch_list(),
    "host_habitat": misc.HostHabitats.fetch_list(),
    "host_behaviour": misc.HostBehaviours.fetch_list(),
    "prior_sars_cov_2_antiviral_treat": ANTIVIRAL_TREAT,
    "prior_sars_cov_2_infection": PRIOR_INFECTION,
    "prior_sars_cov_2_vaccination": misc.HasVaccine.fetch_list(),
    "host_health_state": misc.HostHealthStates.fetch_list(),
    "hospitalisation": HOSPITALISATIONS,
    "sars_cov_2_diag_gene_name_1": misc.SarsCovGenes.fetch_list(),
    "sars_cov_2_diag_gene_name_2": misc.SarsCovGenes.fetch_list(),
    "submitting_lab": Institutions.fetch_list_labeled(),
    "originating_lab": Institutions.fetch_list_labeled(),
    "sequencing_lab": Institutions.fetch_list_labeled(),
    "author_group": AuthorGroups.fetch_list_labeled(replace_key="group_name",
                                        replace_id="group_id"),
    "sampling_strategy": misc.SamplingStrategies.fetch_list(),
    "sample_capture_status": misc.SampleCaptureStatuses.fetch_list(),
    "specimen_source": misc.SpecimenSources.fetch_list(),
    "sequencing_instrument": misc.SequencingInstruments.fetch_list(),
    "assembly_method": misc.AssemblyMethods.fetch_list(),
    "library_layout": LIBRARY_LAYOUTS,
    "library_source": \
        lib.LibrarySources.fetch_list_labeled(replace_key="item_key"),
    "library_selection": \
        lib.LibrarySelections.fetch_list_labeled(replace_key="item_key"),
    "library_strategy": \
        lib.LibraryStrategies.fetch_list_labeled(replace_key="item_key"),
    "geo_loc_exposure": misc.Countries.fetch_list(),

    "host_anatomical_material": misc.HostAnatomicalMaterials.fetch_list(),
    "host_body_product": misc.HostBodyProducts.fetch_list(),

    "purpose_of_sampling": misc.PurposesOfSampling.fetch_list(),
    "purpose_of_sequencing": misc.PurposesOfSequencing.fetch_list(),

    "collection_device": misc.CollectionDevices.fetch_list(),

    "assembly_file": SeqFileTypes.fetch_list_labeled(
                            replace_key="item_key"),

    "fwread_file": SeqFileTypes.fetch_list_labeled(
                            replace_key="item_key"),
    "rvread_file": SeqFileTypes.fetch_list_labeled(
                            replace_key="item_key"),

}

