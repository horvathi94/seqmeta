DELIMITER $$

CREATE PROCEDURE UpsertAuthorsInGroup(
	IN gid INT UNSIGNED,
	IN aid INT UNSIGNED,
	IN oindx INT UNSIGNED
)

	BEGIN

		SET @id := 0;
		SELECT @id := id 
			FROM `authors_in_group` 
			WHERE `author_group_id` = gid
				AND `author_id` = aid;

		IF ( @id > 0 ) THEN

			UPDATE `authors_in_group`
				SET `order_index` = oindx
				WHERE id = @id;

		ELSE

			INSERT INTO `authors_in_group` 
				(author_group_id, author_id, order_index) 
				VALUES (gid, aid, oindx);

		END IF;


	END $$



CREATE PROCEDURE UpsertGroup(
	IN gid INT UNSIGNED,
	IN gname CHAR(100),
	OUT groupInsertedID INT UNSIGNED
)

	BEGIN 

		IF ( gid = 0 ) THEN

			INSERT INTO `author_groups` (name)
				VALUES (gname);
			SELECT LAST_INSERT_ID() INTO groupInsertedID;

		ELSE

			UPDATE `author_groups`
				SET `name` = gname
			WHERE `id` = gid;

			SELECT gid INTO groupInsertedID;

		END IF;

	END $$

DELIMITER ;
