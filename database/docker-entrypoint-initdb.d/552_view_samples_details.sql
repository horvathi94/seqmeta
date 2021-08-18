CREATE OR REPLACE VIEW view_samples_details AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		samples.sample_comment AS sample_comment,
		CONCAT(samples.gisaid_virusname, " (accession: ",
				IF (samples.gisaid_accession IS NULL, "N/A", samples.gisaid_accession),
		")") AS gisaid_details,
		samples.isolate AS isolate,
	
		CONCAT(location.location,
			IF (location.geo_loc_latitude IS NULL OR location.geo_loc_longitude IS NULL, "",
					CONCAT(" (", location.geo_loc_latitude, "DD, ", location.geo_loc_longitude, "DD)")
				)
			) AS location_details,


		coll.collection_date AS collection_date,
		IF (coll.collector_abbreviated_middle_name IS NULL, "not provided",
			coll.collector_abbreviated_middle_name) AS collector_name, 

		library.library_id AS library_id,

		CONCAT(library.library_layout, 
			", strategy: ", library.library_strategy,
			", source: ", library.library_source,
			", selection: ", library.library_selection
		) AS library_details,


		CONCAT(
			host.host_subject_id, ": ",
			host.host_name, " ",
			host.patient_gender, ", ",
			IF (host.patient_age IS NULL, "", CONCAT(host.patient_age, " years old")),
			IF (host.patient_status IS NULL, "", CONCAT(" (", host.patient_status, ")"))
		) AS patient_details,
		host.host_gravidity AS host_gravidity,


		IF (treatment.vaccine_received = ""AND treatment.date_of_prior_sars_cov_2_vaccination IS NULL, "N/A", 
			CONCAT_WS(treatment.vaccine_received, ", ", treatment.prior_sars_cov_2_vaccination,
				" (", treatment.date_of_prior_sars_cov_2_vaccination, ")")
		) AS vaccination_details,


		CONCAT(coll.originating_lab_name, " (", coll.originating_lab_sample_name, ")") AS originating_lab_details,
		CONCAT(coll.submitting_lab_name, " (", coll.submitting_lab_sample_name, ")") AS submitting_lab_details,
		CONCAT(coll.author_group_name, " (", coll.authors_list, ")") AS authors_details,

		IF (health.ilness_symptoms = "" AND health.ilness_duration_days = "", "N/A", 
			CONCAT(health.ilness_symptoms, 
				IF (health.ilness_duration_days = "", "",
					CONCAT(", ", health.ilness_duration_days)
				)
			)
		) AS ilness_details,

		IF (treatment.prior_sars_cov_2_antiviral_treat = "", "N/A",
			IF (treatment.prior_sars_cov_2_antiviral_treat = "no", "No treatment",
				treatment.antiviral_treatment_agent
				)
			) AS antiviral_treatment_details,
		

		IF (treatment.prior_sars_cov_2_infection = "", "N/A",
			IF (treatment.prior_sars_cov_2_infection = "no", "No prior infection",
				CONCAT("Yes, virus isolate: ",
					IF (treatment.virus_isolate_of_prior_infection = "", "N/A", treatment.virus_isolate_of_prior_infection),
					IF(treatment.date_of_prior_sars_cov_2_infection IS NULL, "", 
						CONCAT(" on: ", treatment.date_of_prior_sars_cov_2_infection)
					)
				)
			)
		) AS prior_infection_details,
		

		sampling.sampling_strategy AS sampling_strategy,
		sampling.purpose_of_sampling AS purpose_of_sampling,
		sampling.purpose_of_sequencing AS purpose_of_sequencing,
		health.hospitalization AS hospitalization,
		health.host_disease_outcome AS host_disease_outcome,


		CONCAT(sequencing.sequencing_instrument, " (",
				sequencing.sequencing_platform, ")") AS instrument_details,
		sequencing.assembly_method AS assembly_method,
		sequencing.coverage AS coverage


	FROM view_samples_base AS samples
	LEFT JOIN view_samples_location AS location
		ON samples.sample_id = location.sample_id
	LEFT JOIN view_samples_collection AS coll
		ON samples.sample_id = coll.sample_id
	LEFT JOIN view_samples_library AS library
		ON samples.sample_id = library.sample_id
	LEFT JOIN view_samples_host AS host
		ON samples.sample_id = host.sample_id
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id
	LEFT JOIN view_samples_health_status AS health
		ON samples.sample_id = health.sample_id
	LEFT JOIN view_samples_sequencing AS sequencing
		ON samples.sample_id = sequencing.sample_id
	LEFT JOIN view_samples_patient_treatment AS treatment
		ON samples.sample_id = treatment.sample_id
