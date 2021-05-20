CREATE VIEW view_samples_edit AS

	SELECT

		samples.id AS sample_id,
		samples.name AS sample_name,
		samples.collection_date AS collection_date,
		
		samples.host_id AS host_id,
		samples.additional_host_info AS additional_host_info,
		IF (samples.patient_gender = "" OR samples.patient_gender IS NULL, "unknown", 
			IF (samples.patient_gender = 1, "Male", "Female")
		) AS patient_gender,
		samples.patient_age AS patient_age,
		samples.patient_status_id AS patient_status_id,

		samples.location AS location,
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

		samples.specimen_source AS specimen_source,								
		samples.outbreak AS outbreak,
		samples.last_vaccinated AS last_vaccinated,					
		samples.treatment AS treatment

	FROM samples

