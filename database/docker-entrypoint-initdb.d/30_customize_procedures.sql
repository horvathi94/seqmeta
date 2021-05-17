DELIMITER $$

CREATE PROCEDURE UpsertHosts(
	IN host_id 			MEDIUMINT UNSIGNED,
	IN host_label 	CHAR(100),
	IN host_latin		CHAR(100)
)

	BEGIN

		IF ( host_id = 0 ) THEN

			IF ( host_label <> '' ) THEN

				INSERT INTO `hosts` (label, latin) 
					VALUES (host_label, host_latin);

			END IF;


		ELSE 

			IF ( host_label = '' ) THEN

				DELETE 
					FROM `hosts` 
					WHERE id = host_id;

			ELSE

				UPDATE `hosts` 
					SET `label` = host_label,
							`latin` = host_latin
					WHERE id = host_id;
			

			END IF;


		END IF;


	END $$



CREATE PROCEDURE UpsertSamplingStrategies(
	IN sampling_strategy_id 			MEDIUMINT UNSIGNED,
	IN sampling_strategy_label 	CHAR(100)
)

	BEGIN

		IF ( sampling_strategy_id = 0 ) THEN

			IF ( sampling_strategy_label <> '' ) THEN

				INSERT INTO `sampling_strategies` (label) 
					VALUES (sampling_strategy_label);

			END IF;


		ELSE 

			IF ( sampling_strategy_label = '' ) THEN

				DELETE 
					FROM `sampling_strategies` 
					WHERE id = sampling_strategy_id;

			ELSE

				UPDATE `sampling_strategies` 
					SET `label` = sampling_strategy_label
					WHERE id = sampling_strategy_id;
			

			END IF;


		END IF;


	END $$



CREATE PROCEDURE UpsertPassageDetails(
	IN passage_details_id 			MEDIUMINT UNSIGNED,
	IN passage_details_label 	CHAR(100)
)

	BEGIN

		IF ( passage_details_id = 0 ) THEN

			IF ( passage_details_label <> '' ) THEN

				INSERT INTO `passage_details` (label) 
					VALUES (passage_details_label);

			END IF;


		ELSE 

			IF ( passage_details_label = '' ) THEN

				DELETE 
					FROM `passage_details` 
					WHERE id = passage_details_id;

			ELSE

				UPDATE `passage_details` 
					SET `label` = passage_details_label
					WHERE id = passage_details_id;
			

			END IF;


		END IF;


	END $$


DELIMITER ;
