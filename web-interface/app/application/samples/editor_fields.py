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



FIELDS_LIST = [

    "sample_name",
    "sample_comment",
    "sample_title",
    "sample_description",
    "gisaid_accession",
    "collection_year",
    "collection_month",
    "collection_day",
    "collector_name",
    "location_continent",
    "location_country",
    "location_region",
    "location_locality",
    "additional_location_info",
    "geo_loc_latitude",
    "geo_loc_longitude",
    "host",
    "host_subject_id",
    "additional_host_info",
    "patient_gender",
    "patient_age",
    "patient_status",
    "ppe",
    "host_habitat",
    "host_behaviour",
    "host_description",
    "host_gravidity",
    "host_recent_travel_loc",
    "host_recent_travel_return_date",

    "prior_sars_cov_2_antiviral_treat",
    "antiviral_treatment_agent",
    "date_of_prior_antiviral_treat",
    "prior_sars_cov_2_infection",
    "date_of_prior_sars_cov_2_infection",
    "virus_isolate_of_prior_infection",
    "prior_sars_cov_2_vaccination",
    "vaccine_received",
    "date_of_prior_sars_cov_2_vaccination",
    "subject_exposure",
    "subject_exposure_duration",
    "type_exposure",
    "outbreak",
    "host_health_state",
    "hospitalisation",
    "ilness_symptoms",
    "ilness_duration",
    "sars_cov_2_diag_gene_name_1",
    "sars_cov_2_diag_pcr_ct_value_1",
    "sars_cov_2_diag_gene_name_2",
    "sars_cov_2_diag_pcr_ct_value_2",
    "originating_lab",
    "originating_lab_sample_name",
    "submitting_lab",
    "submitting_lab_sample_name",
    "author_group",
    "sampling_strategy",
    "strain",
    "isolation_source_host_associated",
    "isolation_source_non_host_associated",
    "sample_capture_status",
    "specimen_source",
    "sample_storage_condition",
    "passage_number",
    "passage_method",
    "definition_for_seropositive_sample",
    "serotype",
    "sequencing_instrument",
    "assembly_method",
    "coverage",
    "library_id",
    "library_layout",
    "library_source",
    "library_selection",
    "library_strategy",
    "library_preparation_date",
    "library_design_description",
    "insert_size",
    "library_construction_protcol",

];


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
    "originating_lab": Institutions.fetch_list_labeled(),
    "submitting_lab": Institutions.fetch_list_labeled(),
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

}


