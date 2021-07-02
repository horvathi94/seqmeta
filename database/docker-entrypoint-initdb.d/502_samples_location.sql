CREATE TABLE IF NOT EXISTS `samples_location` (

	sample_id									INT UNSIGNED NOT NULL PRIMARY KEY,
	continent_id							TINYINT UNSIGNED,
	country_id								SMALLINT UNSIGNED,
	region										VARCHAR(150),
	locality									VARCHAR(150),
	additional_location_info	VARCHAR(1000),
	geo_loc_latitude					DECIMAL(5,2),
	geo_loc_longitude					DECIMAL(5,2),
	geo_loc_exposure_id				SMALLINT UNSIGNED

);



CREATE OR REPLACE VIEW view_samples_location AS 

	SELECT 

		location.sample_id AS sample_id,
		CONCAT(
			IF(continents.label IS NULL OR continents.label = "", "", continents.label),
			IF(countries.label IS NULL OR countries.label = "", "", CONCAT(" / ", countries.label)), 
			IF(location.region IS NULL OR location.region = "", "", CONCAT(" / ", location.region)),
			IF(location.locality IS NULL OR location.locality = "", "", CONCAT(" / ", location.locality))
			) AS location,
		IF (continents.label IS NULL, "", continents.label) AS continent,
		IF (countries.label IS NULL, "", countries.label) AS country,
		location.region AS region,
		location.locality AS locality,
		location.additional_location_info AS additional_location_info,
		IF (location.geo_loc_latitude IS NULL, "", location.geo_loc_latitude) AS geo_loc_latitude,
		IF (location.geo_loc_longitude IS NULL, "", location.geo_loc_longitude) AS geo_loc_longitude,
		exposure_country.label AS geo_loc_exposure

	
	FROM samples_location AS location
	LEFT JOIN continents
		ON location.continent_id = continents.id
	LEFT JOIN countries 
		ON location.country_id = countries.id
	LEFT JOIN countries AS exposure_country
		ON location.geo_loc_exposure_id = exposure_country.id;

