CREATE OR REPLACE VIEW `view_samples_base` AS

	SELECT 

		samples.id AS sample_id,
		samples.name AS sample_name,
		samples.`comment` AS sample_comment,
		samples.title AS sample_title,
		samples.description AS sample_description,

		collection.collection_year AS collection_year,
		collection.collection_month AS collection_month,
		collection.collection_day AS collection_day,
		collection.collector_id AS collector_id,
		collection.originating_lab_id AS originating_lab_id,
		collection.originating_lab_sample_name AS originating_lab_sample_name,
		collection.submitting_lab_id AS submitting_lab_id,
		collection.submitting_lab_sample_name AS submitting_lab_sample_name,
		collection.author_group_id AS author_group_id,
		
		location.continent_id AS continent_id,
		location.country_id AS country_id,
		location.region AS region,
		location.locality AS locality,
		location.geo_loc_latitude AS geo_loc_latitude,
		location.geo_loc_longitude AS geo_loc_longitude,
		location.additional_location_info AS additional_location_info,

		treatment.prior_sars_cov_2_antiviral_treat AS prior_sars_cov_2_antiviral_treat,
		treatment.date_of_prior_antiviral_treat AS date_of_prior_antiviral_treat,
		treatment.prior_sars_cov_2_infection AS prior_sars_cov_2_infection,
		treatment.date_of_prior_sars_cov_2_infection AS date_of_prior_sars_cov_2_infection,
		treatment.prior_sars_cov_2_vaccination_id AS prior_sars_cov_2_vaccination_id,
		treatment.date_of_prior_sars_cov_2_vaccination AS date_of_prior_sars_cov_2_vaccination,
		treatment.virus_isolate_of_prior_infection AS virus_isolate_of_prior_infection,
		treatment.vaccine_received AS vaccine_received,

		host.host_id AS host_id,
		host.host_subject_id AS	host_subject_id,
		host.additional_host_info	AS additional_host_info,
		host.patient_gender	AS patient_gender,
		host.patient_age AS patient_age,
		host.patient_status_id AS	patient_status_id,
		host.ppe AS	ppe,
		host.host_habitat_id AS host_habitat_id,
		host.host_behaviour_id AS	host_behaviour_id,
		host.host_description	AS host_description,
		host.gravidity AS	gravidity,

		sampling.receipt_date AS receipt_date,
		sampling.sampling_strategy_id AS sampling_strategy_id,
		sampling.strain AS strain,
		sampling.isolation_source_host_associated AS isolation_source_host_associated,
		sampling.isolation_source_non_host_associated	isolation_source_non_host_associated,
		sampling.sample_capture_status_id AS sample_capture_status_id,
		sampling.specimen_source_id AS specimen_source_id,
		sampling.sample_storage_conditions AS sample_storage_conditions,
		sampling.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		sampling.serotype AS serotype,
		sampling.passage_method AS passage_method,
		sampling.passage_number AS passage_number,


		health.subject_exposure AS subject_exposure,
		health.subject_exposure_duration AS subject_exposure_duration,	
		health.type_exposure AS type_exposure,
		health.hospitalization AS hospitalization,
		health.ilness_duration AS ilness_duration,
		health.ilness_symptoms AS ilness_symptoms,
		health.host_disease_outcome_id AS host_disease_outcome_id,
		health.host_health_state_id AS host_health_state_id,
		health.outbreak AS outbreak,
		health.sars_cov_2_diag_gene_name_1_id AS sars_cov_2_diag_gene_name_1_id,
		health.sars_cov_2_diag_pcr_ct_value_1 AS sars_cov_2_diag_pcr_ct_value_1,
		health.sars_cov_2_diag_gene_name_2_id AS sars_cov_2_diag_gene_name_2_id,
		health.sars_cov_2_diag_pcr_ct_value_2 AS sars_cov_2_diag_pcr_ct_value_2,
	
		sequencing.sequencing_instrument_id AS sequencing_instrument_id,
		sequencing.assembly_method_id AS assembly_method_id,
		sequencing.coverage AS coverage,

		library.lib_id AS library_id,
		library.layout_paired AS library_layout_paired,
		library.strategy_id AS library_strategy_id,
		library.source_id AS library_source_id,
		library.selection_id AS library_selection_id,
		library.design_description AS library_design_description,
		library.preparation_date AS library_preparation_date

		FROM samples
		LEFT JOIN samples_location AS location
			ON samples.id = location.sample_id
		LEFT JOIN samples_collection AS collection
			ON samples.id = collection.sample_id
		LEFT JOIN samples_library AS library
			ON samples.id = library.sample_id
		LEFT JOIN samples_host AS host
			ON samples.id = host.sample_id
		LEFT JOIN samples_sampling AS sampling
			ON samples.id = sampling.sample_id
		LEFT JOIN samples_health_status AS health
			ON samples.id = health.sample_id
		LEFT JOIN samples_sequencing AS sequencing
			ON samples.id = sequencing.sample_id
		LEFT JOIN samples_patient_treatment AS treatment
			ON samples.id = treatment.sample_id
