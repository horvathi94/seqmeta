DROP TABLE IF EXISTS fields;

CREATE TABLE IF NOT EXISTS fields (

	handle				VARCHAR(100) NOT NULL PRIMARY KEY,

	field_name		VARCHAR(200),
	field_type		VARCHAR(100),
	gisaid				TINYINT UNSIGNED,
	ena						TINYINT UNSIGNED,
	ncbi					TINYINT UNSIGNED,
	
	db_key				VARCHAR(100),
	class					VARCHAR(100),
	min_val				INT,
	max_val				INT,
	step					DECIMAL(5,3),
	min_date			DATE,
	max_date			DATE,

	prefix				VARCHAR(100),

	description		VARCHAR(2000)

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
		"sample_description", "sample-description", 0, 200, 1, NULL, NULL,
		"sample",
		"A short description of the sample."
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
		"Additional location informatio", "text", 1, NULL, NULL,
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
		"Prior SARS-CoV-2 antiviral tretment", "radio", 1, NULL, 1,
		"prior_sars_cov_2_antiviral_treat", "prior-sars-cov-2-antiviral-treat", NULL, NULL, NULL, NULL, NULL,
		"treatment",
		"Has the host received SARS-CoV-2 antiviral treatment?" 
	),
	("date_of_prior_antiviral_treat",
		"Date of prior SARS-CoV-2 antiviral tretment", "date", 1, NULL, 1,
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
		"Received SARS-CoV-2 vaccine", "text", NULL, NULL, 1,
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
		"Setting within which the subject is exposed to animals, such as farm, slaughterhouse, food preparation. 
		If multiple exposures are applicable, please state their type in the same order in which you reported the exposure in the field 'subject exposure'. 
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
		"sars_cov_2_diag_pcr_ct_value_1", "sars-cov-2-diag-pcr-ct-value-1", NULL, 45, 1, NULL, NULL,
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
		"sars_cov_2_diag_pcr_ct_value_2", "sars-cov-2-diag-pcr-ct-value-2", NULL, 45, 1, NULL, NULL,
		"health",
		"The cycle threshold (CT) value result from the second diagnostic SARS-CoV-2 RT-PCR test, <em>e.g., 36</em>"
	)


;
