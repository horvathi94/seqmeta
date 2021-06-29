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
				CONCAT(": " location.region,
					IF (location.locality IS NULL, "", 
					 ", ", location.locality)
				) 
			)
		) AS geo_loc_name,
		hosts.scientific_name AS host,
		"COVID-19" AS host_disease,
		sampling.isolation_source_non_host_assiociated AS isolation_source,
		health.treatment AS antiviral_treatment_agent,
		collection.collection_device AS collection_device,
		sampling.specimen_source AS collection_method,
		"date_of_prior_sars_cov_2_infection" AS date_of_prior_sars_cov_2_infection,
		"date_of_sars_cov_2_vaccination" AS date_of_sars_cov_2_vaccination,
		health.outbreak AS exposure_evenet
		"geo_loc_exposure" AS geo_loc_exposure,
		"gisaid_accession" AS gisaid_accession,
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
			location.geo_loc_latitdue = "" OR location.geo_loc_longitude = "", "",
			CONCAT(
				ABS(location.geo_loc_latitude),
				IF(SIGN(location.geo_loc_latitdue) = 1, " N ", " S "),
				ABS(location.geo_loc_longitude),
				IF(SIGN(location.geo_loc_longitude) = 1, " W", " E")
			)
		) AS lat_lon,
		"passage_method" AS passage_method,
		"passage_number" AS passage_number,
		"prior_sars_cov_2_antiviral_treatment" AS prior_sars_cov_2_antiviral_treatment,
		"prior_sars_cov_2_infection" AS prior_sars_cov_2_infection,
		"prior_sars_cov_2vaccination" AS prior_sars_cov_2_vaccination,
		"purpose_of_sampling" AS purpose_of_sampling,
		"purpose_of_sequencing" AS purpose_of_sequencing,
		"sars_cov_2_diag_gene_name_1" AS sars_cov_2_diag_gene_name_1,
		"sars_cov_2_diag_pcr_ct_value_1" AS sars_cov_2_diag_pcr_ct_value_1,
		"sars_cov_2_diag_gene_name_2" AS sars_cov_2_diag_gene_name_2,
		"sars_cov_2_diag_pcr_ct_value_2" AS sars_cov_2_diag_pcr_ct_value_2,
		"sequenced_by" AS sequenced_by,
		"vaccine_receive" AS vaccine_received,
		"virus_isolate_of_prior_infection" AS virus_isolate_of_prior_infection,
		samples.description AS description



	FROM view_samples_base AS samples
	LEFT JOIN view_samples_host AS hosts
		ON samples.sample_id = hosts.sample_id
	LEFT JOIN view_sample_collection AS collection
		ON samples.sample_id = collection.sample_id
	LEFT JOIN view_sample_location AS location
		ON samples.sample_id = location.sample_id
	LEFT JOIN view_samples_sampling AS sampling
		ON samples.sample_id = sampling.sample_id
	LEFT JOIN view_samples_health_status AS health
		ON samples.sample_id = health.sample_id
