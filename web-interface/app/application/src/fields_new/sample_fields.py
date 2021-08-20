from enum import Enum


class SampleFields(Enum):

    """Mapping of field handles form the database to custom Enum class."""

    NONE = "";
    SAMPLE_NAME = "sample_name";
    SAMPLE_COMMENT = "sample_comment";
    SAMPLE_TITLE = "sample_title";
    SAMPLE_DESCRIPTION = "sample_description";
    GISAID_ACCESSION = "gisaid_accession";
    GISAID_VIRUSNAME = "gisaid_virusname";
    ISOLATE_NAME = "isolate";
    COLLECTION_YEAR = "collection_year";
    COLLECTION_MONTH = "collection_month";
    COLLECTION_DAY = "collection_day";
    COLLECTOR_NAME = "collector_name";
    COLLECTION_DEVICE = "collection_device";
    LOCATION_CONTINENT = "location_continent";
    LOCATION_COUNTRY = "location_country";
    LOCATION_REGION = "location_region";
    LOCATION_LOCALITY = "location_locality";
    ADDITIONAL_LOCATION_INFO = "additional_location_info";
    GEOLOC_LATITUDE = "geo_loc_latitude";
    GEOLOC_LONGITUDE = "geo_loc_longitude";
    GEOLOC_EXPOSURE = "geo_loc_exposure";
    HOST = "host";
    HOST_SUBJECT_ID = "host_subject_id";
    ADDITIONAL_HOST_INFO = "additional_host_info";
    HOST_GENDER = "patient_gender";
    HOST_AGE = "patient_age";
    HOST_STATUS = "patient_status";
    PPE = "ppe";
    HOST_HABITAT = "host_habitat";
    HOST_BEHAVIOUR = "host_behaviour";
    HOST_DESCRIPTION = "host_description";
    HOST_GRAVIDITY = "host_gravidity";
    HOST_RECENT_TRAVEL_LOCATION = "host_recent_travel_loc";
    HOST_RECENT_TRAVEL_RETURN_DATE = "host_recent_travel_return_date";
    HOST_ANATOMICAL_MATERIAL = "host_anatomical_material";
    HOST_BODY_PRODUCT = "host_body_product";

    PRIOR_SARS_COV_2_ANTIVIRAL_TREATMENT = "prior_sars_cov_2_antiviral_treat";
    ANTIVIRAL_TREATMENT_AGENT = "antiviral_treatment_agent";
    DATE_OF_PRIOR_ANTIVIRAL_TREATMENT = "date_of_prior_antiviral_treat";
    PRIOR_SARS_COV_2_INFECTION = "prior_sars_cov_2_infection";
    DATE_OF_PRIOR_SARS_COV_2_INFECTION = "date_of_prior_sars_cov_2_infection";
    VIRUS_ISOLATE_OF_PRIOR_INFECTION = "virus_isolate_of_prior_infection";
    PRIOR_SARS_COV_2_VACCINATION = "prior_sars_cov_2_vaccination";
    VACCINE_RECEIVED = "vaccine_received";
    DATE_OF_PRIOR_SARS_COV_2_VACCINATION = \
        "date_of_prior_sars_cov_2_vaccination";
    SUBJECT_EXPOSURE = "subject_exposure";
    SUBJECT_EXPOSURE_DURATION = "subject_exposure_duration";
    TYPE_EXPOSURE = "type_exposure";
    OUTBREAK = "outbreak";
    HOST_HEALTH_STATUS = "host_health_state";
    HOSPITALISATION = "hospitalisation";
    ILNESS_SYMPTOMS = "ilness_symptoms";
    ILNESS_DURATION = "ilness_duration";
    HOST_DISEASE_OUTCOME = "host_disease_outcome";
    SARS_COV_2_DIAG_GENE_NAME_1 = "sars_cov_2_diag_gene_name_1";
    SARS_COV_2_DIAG_PCR_CT_VALUE_1 = "sars_cov_2_diag_pcr_ct_value_1";
    SARS_COV_2_DIAG_GENE_NAME_2 = "sars_cov_2_diag_gene_name_2";
    SARS_COV_2_DIAG_PCR_CT_VALUE_2 = "sars_cov_2_diag_pcr_ct_value_2";
    ORIGINATING_LAB_SAMPLE = "originating_lab";
    ORIGINATING_LAB_SAMPLE_NAME = "originating_lab_sample_name";
    SEQUENCING_LAB = "sequencing_lab";
    SUBMITTING_LAB = "submitting_lab";
    SUBMITTING_LAB_SAMPLE_NAME = "submitting_lab_sample_name";
    AUTHOR_GROUP = "author_group";
    SAMPLING_STRATEGY = "sampling_strategy";
    PURPOSE_OF_SAMPLING = "purpose_of_sampling";
    PURPOSE_OF_SEQUENCING = "purpose_of_sequencing";
    STRAIN = "strain";
    ISOLATION_SOURCE_HOST_ASSOCIATED = "isolation_source_host_associated";
    ISOLATION_SOURCE_NON_HOST_ASSOCIATED = \
        "isolation_source_non_host_associated";
    SAMPLE_CAPTURE_STATUS = "sample_capture_status";
    SPECIMEN_SOURCE = "specimen_source";
    SAMPLE_STORAGE_CONDITIONS = "sample_storage_conditions";
    PASSAGE_NUMBER = "passage_number";
    PASSAGE_METHOD = "passage_method";
    DEFINITION_FOR_SEROPOSITIVE_SAMPLE = "definition_for_seropositive_sample";
    SEROTYPE = "serotype";
    SEQUENCING_INSTRUMENT = "sequencing_instrument";
    ASSEMBLY_METHOD = "assembly_method";
    COVERAGE = "coverage";
    LIBRARY_ID = "library_id";
    LIBRARY_LAYOUT = "library_layout";
    LIBRARY_SOURCE = "library_source";
    LIBRARY_SELECTION = "library_selection";
    LIBRARY_STRATEGY = "library_strategy";
    LIBRARY_PREPARATION_DATE = "library_preparation_date";
    LIBRARY_DESIGN_DESCRIPTION = "library_design_description";
    INSERT_SIZE = "insert_size";
    LIBRARY_CONSTRUCTION_PROTOCOL = "library_construction_protocol";

    CONSENSUS_FILE = "assembly_file";
    CONTIGS_FILE = "contigs_file";
    SCAFFOLDS_FILE = "scaffolds_file";
    FORWARD_READ_FILE = "fwread_file";
    REVERSE_READ_FILE = "rvread_file";
    COLLECTOR_NAME = "collector_name";


    @classmethod
    def list_for_editor(cls) -> list:
        """List fields for editor."""
        items = [];
        for e in cls:
            if e != cls.NONE: items.append(e);
        return items;

