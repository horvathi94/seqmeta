/* Store fields and field information for the sample editors */

DROP TABLE IF EXISTS `fields`;

CREATE TABLE IF NOT EXISTS `fields` (

	handle VARCHAR(100) NOT NULL PRIMARY KEY,
	field_name VARCHAR(200),
	field_type VARCHAR(100),
	gisaid TINYINT UNSIGNED,
	ena TINYINT UNSIGNED,
	ncbi TINYINT UNSIGNED,
	db_key VARCHAR(100),
	class VARCHAR(100),
	min_val INT,
	max_val INT,
	step DECIMAL(5,3),
	min_date DATE,
	max_date DATE,
	prefix VARCHAR(100),
	description VARCHAR(2000),
	edit_all BIT(1) DEFAULT TRUE

);


INSERT INTO fields 
	(	`handle`,
		`field_name`, `field_type`, `gisaid`, `ena`, `ncbi`,
		`db_key`, `class`, `min_val`, `max_val`, `step`, `min_date`, `max_date`,
		`prefix`, 
		`description`)
	VALUES

	/* --- Basic sample data --- */
	
	("sample_name",
		"Sample name", "text", NULL, NULL, NULL,
		"sample_name", "sample-name", 0, 200, NULL, NULL, NULL,
		"sample",
		"Name of the sequenced files. Use this to keep track of your samples in the database."
	),
	("sample_comment",
		"Sample comment", "text", NULL, NULL, NULL,
		"sample_comment", "sample-comment", 0, 200, NULL, NULL, NULL,
		"sample",
		"A comment to more easily identify the sample. This will not be used for any of the uploads."
	),
	("sample_title",
		"Sample title", "text", NULL, 3, NULL,
		"sample_title", "sample-title", 0, 200, NULL, NULL, NULL,
		"sample",
		"A title for the sample."
	),
	("sample_description",
		"Sample description", "text", NULL, 2, NULL,
		"sample_description", "sample-description", 0, 200, NULL, NULL, NULL,
		"sample",
		"A short description of the sample."
	),
	("gisaid_accession",
		"GISAID accession", "text", NULL, NULL, 1,
		"gisaid_accession", "gisaid-accession", 0, 200, NULL, NULL, NULL,
		"sample",
		"The GISAID accession assigned to the sequence. GISAID Accession Numbers are used as unique and permanent identifiers for each virus beginning with the letters EPI and followed by numbers, to identify viruses and/or segments; https://www.gisaid.org/; <em>e.g., EPI_ISL_1091361.</em>"
	),
	("gisaid_virusname",
		"GISAID virusname", "text", 3, NULL, 1,
		"gisaid_virusname", "gisaid-virusname", 0, 300, NULL, NULL, NULL,
		"sample",
		"Leave this field empty to generate programatically."
	),
	("isolate",
		"Isolate name", "text", NULL, 3, 3,
		"isolate", "isolate-name", 0, 300, NULL, NULL, NULL,
		"sample",
		"Leave this field empty to generate programatically."
	),

	/* --- Collection data --- */
	("collection_year",
		"Collection year", "number", 3, 2, NULL,
		"collection_year", "collection-year", 2019, NULL, 1, NULL, NULL,
		"collection",
		"Collection date of the sample."
	),
	("collection_month",
		"Collection month", "number", 3, 2, NULL,
		"collection_month", "collection-month", 0, 12, 1, NULL, NULL,
		"collection",
		"Collection date of the sample."
	),
	("collection_day",
		"Collection day", "number", 3, 2, NULL,
		"collection_day", "collection-day", 0, 31, 1, NULL, NULL,
		"collection",
		"Collection date of the sample."
	),
	("collector_name",
		"Collector name", "select", NULL, 3, NULL,
		"collector_id", "collector-name", NULL, NULL, NULL, NULL, NULL,
		"collection",
		"Person who collected the sample."
	),
	("collection_device",
		"Collection device", "select", NULL, NULL, 1,
		"collection_device_id", "collection-device", NULL, NULL, NULL, NULL, NULL,
		"collection",
		"Instrument or container used to collect sample, <em>e.g., swab</em>."
	),


	/* --- Location data --- */
	("location_continent",
		"Continent", "select", 3, NULL, NULL,
		"continent_id", "continent", NULL, NULL, NULL, NULL, NULL,
		"location",
		"The geographical location of the sample as defined by the continent."
	),
	("location_country",
		"Country", "select", 3, NULL, NULL,
		"country_id", "country", NULL, NULL, NULL, NULL, NULL,
		"location",
		"The geographical origin of the sample as defined by the country or sea. 
ntry or sea names should be chosen from the <a target='_blank' href='http://insdc.org/country.html'>INSDC country list</a>"
	),
	("location_region",
		"Region", "text", 1, 2, NULL,
		"region", "region", NULL, 200, NULL, NULL, NULL,
		"location",
		"The geographical location of the sample as defined by the region."
	),
	("location_locality",
		"Locality", "text", 1, 2, NULL,
		"locality", "locality", NULL, 200, NULL, NULL, NULL,
		"location",
		"The geographical location of the sample as defined by the locality."
	),
	("additional_location_info",
		"Additional location information", "text", 1, NULL, NULL,
		"additional_location_info", "location-additional-info", NULL, 1000, NULL, NULL, NULL,
		"location",
		"<em> e.g. Cruise ship, Convention, Live animal market </em>"
	),
	("geo_loc_latitude",
		"Geographic location (latitude) (DD)", "number", NULL, 2, NULL,
		"geo_loc_latitude", "geo-loc-latitude", -90, 90, 0.01, NULL, NULL,
		"location",
		"The geographical origin of the sample as defined by the latitude. Minimum value: -90 and maximum value: 90."
	),
	("geo_loc_longitude",
		"Geographic location (longitude) (DD)", "number", NULL, 2, NULL,
		"geo_loc_longitude", "geo-loc-longitude", -180, 180, 0.01, NULL, NULL,
		"location",
		"The geographical origin of the sample as defined by the longitude. Minimum value: -180 and maximum value: 180."
	),

	/* --- Host information --- */
	("host",
		"Host", "select", 3, 3, 3,
		"host_id", "host", NULL, NULL, NULL, NULL, NULL,
		"host",
		"You can add more options in the <a target='_blank' href='/misc/edit'>manage options tab</a>"
	),
	("host_subject_id",
		"Host subject ID", "text", NULL, 3, 1,
		"host_subject_id", "host-subject-id", NULL, 200, NULL, NULL, NULL,
		"host",
		"A unique identifier by which each subject can be referred to, de-identified, <em>e.g. #131</em>"
	),
	("additional_host_info",
		"Additional host information", "text", 1, NULL, NULL,
		"additional_host_info", "additional-host-info", NULL, 200, NULL, NULL, NULL,
		"host",
		"<em> e.g. Patient infected while traveling in... </em>"
	),
	("patient_gender",
		"Patient gender", "radio", 3, 3, NULL,
		"patient_gender", "patient-gender", NULL, NULL, NULL, NULL, NULL,
		"host",
		"The gender of the host." 
	),
	("patient_age",
		"Patient age", "number", 3, 2, NULL,
		"patient_age", "patient-age", 0, 150, 1, NULL, NULL,
		"host",
		"The age of the host in years." 
	),
	("patient_status",
		"Patient status", "select", 3, NULL, NULL,
		"patient_status_id", "patient-status", NULL, NULL, NULL, NULL, NULL,
		"host",
		"The status of the host at collection time of the sample." 
	),
	("ppe",
		"Personal protective equipment", "text", NULL, 1, NULL,
		"ppe", "ppe", NULL, 600, NULL, NULL, NULL,
		"host",
		"Use of personal protective equipment, such as gloves, gowns, during any type of exposure. <em>Example: mask.</em>"
	),
	("host_habitat",
		"Host habitat", "select", NULL, 2, NULL,
		"host_habitat_id", "host-habitat-id", NULL, NULL, NULL, NULL, NULL,
		"host",
		"Natural habitat of the avian or mammalian host."
	),
	("host_behaviour",
		"Host behaviour", "select", NULL, 2, NULL,
		"host_behaviour_id", "host-behaviour-id", NULL, NULL, NULL, NULL, NULL,
		"host",
		"Natural behaviour of the host."
	),
	("host_description",
		"Host description", "text", NULL, 1, NULL,
		"host_description", "host-description", NULL, 1000, NULL, NULL, NULL,
		"host",
		"Other descriptive information relating to the host."
	),
	("host_gravidity",
		"Gravidity", "text", NULL, 1, NULL,
		"gravidity", "host-gravidity", NULL, 500, NULL, NULL, NULL,
		"host",
		"Whether or not the subject is gravid. If so, report date due or date post-conception and specify which of these two dates is being reported."
	),
	
	/* --- Patient treatment ---*/
	("prior_sars_cov_2_antiviral_treat",
		"Prior SARS-CoV-2 antiviral treatment", "radio", 1, NULL, 1,
		"prior_sars_cov_2_antiviral_treat", "prior-sars-cov-2-antiviral-treat", NULL, NULL, NULL, NULL, NULL,
		"treatment",
		"Has the host received SARS-CoV-2 antiviral treatment?" 
	),
	("antiviral_treatment_agent",
		"Prior SARS-CoV-2 antiviral treatment agent", "text", 1, NULL, 1,
		"antiviral_treatment_agent", "antiviral-treatment-agent", NULL, 200, NULL, NULL, NULL,
		"treatment",
		"What was the antiviral treatment agent?"
	),
	("date_of_prior_antiviral_treat",
		"Date of prior SARS-CoV-2 antiviral treatment", "date", 1, NULL, 1,
		"date_of_prior_antiviral_treat", "date-of-prior-antiviral-treat", NULL, NULL, NULL, "2019-01-01", NULL,
		"treatment",
		"Date of the SARS-CoV-2 antiviral treatment." 
	),
	("prior_sars_cov_2_infection",
		"Prior SARS-CoV-2 infection", "radio", NULL, NULL, 1,
		"prior_sars_cov_2_infection", "prior-sars-cov-2-infection", NULL, NULL, NULL, NULL, NULL,
		"treatment",
		"Did the host have a prior SARS-CoV-2 infection?" 
	),
	("date_of_prior_sars_cov_2_infection",
		"Date of prior SARS-CoV-2 infection", "date", NULL, NULL, 1,
		"date_of_prior_sars_cov_2_infection", "date-of-prior-sars-cov-2-infection", NULL, NULL, NULL, "2019-01-01", NULL,
		"treatment",
		"Date of the SARS-CoV-2 infection." 
	),
	("virus_isolate_of_prior_infection",
		"Virus isolate of prior infection", "text", NULL, NULL, 1,
		"virus_isolate_of_prior_infection", "virus-isolate-of-prior-infection", NULL, 200, NULL, NULL, NULL,
		"treatment",
		"Specific isolate of SARS-CoV-2 in prior infection (if known), <em>e.g., SARS-CoV-2/human/USA/CA-CDPH-001/2020 </em>." 
	),
	("prior_sars_cov_2_vaccination",
		"Prior SARS-CoV-2 vaccination", "select", NULL, NULL, 1,
		"prior_sars_cov_2_vaccination_id", "prior-sars-cov-2-vaccination-id", NULL, NULL, NULL, NULL, NULL,
		"treatment",
		"Has the host received a SARS-CoV-2 vaccination?" 
	),
	("vaccine_received",
		"Name of received SARS-CoV-2 vaccine", "text", NULL, NULL, 1,
		"vaccine_received", "vaccine-received", NULL, 100, NULL, NULL, NULL,
		"treatment",
		"Which vaccine did the host receive, e.g., Pfizer-BioNTech COVID-19 vaccine" 
	),
	("date_of_prior_sars_cov_2_vaccination",
		"Date of prior SARS-CoV-2 vaccination", "date", NULL, NULL, 1,
		"date_of_prior_sars_cov_2_vaccination", "date-of-prior-sars-cov-2-vaccination", NULL, NULL, NULL, "2019-01-01", NULL,
		"treatment",
		"Date of the 1st dose of the SARS-CoV-2 vaccine, <em>e.g., 2021-03-30</em>." 
	),

	/*--- Health status ---*/
	("subject_exposure",
		"Subject exposure", "text", NULL, 1, NULL,
		"subject_exposure", "subject-exposure", NULL, 600, NULL, NULL, NULL,
		"health",
		"Exposure of the subject to infected human or animals, such as poultry, wild bird or swine. 
		If multiple exposures are applicable, please state them separated by semicolon. <em>Example: poultry; wild bird. </em>"
	),
	("subject_exposure_duration",
		"Subject exposure duration", "text", NULL, 1, NULL,
		"subject_exposure_duration", "subject-exposure-duration", NULL, 600, NULL, NULL, NULL,
		"health",
		"Duration of the exposure of the subject to an infected human or animal. 
		If multiple exposures are applicable, please state their duration in the same order in which you reported the exposure in the field 'subject exposure'. 
		<em>Example: 1 day; 0.33 days.</em>"
	),
	("type_exposure",
		"Type exposure", "text", NULL, 1, NULL,
		"type_exposure", "type-exposure", NULL, 600, NULL, NULL, NULL,
		"health",
		"Setting within which the subject is exposed to animals, such as farm, slaughterhouse, food preparation. If multiple exposures are applicable, please state their type in the same order in which you reported the exposure in the field 'subject exposure'. 
		<em>Example: backyard flock; confined animal feeding operation</em>"
	),
	("outbreak",
		"Outbreak", "text", 1, NULL, NULL,
		"outbreak", "outbreak", NULL, 200, NULL, NULL, NULL,
		"health",
		"Date, location <em> e.g. type of gathering, family cluster etc. </em>"
	),
	("host_health_state",
		"Host health state", "select", NULL, 3, NULL,
		"host_health_state_id", "host-health-state", NULL, NULL, NULL, NULL, NULL,
		"health",
		"Health status of the host at the time of sample collection."
	),
	("hospitalisation",
		"Hospitalisation", "radio", NULL, 1, NULL,
		"hospitalization", "hospitalisation", NULL, NULL, NULL, NULL, NULL,
		"health",
		"Was the subject confined to a hospital as a result of virus infection or problems occurring secondary to virus infection?"
	),
	("ilness_symptoms",
		"Ilness symptoms", "text", NULL, 1, NULL,
		"ilness_symptoms", "ilness-symptoms", NULL, 600, NULL, NULL, NULL,
		"health",
		"The symptoms that have been reported in relation to the illness, such as cough, diarrhea, fever, headache, malaise, myalgia, nausea, runny_nose, shortness_of_breath, sore_throat. If multiple exposures are applicable, please state them separated by semicolon."
	),
	("ilness_duration",
		"Ilness duration", "number", NULL, 1, NULL,
		"ilness_duration", "ilness-duration", 0, NULL, NULL, NULL, NULL,
		"health",
		"The number of days the illness lasted. <em>Example: 4</em>."
	),
	("host_disease_outcome",
		"Host disease outcome", "select", 1, NULL, NULL,
		"host_disease_outcome_id", "ilness-disease-outcome", NULL, NULL, NULL, NULL, NULL,
		"health",
		"Disease outcome in the host."
	),
	("sars_cov_2_diag_gene_name_1",
		"Name of the gene used in the first diagnostic SARS-CoV-2 RT-PCR test", "select", NULL, NULL, 1,
		"sars_cov_2_diag_gene_name_1_id", "sars-cov-2-diag-gene-name-1", NULL, NULL, NULL, NULL, NULL,
		"health",
		"The name of the gene used in the first diagnostic SARS-CoV-2 RT-PCR test."
	),
	("sars_cov_2_diag_pcr_ct_value_1",
		"The cycle treshold of the first diagnostic SARS-CoV-2 RT-PCR test", "number", NULL, NULL, 1,
		"sars_cov_2_diag_pcr_ct_value_1", "sars-cov-2-diag-pcr-ct-value-1", 0, 45, 1, NULL, NULL,
		"health",
		"The cycle threshold (CT) value result from the first diagnostic SARS-CoV-2 RT-PCR test, <em>e.g., 21</em>"
	),
	("sars_cov_2_diag_gene_name_2",
		"Name of the gene used in the second diagnostic SARS-CoV-2 RT-PCR test", "select", NULL, NULL, 1,
		"sars_cov_2_diag_gene_name_2_id", "sars-cov-2-diag-gene-name-2", NULL, NULL, NULL, NULL, NULL,
		"health",
		"The name of the gene used in the second diagnostic SARS-CoV-2 RT-PCR test."
	),
	("sars_cov_2_diag_pcr_ct_value_2",
		"The cycle treshold of the second diagnostic SARS-CoV-2 RT-PCR test", "number", NULL, NULL, 1,
		"sars_cov_2_diag_pcr_ct_value_2", "sars-cov-2-diag-pcr-ct-value-2", 0, 45, 1, NULL, NULL,
		"health",
		"The cycle threshold (CT) value result from the second diagnostic SARS-CoV-2 RT-PCR test, <em>e.g., 36</em>"
	),


	/* --- Collection --- */
	("originating_lab",
		"Originating lab", "select", 3, NULL, NULL,
		"originating_lab_id", "originating-lab", NULL, NULL, NULL, NULL, NULL,
		"collection",
		"Where the clinical specimen or virus isolate was first obtained."
	),
	("submitting_lab",
		"Submitting lab", "select", 3, NULL, NULL,
		"submitting_lab_id", "submitting-lab", NULL, NULL, NULL, NULL, NULL,
		"collection",
		"Where the sequence data have been generated and submitted to GISAID."
	),
	("originating_lab_sample_name",
		"Sample ID given by the originating lab", "text", 1, NULL, NULL,
		"originating_lab_sample_name", "originating-lab-sample-name", NULL, 200, NULL, NULL, NULL,
		"collection",
		""
	),
	("submitting_lab_sample_name",
		"Sample ID given by the submitting lab", "text", 1, NULL, NULL,
		"submitting_lab_sample_name", "submitting-lab-sample-name", NULL, 200, NULL, NULL, NULL,
		"collection",
		""
	),
	("author_group",
		"Author group", "select", 3, NULL, NULL,
		"author_group_id", "author-group", NULL, NULL, NULL, NULL, NULL,
		"collection",
		"Create and edit author groups <a href='/author-groups/view'>here</a>"
	),


	/*--- Sampling ---*/
	("sampling_strategy",
		"Sampling strategy", "select", 1, NULL, NULL,
		"sampling_strategy_id", "sampling-strategy", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"The sampling strategy used to select the sample. 
		Edit and add options <a href='/misc/edit/#specimen-sources-editor' target='_blank'>here</a>"
	),
	("strain",
		"Strain", "text", NULL, 1, NULL,
		"strain", "strain", NULL, 500, NULL, NULL, NULL,
		"sampling",
		"Name of the strain from which the sample was obtained."
	),
	("isolation_source_host_associated",
		"Isolation source host-associated", "text", NULL, 1, NULL,
		"isolation_source_host_associated", "isolation-source-host-associated", NULL, 600, NULL, NULL, NULL,
		"sampling",
		"Name of host tissue or organ sampled for analysis. <em>Example: tracheal tissue</em>"
	),
	("isolation_source_non_host_associated",
		"Isolation source non-host-associated", "text", NULL, 1, 3,
		"isolation_source_non_host_associated", "isolation-source-non-host-associated", NULL, 600, NULL, NULL, NULL,
		"sampling",
		"Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived. <em>Example: soil</em>"
	),
	("sample_capture_status",
		"Sample capture status", "select", NULL, 2, NULL,
		"sample_capture_status_id", "sample-capture-status", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"Reason for the sample collection."
	),
	("specimen_source",
		"Specimen source", "select", 1, NULL, NULL,
		"specimen_source_id", "specimen-source", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"Source of the specimen."
	),
	("sample_storage_conditions",
		"Sample storage conditions", "text", NULL, 1, NULL,
		"sample_storage_conditions", "sample-storage-conditions", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"Conditions at which sample was stored, usually storage temperature, duration and location."
	),
	("passage_method",
		"Passage method", "text", 1, NULL, 1,
		"passage_method", "passage-method", NULL, 200, NULL, NULL, NULL,
		"sampling",
		"Description of how the organism was passaged. Provide a short description, <em>e.g., AVL buffer+30%EtOH lysate received from Respiratory Lab. P3 passage in Vero-1 via bioreactor large-scale batch passage. P3 batch derived from the SP-2/reference lab strain. </em>If not passaged, put 'not applicable'."
	),
	("passage_number",
		"Passage number", "number", 3, NULL, 1,
		"passage_number", "passage-number", 0, 200, 1, NULL, NULL,
		"sampling",
		"The number of known passages, e.g., 3. For origianl passsage use: 0."
	),
	("definition_for_seropositive_sample",
		"Definition for seropositive sample", "text", NULL, 2, NULL,
		"definition_for_seropositive_sample", "definition_for_seropositive_sample", NULL, 500, NULL, NULL, NULL,
		"sampling",
		"The cut off value used by an investigatior in determining that a sample was seropositive."
	),
	("serotype",
		"Serotype (<em>required for a seropositive sample</em>)", "text", NULL, 2, NULL,
		"serotype", "serotype", NULL, 500, NULL, NULL, NULL,
		"sampling",
		"Serological variety of a species characterised by its antigenic properties. For Influenza, HA subtype should be the letter H followed by a number between 1-16 unless novel subtype is identified and the NA subtype should be the letter N followed by a number between 1-9 unless novel subtype is identified. If only one of the subtypes have been tested then use the format H5Nx or HxN1. <em>Example: H1N1.</em>"
	),


	/* --- Sequencing --- */
	("sequencing_instrument",
		"Sequencing instrument", "select", 3, 3, 3,
		"sequencing_instrument_id", "sequencing-instrument", NULL, NULL, NULL, NULL, NULL,
		"sequencing",
		"Apparatus with which the sequencing was done."
	),
	("coverage",
		"Coverage", "number", 1, NULL, NULL,
		"coverage", "coverage", 0, NULL, 1, NULL, NULL,
		"sequencing",
		"The average coverage of the sample."
	),
	

	/* --- Library --- */
	("library_id",
		"Library ID", "text", NULL, NULL, 3,
		"library_id", "library-id", NULL, 200, NULL, NULL, NULL,
		"library",
		"Short unique identifier for the sequencing library. Each library ID must be unique."
	),
	("library_layout",
		"Library layout", "radio", NULL, NULL, 3,
		"library_layout_paired", "library-layout", NULL, NULL, NULL, NULL, NULL,
		"library",
		"Paired-end or Single."
	),
	("library_source",
		"Library source", "select", NULL, NULL, 3,
		"library_source_id", "library-source", NULL, NULL, NULL, NULL, NULL,
		"library",
		"Detailed description can be found <a href='/descriptions/library#library-sources' target='_blank'>here</a>"
	),
	("library_strategy",
		"Library strategy", "select", NULL, NULL, 3,
		"library_strategy_id", "library-strategy", NULL, NULL, NULL, NULL, NULL,
		"library",
		"Detailed description can be found <a href='/descriptions/library#library-strategies' target='_blank'>here</a>"
	),
	("library_selection",
		"Library selection", "select", NULL, NULL, 3,
		"library_selection_id", "library-selection", NULL, NULL, NULL, NULL, NULL,
		"library",
		"Detailed description can be found <a href='/descriptions/library#library-selections'	target='_blank'>here</a>"
	),
	("library_preparation_date",
		"Library preparation date", "date", NULL, 1, NULL,
		"library_preparation_date", "library-preparation-date", NULL, NULL, NULL, "2019-01-01", NULL,
		"library",
		"Date when the library was prepared."
	),
	("library_design_description",
		"Library design description", "text", NULL, NULL, 3,
		"library_design_description", "library-design-description", NULL, 1000, NULL, NULL, NULL,
		"library",
		"Free-form description of the methods used to create the sequencing library a brief 'material and methods' section."
	),
	("insert_size",
		"Insert size", "number", NULL, NULL, 1,
		"insert_size", "insert-size", 0, NULL, 1, NULL, NULL,
		"library",
		"The insert size of the library."
	),
	("library_construction_protocol",
		"Library construction protocol", "text", NULL, NULL, 1,
		"library_construction_protocol", "library-construction-protocol", NULL, 500, NULL, NULL, NULL,
		"library",
		"Describes the protocol by which the sequencing library was constructed."
	),


	/* --- Host extra --- */
	("host_recent_travel_loc",
		"Host recent travel loc", "text", NULL, NULL, 1,
		"host_recent_travel_loc", "host-recent-travel-loc", NULL, 500, NULL, NULL, NULL,
		"host",
		"The name of the country that was the destination of most recent travel. Specify the countries (and more granular locations if known) travelled, <em>e.g., United Kingdom </em>. Can include multiple travels; separate multiple travel events with a semicolon."
	),
	("host_recent_travel_return_date",
		"Host recent travel return date", "date", NULL, NULL, 1,
		"host_recent_travel_return_date", "host-recent-travel-return-date", NULL, NULL, NULL, "2019-01-01", NULL,
		"host",
		"The date of a person's most recent return to some residence from a journey originating at that residence, <em>e.g., 2021-03-30</em>"
	),


	/* --- Location extra --- */
	("geo_loc_exposure",
		"Country of exposure", "select", NULL, NULL, 1,
		"geo_loc_exposure_id", "geo-loc-exposure", NULL, NULL, NULL, NULL, NULL,
		"location",
		"The country where the host was likely exposed to the causative agent of the illness. This location pertains to the country the host was believed to be exposed, and may not be the same as the host's country of residence, <em>e.g., Canada</em>"
	),


	/* --- Sequencing extra --- */
	("sequencing_lab",
		"Sequencing lab", "select", NULL, NULL, 1,
		"sequencing_lab_id", "sequencing-lab", NULL, NULL, NULL, NULL, NULL,
		"sequencing",
		"The name of the agency that generated the sequence, <em>e.g., Centers for Disease Control and Prevention</em>."
	),


	/* --- Sampling extra --- */
	("host_anatomical_material",
		"Host anatomical material", "select", NULL, NULL, 1,
		"host_anatomical_material_id", "host-anatomical-material", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"Host anatomical material or substance produced by the body where the sample was obtained, <em>e.g., stool, mucus, saliva</em>"
	),
	("host_body_product",
		"Host body product", "select", NULL, NULL, 1,
		"host_body_product_id", "host-body-product", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"Substance produced by the host, <em>e.g. stool, mucus</em>, where the sample was obtained from	"
	),
	("purpose_of_sampling",
		"Purpose of sampling", "select", NULL, NULL, 1,
		"purpose_of_sampling_id", "purpose-of-sampling", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"The reason the sample was collected, <em>e.g., diagnostic testing</em>"
	),
	("purpose_of_sequencing",
		"Purpose of sequencing", "select", NULL, NULL, 1,
		"purpose_of_sequencing_id", "purpose-of-sequencing", NULL, NULL, NULL, NULL, NULL,
		"sampling",
		"The reason the sample was sequenced, <em>e.g., baseline surveillance (random sampling)</em>"
	),



	("assembly_file",
		"Consensus sequence file", "seqfile", 3, 1, 1,
		"assembly_file", "assembly-file", NULL, NULL, NULL, NULL, NULL,
		"seqfile",
		"Consensus sequence file."
	),
	("contigs_file",
		"Contigs assembly file", "seqfile", NULL, 1, 1,
		"contigs_file", "contigs-file", NULL, NULL, NULL, NULL, NULL,
		"seqfile",
		"Contigs assembly file."
	),
	("scaffolds_file",
		"Scaffolds assembly file", "seqfile", NULL, 1, 1,
		"scaffolds_file", "scaffolds-file", NULL, NULL, NULL, NULL, NULL,
		"seqfile",
		"Scaffolds assembly file."
	),
	("fwread_file",
		"Forward read", "seqfile", NULL, 1, 1,
		"fwread_file", "fwread-file", NULL, NULL, NULL, NULL, NULL,
		"seqfile",
		"Forward read file (the first one the machine returns)."
	),
	("rvread_file",
		"Reverse read", "seqfile", NULL, 1, 1,
		"rvread_file", "rvread-file", NULL, NULL, NULL, NULL, NULL,
		"seqfile",
		"Reverse read file (the second one the machine returns)."
	),
	("consensus_assembly_method",
		"Consensus sequence assembly method", "seqfile_assembly", 3, 1, 1,
		"assembly_file", "consensus-assembly-method", NULL, NULL, NULL, NULL, NULL,
		"seqfile_assembly",
		"Consensus sequence assembly method."
	),
	("contigs_assembly_method",
		"Contigs assembly assembly method", "seqfile_assembly", NULL, 1, 1,
		"contigs_file", "contigs-assembly-method", NULL, NULL, NULL, NULL, NULL,
		"seqfile_assembly",
		"Contigs assembly assembly method."
	),
	("scaffolds_assembly_method",
		"Scaffolds assembly assembly method", "seqfile_assembly", NULL, 1, 1,
		"scaffolds_file", "scaffolds-assembly-method", NULL, NULL, NULL, NULL, NULL,
		"seqfile_assembly",
		"Scaffolds assembly assembly_method."
	)



;

UPDATE `fields` 
	SET `edit_all` = FALSE
	WHERE `handle` = "sample_name";

UPDATE `fields` 
	SET `edit_all` = FALSE
	WHERE `handle` = "library_id";


