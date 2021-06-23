#!/bin/bash

mysqldump \
	--user=$MYSQL_USER \
	-p$MYSQL_PASSWORD \
	--skip-add-drop-table \
	-t \
	--complete-insert \
	$MYSQL_DATABASE \
		samples \
		author_groups \
	 	authors \
	 	authors_in_group \
		ena_studies \
		institutions \
		samples_collection \
		samples_health_status \
		samples_host \
		samples_library \
		samples_location \
		samples_sampling \
		samples_sequencing \
		sampling_strategies \
		seqfiles

mysqldump \
	--user=$MYSQL_USER \
	-p$MYSQL_PASSWORD \
	--complete-insert \
	$MYSQL_DATABASE \
		virusnames \
		default_values 
