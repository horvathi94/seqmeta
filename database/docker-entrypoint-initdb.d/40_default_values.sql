CREATE TABLE IF NOT EXISTS `default_values`(
	`item_key`			VARCHAR(100) NOT NULL PRIMARY KEY,
	`item_value`		VARCHAR(100) NULL
);


DELIMITER $$

CREATE PROCEDURE upsert_deftab(
	IN in_key 		VARCHAR(100),
	IN in_value 	VARCHAR(100)
)

	BEGIN
		
		SELECT in_key;

		SELECT @exist := COUNT(*)
			FROM `default_values` 
			WHERE item_key = in_key;

		SELECT @exist;

		IF(@exist = 1) THEN

			UPDATE `default_values`
				SET `item_value` = in_value
				WHERE `item_key` = in_key;

		ELSE 

			INSERT INTO `default_values` (`item_key`, `item_value`) 
				VALUES (in_key, in_value);
				
		END IF;


	END $$


DELIMITER ;


CALL upsert_deftab("continent_id", NULL);
CALL upsert_deftab("country_id", NULL);
CALL upsert_deftab("region", NULL);
CALL upsert_deftab("locality", NULL);
CALL upsert_deftab("geo_loc_latitude", NULL);
CALL upsert_deftab("geo_loc_longitude", NULL);
CALL upsert_deftab("host_id", NULL);
CALL upsert_deftab("patient_status_id", NULL);
CALL upsert_deftab("sampling_strategy_id", NULL);
CALL upsert_deftab("passage_details_id", NULL);
CALL upsert_deftab("assembly_method_id", NULL);
CALL upsert_deftab("sequencing_instrument_id", NULL);
CALL upsert_deftab("specimen_source_id", NULL);
CALL upsert_deftab("sample_capture_status_id", NULL);
CALL upsert_deftab("library_strategy_id", NULL);
CALL upsert_deftab("library_source_id", NULL);
CALL upsert_deftab("library_selection_id", NULL);
CALL upsert_deftab("library_layout_paired", NULL);
CALL upsert_deftab("originating_lab_id", NULL);
CALL upsert_deftab("submitting_lab_id", NULL);
CALL upsert_deftab("author_group_id", NULL);
