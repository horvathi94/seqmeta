DELIMITER $

DROP PROCEDURE IF EXISTS `upsert_template`;
CREATE PROCEDURE `upsert_template` (
	IN in_id INT UNSIGNED,
	IN in_name VARCHAR(200)
)
BEGIN

	SET @is_reg := (SELECT `id` FROM `templates` WHERE `id` = in_id);

	IF (@is_reg IS NULL) THEN
	
		INSERT INTO `templates` (`name`) VALUES (in_name);

	ELSE 

		UPDATE `templates` SET `name` = in_name WHERE `id` = in_id;

	END IF;

END $


DELIMITER ;
