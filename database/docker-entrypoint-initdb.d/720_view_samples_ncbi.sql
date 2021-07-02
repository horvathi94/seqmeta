CREATE OR REPLACE VIEW `view_samples_ncbi` AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
		samples.sample_title AS sample_title,
		"SARS-CoV-2" AS organism,
		collection.collector_abbreviated_middle_name AS collected_by,
		collection.collection_date AS collection_date,
		CONCAT(location.continent, 
			IF (location.region IS NULL, "",
				CONCAT(": ", location.region,
					IF (location.locality IS NULL, "", 
					 CONCAT(", ", location.locality))
				) 
			)
		) AS geo_loc_name,
		hosts.host_scientific_name AS host,
		"COVID-19" AS host_disease,
		sampling.isolation_source_non_host_associated AS isolation_source,
		treatment.antiviral_treatment_agent AS antiviral_treatment_agent,
		collection.collection_device AS collection_device,
		sampling.specimen_source AS collection_method,
		treatment.date_of_prior_sars_cov_2_infection AS date_of_prior_sars_cov_2_infection,
		treatment.date_of_prior_sars_cov_2_vaccination AS date_of_sars_cov_2_vaccination,
		health.outbreak AS exposure_evenet,
		"geo_loc_exposure" AS geo_loc_exposure,
		samples.gisaid_accession AS gisaid_accession,
		CONCAT(hosts.patient_age, " years") AS host_age,
		"host_anatomical_material" AS host_anatomical_material,
		sampling.isolation_source_host_associated AS host_anatomical_part,
		"host_body_product" AS host_body_product,
		health.host_disease_outcome AS host_disease_outcome,
		health.host_health_state AS host_health_state,
		"host_recent_travel_loc" AS host_recent_travel_loc,
		"host_recent_travel_return_date" AS host_recent_travel_return_date,
		hosts.patient_gender_ncbi AS host_sex,
		"host_specimen_voucher" AS host_specimen_voucher,
		hosts.host_subject_id AS host_subject_id,
		IF ( 
			location.geo_loc_latitude = "" OR location.geo_loc_longitude = "", "",
			CONCAT(
				ABS(location.geo_loc_latitude),
				IF(SIGN(location.geo_loc_latitude) = 1, " N ", " S "),
				ABS(location.geo_loc_longitude),
				IF(SIGN(location.geo_loc_longitude) = 1, " W", " E")
			)
		) AS lat_lon,
		sampling.passage_method AS passage_method,
		sampling.passage_number AS passage_number,
		treatment.prior_sars_cov_2_antiviral_treat AS prior_sars_cov_2_antiviral_treat,
		treatment.prior_sars_cov_2_infection AS prior_sars_cov_2_infection,
		treatment.prior_sars_cov_2_vaccination AS prior_sars_cov_2_vaccination,
		"purpose_of_sampling" AS purpose_of_sampling,
		"purpose_of_sequencing" AS purpose_of_sequencing,
		health.sars_cov_2_diag_gene_name_1 AS sars_cov_2_diag_gene_name_1,
		health.sars_cov_2_diag_pcr_ct_value_1 AS sars_cov_2_diag_pcr_ct_value_1,
		health.sars_cov_2_diag_gene_name_2 AS sars_cov_2_diag_gene_name_2,
		health.sars_cov_2_diag_pcr_ct_value_2 AS sars_cov_2_diag_pcr_ct_value_2,
		"sequenced_by" AS sequenced_by,
		treatment.vaccine_received AS vaccine_received,
		treatment.virus_isolate_of_prior_infection AS virus_isolate_of_prior_infection,
		samples.sample_description AS description



	FROM view_samples_base AS samples
	LEFT JOIN view_samples_host AS hosts
		ON samples.sample_id = hosts.sample_id
	LEFT JOIN view_samples_collection AS collection
		ON samples.sample_id = collection.sample_id
	LEFT JOIN view_samples_location AS location
		ON samples.sample_id = location.sample_id
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id
	LEFT JOIN view_samples_health_status AS health
		ON samples.sample_id = health.sample_id
	LEFT JOIN view_samples_patient_treatment AS treatment
		ON samples.sample_id = treatment.sample_id
