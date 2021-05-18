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



CREATE PROCEDURE UpsertAssemblyMethods(
	IN assembly_methods_id 			MEDIUMINT UNSIGNED,
	IN assembly_methods_label 	CHAR(100)
)

	BEGIN

		IF ( assembly_methods_id = 0 ) THEN

			IF ( assembly_methods_label <> '' ) THEN

				INSERT INTO `assembly_methods` (label) 
					VALUES (assembly_methods_label);

			END IF;


		ELSE 

			IF ( assembly_methods_label = '' ) THEN

				DELETE 
					FROM `assembly_methods` 
					WHERE id = assembly_methods_id;

			ELSE

				UPDATE `assembly_methods` 
					SET `label` = assembly_methods_label
					WHERE id = assembly_methods_id;
			

			END IF;


		END IF;


	END $$





CREATE PROCEDURE UpsertSequencingTechnologies(
	IN sequencing_technologies_id 			MEDIUMINT UNSIGNED,
	IN sequencing_technologies_label 	CHAR(100)
)

	BEGIN

		IF ( sequencing_technologies_id = 0 ) THEN

			IF ( sequencing_technologies_label <> '' ) THEN

				INSERT INTO `sequencing_technologies` (label) 
					VALUES (sequencing_technologies_label);

			END IF;


		ELSE 

			IF ( sequencing_technologies_label = '' ) THEN

				DELETE 
					FROM `sequencing_technologies` 
					WHERE id = sequencing_technologies_id;

			ELSE

				UPDATE `sequencing_technologies` 
					SET `label` = sequencing_technologies_label
					WHERE id = sequencing_technologies_id;
			

			END IF;


		END IF;


	END $$



DELIMITER ;
