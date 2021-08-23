from .sample_fields import SampleFields as SF
from application.src.authors import Authors, AuthorGroups
from application.src.institutions import Institutions
from application.src import misc
from application.src import library as lib
from application.src.seqfiles.db import AssemblyFileTypes, ReadFileTypes


_OPTIONS_LIST = {

    SF.COLLECTOR_NAME: Authors.fetch_select_list,
    SF.COLLECTION_DEVICE: misc.CollectionDevices.fetch_list,
    SF.LOCATION_CONTINENT: misc.Continents.fetch_list,
    SF.LOCATION_COUNTRY: misc.Countries.fetch_list,
    SF.GEOLOC_EXPOSURE: misc.Countries.fetch_list,
    SF.HOST: misc.Hosts.fetch_list,
    SF.HOST_GENDER: misc.Genders.get_list,
    SF.HOST_STATUS: misc.PatientStatuses.fetch_list,
    SF.HOST_HABITAT: misc.HostHabitats.fetch_list,
    SF.HOST_BEHAVIOUR: misc.HostBehaviours.fetch_list,
    SF.HOST_ANATOMICAL_MATERIAL: misc.HostAnatomicalMaterials.fetch_list,
    SF.HOST_BODY_PRODUCT: misc.HostBodyProducts.fetch_list,
    SF.PRIOR_SARS_COV_2_ANTIVIRAL_TREATMENT: misc.ReceivedTreatment.get_list,
    SF.PRIOR_SARS_COV_2_INFECTION: misc.PriorInfection.get_list,
    SF.PRIOR_SARS_COV_2_VACCINATION: misc.HasVaccine.fetch_list,
    SF.HOST_HEALTH_STATUS: misc.HostHealthStates.fetch_list,
    SF.HOSPITALISATION: misc.Hospitalisation.get_list,
    SF.HOST_DISEASE_OUTCOME: misc.HostDiseaseOutcomes.fetch_list,
    SF.SARS_COV_2_DIAG_GENE_NAME_1: misc.SarsCovGenes.fetch_list,
    SF.SARS_COV_2_DIAG_GENE_NAME_2: misc.SarsCovGenes.fetch_list,
    SF.ORIGINATING_LAB: Institutions.fetch_list_labeled,
    SF.SEQUENCING_LAB: Institutions.fetch_list_labeled,
    SF.SUBMITTING_LAB: Institutions.fetch_list_labeled,
    SF.AUTHOR_GROUP: AuthorGroups.fetch_select_list,
    SF.SAMPLING_STRATEGY: misc.SamplingStrategies.fetch_list,
    SF.PURPOSE_OF_SAMPLING: misc.PurposesOfSampling.fetch_list,
    SF.PURPOSE_OF_SEQUENCING: misc.PurposesOfSequencing.fetch_list,
    SF.SAMPLE_CAPTURE_STATUS: misc.SampleCaptureStatuses.fetch_list,
    SF.SPECIMEN_SOURCE: misc.SpecimenSources.fetch_list,
    SF.SEQUENCING_INSTRUMENT: misc.SequencingInstruments.fetch_list,
    SF.ASSEMBLY_METHOD: misc.AssemblyMethods.fetch_list,
    SF.LIBRARY_LAYOUT: misc.LibraryLayouts.get_list,
    SF.LIBRARY_SOURCE: lib.LibrarySources.fetch_select_list,
    SF.LIBRARY_SELECTION: lib.LibrarySelections.fetch_select_list,
    SF.LIBRARY_STRATEGY: lib.LibraryStrategies.fetch_select_list,

    SF.CONSENSUS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.CONTIGS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.SCAFFOLDS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.FORWARD_READ_FILE: ReadFileTypes.fetch_select_list,
    SF.REVERSE_READ_FILE: ReadFileTypes.fetch_select_list,

};



