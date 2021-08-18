DROP PROCEDURE IF EXISTS `delete_sample`;


DELIMITER $$


CREATE PROCEDURE `delete_sample` (
	IN delid INT UNSIGNED
)

	BEGIN

		DELETE FROM `samples` WHERE `id` = delid;
		DELETE FROM `samples_collection` WHERE `sample_id` = delid;
		DELETE FROM `samples_location` WHERE `sample_id` = delid;
		DELETE FROM `samples_host` WHERE `sample_id` = delid;
		DELETE FROM `samples_health_status` WHERE `sample_id` = delid;
		DELETE FROM `samples_sampling` WHERE `sample_id` = delid;
		DELETE FROM `samples_library` WHERE `sample_id` = delid;
		DELETE FROM `samples_sequencing` WHERE `sample_id` = delid;
		DELETE FROM `samples_patient_treatment` WHERE `sample_id` = delid;

	END $$


DELIMITER ;
