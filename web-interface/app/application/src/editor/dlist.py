from application.src.authors import Authors, AuthorGroups
from application.src.institutions import Institutions
from application.src import misc
from application.src import library as lib
from application.src.samples.extensions.host import Host
from application.src.samples.extensions.library import Library
from application.src.seqfiles.db import SeqFileTypes, \
    AssemblyFileTypes, ReadFileTypes



def get_dlist(handle):

    if handle == "collector_name":
        return Authors.fetch_list_labeled(
            replace_key="abbreviated_middle_name");
    if handle == "location_continent":
        return misc.Continents.fetch_list();
    if handle == "location_country":
        return misc.Countries.fetch_list();
    if handle == "host":
        return misc.Hosts.fetch_list();
    if handle == "patient_gender":
        return PATIENT_GENDERS;
    if handle == "patient_status":
        return misc.PatientStatuses.fetch_list();
    if handle == "host_habitat":
        return misc.HostHabitats.fetch_list();
    if handle == "host_behaviour":
        return misc.HostBehaviours.fetch_list();
    if handle == "prior_sars_cov_2_antiviral_treat":
        return ANTIVIRAL_TREAT;
    if handle == "prior_sars_cov_2_infection":
        return PRIOR_INFECTION;
    if handle == "prior_sars_cov_2_vaccination":
        return misc.HasVaccine.fetch_list();
    if handle == "host_health_state":
        return misc.HostHealthStates.fetch_list();
    if handle == "hospitalisation":
        return HOSPITALISATIONS;
    if handle == "sars_cov_2_diag_gene_name_1":
        return misc.SarsCovGenes.fetch_list();
    if handle == "sars_cov_2_diag_gene_name_2":
        return misc.SarsCovGenes.fetch_list();
    if handle == "submitting_lab":
        return Institutions.fetch_list_labeled();
    if handle == "originating_lab":
        return Institutions.fetch_list_labeled();
    if handle == "sequencing_lab":
        return Institutions.fetch_list_labeled();
    if handle == "author_group":
        return AuthorGroups.fetch_list_labeled(
            replace_key="group_name", replace_id="group_id");
    if handle == "sampling_strategy":
        return misc.SamplingStrategies.fetch_list();
    if handle == "sample_capture_status":
        return misc.SampleCaptureStatuses.fetch_list();
    if handle == "specimen_source":
        return misc.SpecimenSources.fetch_list();
    if handle == "sequencing_instrument":
        return misc.SequencingInstruments.fetch_list();
    if handle == "assembly_method":
        return misc.AssemblyMethods.fetch_list();
    if handle == "library_layout":
        return LIBRARY_LAYOUTS;
    if handle == "library_source":
        return lib.LibrarySources.fetch_list_labeled(replace_key="item_key");
    if handle == "library_selection":
        return \
            lib.LibrarySelections.fetch_list_labeled(replace_key="item_key");
    if handle == "library_strategy":
        return \
            lib.LibraryStrategies.fetch_list_labeled(replace_key="item_key");
    if handle == "geo_loc_exposure":
        return misc.Countries.fetch_list();

    if handle == "host_anatomical_material":
        return misc.HostAnatomicalMaterials.fetch_list();
    if handle == "host_body_product":
        return misc.HostBodyProducts.fetch_list();

    if handle == "purpose_of_sampling":
        return misc.PurposesOfSampling.fetch_list();
    if handle == "purpose_of_sequencing":
        return misc.PurposesOfSequencing.fetch_list();

    if handle == "collection_device":
        return misc.CollectionDevices.fetch_list();

    if handle == "assembly_file":
        return AssemblyFileTypes.fetch_list_labeled(replace_key="item_key");
    if handle == "contigs_file":
        return AssemblyFileTypes.fetch_list_labeled(replace_key="item_key");
    if handle == "scaffolds_file":
        return AssemblyFileTypes.fetch_list_labeled(replace_key="item_key");

    if handle == "fwread_file":
        return ReadFileTypes.fetch_list_labeled(replace_key="item_key");
    if handle == "rvread_file":
        return ReadFileTypes.fetch_list_labeled(replace_key="item_key");

    if handle == "host_disease_outcome":
        return misc.HostDiseaseOutcomes.fetch_list();

    return [];
