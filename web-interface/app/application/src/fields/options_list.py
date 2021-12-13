from .sample_fields import SampleFields as SF
from application.src.authors import Authors, AuthorGroups
from application.src.institutions import Institutions
from application.src.misc import sampling, sequencing, location, \
    health, library, host
from application.src.seqfiles.db import AssemblyFileTypes, ReadFileTypes


_OPTIONS_LIST = {

    SF.COLLECTOR_NAME: Authors.fetch_select_list,
    SF.COLLECTION_DEVICE: sampling.CollectionDevices.fetch_list,
    SF.LOCATION_CONTINENT: location.Continents.fetch_list,
    SF.LOCATION_COUNTRY: location.Countries.fetch_list,
    SF.GEOLOC_EXPOSURE: location.Countries.fetch_list,
    SF.HOST: host.Hosts.fetch_list,
    SF.HOST_GENDER: host.Genders.get_list,
    SF.HOST_STATUS: health.PatientStatuses.fetch_list,
    SF.HOST_HABITAT: host.HostHabitats.fetch_list,
    SF.HOST_BEHAVIOUR: host.HostBehaviours.fetch_list,
    SF.HOST_ANATOMICAL_MATERIAL: \
        sampling.HostAnatomicalMaterials.fetch_list,
    SF.HOST_BODY_PRODUCT: sampling.HostBodyProducts.fetch_list,
    SF.PRIOR_SARS_COV_2_ANTIVIRAL_TREATMENT: \
        health.ReceivedTreatment.get_list,
    SF.PRIOR_SARS_COV_2_INFECTION: health.PriorInfection.get_list,
    SF.PRIOR_SARS_COV_2_VACCINATION: health.HasVaccine.fetch_list,
    SF.HOST_HEALTH_STATUS: health.HostHealthStates.fetch_list,
    SF.HOSPITALISATION: health.Hospitalisation.get_list,
    SF.HOST_DISEASE_OUTCOME: health.HostDiseaseOutcomes.fetch_list,
    SF.SARS_COV_2_DIAG_GENE_NAME_1: sequencing.SarsCovGenes.fetch_list,
    SF.SARS_COV_2_DIAG_GENE_NAME_2: sequencing.SarsCovGenes.fetch_list,
    SF.ORIGINATING_LAB: Institutions.fetch_list_labeled,
    SF.SEQUENCING_LAB: Institutions.fetch_list_labeled,
    SF.SUBMITTING_LAB: Institutions.fetch_list_labeled,
    SF.AUTHOR_GROUP: AuthorGroups.fetch_select_list,
    SF.SAMPLING_STRATEGY: sampling.SamplingStrategies.fetch_list,
    SF.PURPOSE_OF_SAMPLING: sampling.PurposesOfSampling.fetch_list,
    SF.PURPOSE_OF_SEQUENCING: sampling.PurposesOfSequencing.fetch_list,
    SF.SAMPLE_CAPTURE_STATUS: sampling.SampleCaptureStatuses.fetch_list,
    SF.SPECIMEN_SOURCE: sampling.SpecimenSources.fetch_list,
    SF.SEQUENCING_INSTRUMENT: sequencing.SequencingInstruments.fetch_list,
    SF.LIBRARY_LAYOUT: library.LibraryLayouts.get_list,
    SF.LIBRARY_SOURCE: library.LibrarySources.fetch_select_list,
    SF.LIBRARY_SELECTION: library.LibrarySelections.fetch_select_list,
    SF.LIBRARY_STRATEGY: library.LibraryStrategies.fetch_select_list,

    SF.CONSENSUS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.CONSENSUS_ASSEMBLY_METHOD: sequencing.AssemblyMethods.fetch_list,
    SF.CONTIGS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.CONTIGS_ASSEMBLY_METHOD: sequencing.AssemblyMethods.fetch_list,
    SF.SCAFFOLDS_FILE: AssemblyFileTypes.fetch_select_list,
    SF.SCAFFOLDS_ASSEMBLY_METHOD: sequencing.AssemblyMethods.fetch_list,
    SF.FORWARD_READ_FILE: ReadFileTypes.fetch_select_list,
    SF.REVERSE_READ_FILE: ReadFileTypes.fetch_select_list,

}



