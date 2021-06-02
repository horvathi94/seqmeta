CREATE OR REPLACE VIEW `view_samples_base` AS

	SELECT 

		samples.id AS sample_id,
		samples.name AS sample_name,

		location.continent_id AS continent_id,
		location.country_id AS country_id,
		location.region AS region,
		location.locality AS locality,
		location.geo_loc_latitude AS geo_loc_latitude,
		location.geo_loc_longitude AS geo_loc_longitude,
		location.additional_info AS additional_location_info,

		collection.year AS collection_year,
		collection.month AS collection_month,
		collection.day AS collection_day,
		collection.collector_id AS collector_id,

		library.lib_id AS library_id,
		library.layout_paired AS library_layout_paired,
		library.strategy_id AS library_strategy_id,
		library.source_id AS library_source_id,
		library.selection_id AS library_selection_id,
		library.design_description AS library_design_description,
		library.preparation_date AS library_preparation_date,

		host.host_id AS host_id,
		host.host_subject_id AS	host_subject_id,
		host.additional_host_info	AS additional_host_info,
		host.patient_gender	AS patient_gender,
		host.patient_age AS patient_age,
		host.patient_status_id AS	patient_status_id,
		host.last_vaccinated AS last_vaccinated,
		host.ppe AS	ppe,
		host.host_habitat_id AS host_habitat_id,
		host.host_behaviour_id AS	host_behaviour_id,
		host.host_description	AS host_description,
		host.gravidity AS	gravidity,

		sampling.originating_lab_id AS originating_lab_id,
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		sampling.submitting_lab_id AS submitting_lab_id,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name,
		sampling.author_group_id AS author_group_id,
		sampling.receipt_date AS receipt_date,
		sampling.sampling_strategy_id AS sampling_strategy_id,
		sampling.passage_details_id AS passage_details_id,
		sampling.isolate AS isolate,
		sampling.strain AS strain,
		sampling.isolation_source_host_associated AS isolation_source_host_associated,
		sampling.isolation_source_non_host_associated	isolation_source_non_host_associated,
		sampling.sample_capture_status_id AS sample_capture_status_id,
		sampling.specimen_source_id AS specimen_source_id,
		sampling.sample_storage_conditions AS sample_storage_conditions,
		sampling.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		sampling.serotype AS serotype,

		health.subject_exposure AS subject_exposure,
		health.subject_exposure_duration AS subject_exposure_duration,	
		health.type_exposure AS type_exposure,
		health.hospitalization AS hospitalization,
		health.ilness_duration AS ilness_duration,
		health.ilness_symptoms AS ilness_symptoms,
		health.host_disease_outcome_id AS host_disease_outcome_id,
		health.host_health_state_id AS host_health_state_id,
		health.treatment AS treatment,
		health.outbreak AS outbreak,
	
		sequencing.sequencing_instrument_id AS sequencing_instrument_id,
		sequencing.assembly_method_id AS assembly_method_id,
		sequencing.coverage AS coverage


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
