DELIMITER $

DROP PROCEDURE IF EXISTS `upsert_sample`;
CREATE PROCEDURE `upsert_sample` (
	IN in_id INT UNSIGNED,
	IN in_template_id INT UNSIGNED,
	IN in_name VARCHAR(200),
	IN in_short_description VARCHAR(500),
	IN in_status VARCHAR(10),
	OUT sample_id INT UNSIGNED
)
new_sample:BEGIN


	IF (in_status = "new") THEN

		INSERT
		INTO `samples`
			(`name`, `template_id`, `short_description`)
		VALUES
			(in_name, in_template_id, in_short_description);
		SET sample_id = (SELECT LAST_INSERT_ID());

		LEAVE new_sample;

	END IF;


	UPDATE
		`samples`
	SET 
		`name` = in_name,
		`template_id` = in_template_id,
		`short_description` = in_short_description
	WHERE
		`id` = in_id;

	SET sample_id = in_id;


END $


DROP PROCEDURE IF EXISTS `upsert_sample_attribute`;
CREATE PROCEDURE `upsert_sample_attribute` (
	IN in_sample_id INT UNSIGNED,
	IN in_name VARCHAR(100),
	IN in_value TEXT,
	IN in_sample_status VARCHAR(20)
)
new_attr:BEGIN

	SET @attr_id = (
		SELECT
			`id` 
		FROM
			`sample_attributes`
		WHERE
			`sample_id` = in_sample_id AND
			`name` = in_name
	);


	IF (in_sample_status = "new" OR @attr_id IS NULL) THEN

		INSERT 
			INTO `sample_attributes`
				(`sample_id`, `name`, `value`)
			VALUES
				(in_sample_id, in_name, in_value);
			
		LEAVE new_attr;

	END IF;

	UPDATE 
		`sample_attributes`
	SET
		`value` = in_value
	WHERE
		`id` = @attr_id;


END $

DELIMITER ;
