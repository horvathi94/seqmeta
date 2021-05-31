CREATE OR REPLACE VIEW view_samples_details AS

	SELECT 

		samples.sample_id AS sample_id,
		samples.sample_name AS sample_name,
	
		location.location AS location,
		location.additional_location_info AS additional_location_info,
		IF(location.geo_loc_latitude IS NULL, "",
				CONCAT(location.geo_loc_latitude, " DD") ) AS geo_loc_latitude,
		IF(location.geo_loc_longitude IS NULL, "",
				CONCAT(location.geo_loc_longitude, " DD") ) AS geo_loc_longitude,

		coll.collection_date AS collection_date,
		coll.collector_abbreviated_middle_name AS collector_name,

		library.library_id AS library_id,
		library.library_layout AS library_layout,
		library.library_strategy AS library_strategy,
		library.library_source AS library_source,
		library.library_selection AS library_selection,
		library.library_design_description AS library_design_description,

		host.host_name AS host_name,
		host.host_subject_id AS host_subject_id,
		host.additional_host_info AS additional_host_info,
		IF (host.patient_age IS NULL, "", 
			CONCAT(host.patient_age, " years")) AS patient_age,
		host.patient_gender AS patient_gender,
		host.patient_status AS patient_status,
		host.last_vaccinated AS last_vaccinated,
		host.host_habitat AS host_habitat,
		host.host_behaviour AS host_behaviour,
		host.host_description AS host_decription,
		host.host_gravidity AS host_gravidity,

		sampling.originating_lab_name AS originating_lab_name,
		sampling.submitting_lab_name AS submitting_lab_name,
		sampling.passage_details AS passage_details,
		sampling.sampling_strategy AS sampling_strategy,
		sampling.author_group_name AS author_group_name,
		sampling.authors_list AS authors_list,
		sampling.isolate AS isolate,
		sampling.strain AS strain,
		sampling.sample_capture_status AS sample_capture_status,
		sampling.specimen_source AS specimen_source


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

