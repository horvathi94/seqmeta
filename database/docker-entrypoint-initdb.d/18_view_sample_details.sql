CREATE OR REPLACE VIEW view_samples_location AS 

	SELECT 

		location.sample_id AS sample_id,
		CONCAT(continents.label, " / ", countries.label, 
			IF(location.region IS NOT NULL, CONCAT(" / ", location.region), ""),
			IF(location.locality IS NOT NULL, CONCAT(" / ", location.locality), "")
			) AS location,
		location.additional_info AS additional_location_info,
		location.geo_loc_latitude AS geo_loc_latitude,
		location.geo_loc_longitude AS geo_loc_longitude
	
	FROM samples_location AS location
	LEFT JOIN continents
		ON location.continent_id = continents.id
	LEFT JOIN countries 
		ON location.country_id = countries.id;



CREATE OR REPLACE VIEW view_samples_collection AS 

	SELECT 
	
		coll.sample_id AS sample_id,
		coll.year AS collection_year,
		coll.month AS collection_month,
		coll.day AS collection_day,
		CONCAT(coll.year,  
			IF (coll.month > 0 AND coll.month IS NOT NULL,
				CONCAT("-", LPAD(coll.month, 2, 0), 
					IF (coll.day > 0 AND coll.day IS NOT NULL,
						CONCAT("-", LPAD(coll.day, 2, 0) ), "" ) ), 
					"") ) AS collection_date,
		authors.abbreviated_middle_name AS collector_abbreviated_middle_name


		FROM samples_collection AS coll
		LEFT JOIN view_authors AS authors
			ON coll.collector_id = authors.id;



CREATE OR REPLACE VIEW view_samples_library AS 

	SELECT

		library.sample_id AS sample_id,
		library.lib_id AS library_id,
		IF( library.layout_paired	IS NULL, "",
			IF (library.layout_paired IS TRUE, "Paired-End", "Single") ) AS library_layout,
		strategies.item_key AS library_strategy,
		sources.item_key AS library_source,
		selections.item_key AS library_selection,
		library.design_description AS library_design_description

	FROM samples_library AS library
	LEFT JOIN library_strategies AS strategies
		ON library.strategy_id = strategies.id
	LEFT JOIN library_sources AS sources
		ON library.source_id = sources.id
	LEFT JOIN library_selections AS selections
		ON library.selection_id = selections.id;
	


CREATE OR REPLACE VIEW view_samples_host AS 

	SELECT 

		host.sample_id AS sample_id,
		hosts.label AS host_common_name,
		hosts.latin AS host_scientific_name,
		CONCAT(hosts.label, " (", hosts.latin, ")") AS host_name,
		host.host_subject_id AS host_subject_id,
		host.additional_host_info AS additional_host_info,
		host.patient_age AS patient_age,
		IF (host.patient_gender IS NULL, "unknown", 
			IF (host.patient_gender IS TRUE, "Male", "Female")
		) AS patient_gender,
		patient_statuses.label AS patient_status,
		host.last_vaccinated AS last_vaccinated,
		habitats.label AS host_habitat,
		behaviours.label AS host_behaviour,
		host.host_description AS host_description,
		host.gravidity AS host_gravidity

	FROM samples_host AS host
	LEFT JOIN hosts
		ON host.host_id = hosts.id
	LEFT JOIN patient_statuses
		ON host.patient_status_id = patient_statuses.id
	LEFT JOIN host_habitats AS habitats
		ON host.host_habitat_id = habitats.id
	LEFT JOIN host_behaviours AS behaviours
		ON host.host_behaviour_id = behaviours.id;


CREATE OR REPLACE VIEW view_samples_sampling AS

	SELECT 
		
		sampling.sample_id AS sample_id,
		originating_lab.name AS originating_lab_name,
		originating_lab.address AS originating_lab_address,
		sampling.originating_lab_sample_name AS originating_lab_sample_name,
		submitting_lab.name AS submitting_lab_name,
		submitting_lab.address AS submitting_lab_address,
		sampling.submitting_lab_sample_name AS submitting_lab_sample_name,
		passage_details.label AS passage_details,
		sampling_strategies.label AS sampling_strategy,
		author_groups.group_name AS author_group_name,
		author_groups.abbreviated_middle_names AS authors_list,
		sampling.isolate AS isolate,
		sampling.strain AS strain,
		sampling.isolation_source_host_associated AS isolation_source_host_associated,
		sampling.isolation_source_non_host_associated AS isolation_source_non_host_associated,
		capture_statuses.label AS sample_capture_status,
		specimen_sources.label AS specimen_source,
		sampling.sample_storage_conditions AS sample_storage_conditions,
		sampling.definition_for_seropositive_sample AS definition_for_seropositive_sample,
		sampling.serotype AS serotype

	FROM samples_sampling AS sampling
	LEFT JOIN view_institutions AS originating_lab
		ON sampling.originating_lab_id = originating_lab.id
	LEFT JOIN view_institutions AS submitting_lab
		ON sampling.submitting_lab_id = submitting_lab.id
	LEFT JOIN view_passage_details AS passage_details
		ON sampling.passage_details_id = passage_details.id
	LEFT JOIN view_sampling_strategies AS sampling_strategies
		ON sampling.sampling_strategy_id = sampling_strategies.id
	LEFT JOIN view_authors_in_groups_condensed AS author_groups
		ON sampling.author_group_id = author_groups.`group_id`
	LEFT JOIN sample_capture_status AS capture_statuses
		ON sampling.sample_capture_status_id = capture_statuses.id
	LEFT JOIN view_specimen_sources AS specimen_sources
		ON sampling.specimen_source_id = specimen_sources.id
