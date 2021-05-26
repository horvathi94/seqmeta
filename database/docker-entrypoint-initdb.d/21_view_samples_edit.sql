CREATE VIEW view_samples_edit AS

	SELECT

		samples.id AS sample_id,
		samples.name AS sample_name,
		samples.collection_year AS collection_year,
		samples.collection_month AS collection_month,
		samples.collection_day AS collection_day,

		samples.host_id AS host_id,
		samples.additional_host_info AS additional_host_info,
		IF (samples.patient_gender = "" OR samples.patient_gender IS NULL, "unknown", 
			IF (samples.patient_gender = 1, "Male", "Female")
		) AS patient_gender,
		samples.patient_age AS patient_age,
		samples.patient_status_id AS patient_status_id,

		samples.continent_id AS continent_id,
		samples.country_id AS country_id,
		samples.county AS county,
		samples.city AS city,
		samples.additional_location_info AS additional_location_info,

		samples.originating_lab_id AS originating_lab_id,
		samples.originating_lab_sample_name AS originating_lab_sample_name,	
		samples.submitting_lab_id AS submitting_lab_id,
		samples.submitting_lab_sample_name AS submitting_lab_sample_name,
		samples.author_group_id AS author_group_id,

		samples.sampling_strategy_id AS sampling_strategy_id,	
		samples.passage_details_id AS passage_details_id,
		samples.sequencing_technology_id AS sequencing_technology_id,
		samples.assembly_method_id AS assembly_method_id,	
		samples.coverage AS coverage,

		samples.specimen_source_id AS specimen_source_id,
		samples.outbreak AS outbreak,
		samples.last_vaccinated AS last_vaccinated,					
		samples.treatment AS treatment,

		samples.subject_exposure AS subject_exposure,
		samples.subject_exposure_duration AS subject_exposure_duration,
		samples.type_exposure AS type_exposure,
		samples.ppe AS ppe,
	
		IF (samples.hospitalization = "" OR samples.hospitalization IS NULL, "N/A", 
			IF (samples.hospitalization = 1, "Yes", "No")
		) AS hospitalization,
		samples.ilness_duration AS ilness_duration,
		samples.ilness_symptoms AS ilness_symptoms,
	
		samples.geo_loc_latitude AS geo_loc_latitude,
		samples.geo_loc_longitude AS geo_loc_longitude,
		
		samples.sample_capture_status_id AS sample_capture_status_id,
		samples.host_disease_outcome_id	AS host_disease_outcome_id,
		
		samples.host_subject_id	AS host_subject_id, 
		samples.host_health_state_id AS host_health_state_id,
		
		samples.collector_name_id	AS collector_name_id,
		samples.receipt_date AS receipt_date,
		samples.sample_storage_conditions	AS sample_storage_conditions,
		
		samples.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		samples.serotype AS serotype,
		
		samples.isolate AS isolate,
		samples.strain AS strain,
		
		samples.isolation_source_host_associated AS isolation_source_host_associated,
		samples.host_description AS host_description,
		samples.gravidity AS gravidity,
		samples.isolation_source_non_host_associated AS isolation_source_non_host_associated

	FROM samples

