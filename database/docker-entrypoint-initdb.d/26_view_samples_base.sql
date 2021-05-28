CREATE OR REPLACE VIEW `view_samples_base` AS

	SELECT 

		samples.id AS sample_id,
		samples.name AS sample_name,

		samples.link_location_id AS link_location_id,
		location.continent_id AS continent_id,
		location.country_id AS country_id,
		location.region AS region,
		location.locality AS locality,
		location.geo_loc_latitude AS geo_loc_latitude,
		location.geo_loc_longitude AS geo_loc_longitude,
		location.additional_info AS additional_location_info,

		samples.link_collection_id AS link_collection_id,
		collection.year AS collection_year,
		collection.month AS collection_month,
		collection.day AS collection_day,
		collection.collector_id AS collector_name_id,

		samples.link_library_id AS link_library_id,
		library.lib_id AS library_id,
/*		IF (library.layout_paired IS NULL, "N/A", 
			IF (library.layout_paired = 1, "Paired-end", "Single")
			) AS library_layout,*/
		library.layout_paired AS library_layout_paired,
		library.strategy_id AS library_strategy_id,
		library.source_id AS library_source_id,
		library.selection_id AS library_selection_id,
		library.design_description AS library_design_description


		FROM samples
		LEFT JOIN samples_location AS location
			ON samples.link_location_id = location.id
		LEFT JOIN samples_library AS library
			ON samples.link_library_id = library.id
		LEFT JOIN samples_collection AS collection
			ON samples.link_collection_id = collection.id


