#!/bin/bash

mysqldump \
	--user=$MYSQL_USER \
	-p$MYSQL_PASSWORD \
	--skip-add-drop-table	-t \
	$MYSQL_DATABASE \
		samples \
		virusnames \
		author_groups \
	 	authors \
	 	authors_in_group \
		default_values \
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
