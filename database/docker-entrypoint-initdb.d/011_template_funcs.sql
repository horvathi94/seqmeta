DELIMITER $

DROP PROCEDURE IF EXISTS `upsert_template`;
CREATE PROCEDURE `upsert_template` (
	IN in_id INT UNSIGNED,
	IN in_name VARCHAR(200),
	OUT out_id INT UNSIGNED
)
BEGIN

	SET @is_reg := (SELECT `id` FROM `templates` WHERE `id` = in_id);

	IF (@is_reg IS NULL) THEN
	
		INSERT INTO `templates` (`name`) VALUES (in_name);
		SET out_id := (SELECT LAST_INSERT_ID());

	ELSE 

		UPDATE `templates` SET `name` = in_name WHERE `id` = in_id;
		SET out_id := in_id;

	END IF;

END $



DROP PROCEDURE IF EXISTS `upsert_attribute`;
CREATE PROCEDURE `upsert_attribute` (
	IN in_id INT UNSIGNED,
	IN in_template_id INT UNSIGNED,
	IN is_delete TINYINT,
	IN in_general_name VARCHAR(100),
	IN in_label VARCHAR(100),
	IN in_type_ VARCHAR(20),
	IN in_description VARCHAR(500),
	IN in_template VARCHAR(200),
	IN in_default VARCHAR(200),
	IN in_pattern VARCHAR(200),
	IN in_options TEXT,
	IN in_ena_name VARCHAR(200),
	IN in_ena_requirement VARCHAR(50),
	IN in_gisaid_name VARCHAR(200),
	IN in_gisaid_requirement VARCHAR(50)
)
new_attr:BEGIN

	IF (is_delete) THEN

		DELETE 
		FROM 
			`attributes`
		WHERE 
			`id` = in_id AND
			`template_id` = in_template_id;
		LEAVE new_attr;

	END IF;

	SET @is_reg := (
		SELECT
			`id`
		FROM 
			`attributes`
		WHERE
			`id` = in_id AND
			`template_id` = in_template_id);

	IF (@is_reg IS NULL) THEN

		INSERT 
		INTO `attributes`
			(`template_id`, `general_name`, `label`, `type_`, `description`,
				`template`, `default`, `pattern`, `options`,
				`ena_name`, `ena_requirement`, `gisaid_name`, `gisaid_requirement`)
		VALUES
			(template_id, in_general_name, in_label, in_type_, in_description,
				template, in_default, in_pattern, in_options,
				ena_name, in_ena_requirement, in_gisaid_name, in_gisaid_requirement);

	ELSE

		UPDATE
			`attributes`
		SET 
			`general_name` = in_general_name,
			`label` = in_label,
			`type_` = in_type_,
			`description` = in_description,
 			`template` = in_template,
			`default` = in_default,
			`pattern` = in_pattern,
			`options` = in_options,
			`ena_name` = in_ena_name,
			`ena_requirement` = in_ena_requirement,
			`gisaid_name` = in_gisaid_name,
			`gisaid_requirement` = in_gisaid_requirement
		WHERE
			`id` = in_id AND
			`template_id` = in_template_id;

	END IF;

END $

DELIMITER ;
