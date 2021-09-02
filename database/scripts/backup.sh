#!/bin/bash

# Perform backups for the MySQL database

BACKUPS_DIR="/backups"
SAVE_DATA="all";


help(){
	# Display help
	echo "Backup tables from the MySQL database.";
	echo ;
  echo "Syntax: backup [-s|-h]";
  echo "options:";
  echo "  -d, --data   Specify the type of save you want to perform.";
  echo "  -h, --help   Print this help screen.";
  echo ;
	echo "Save options:";
	echo "  samples      Data related to the samples.";
	echo "  groups       Authors, author groups and institutions.";
	echo "  defaults     The default values.";
	echo "  misc         Values specified on the misc page.";
	echo "  templates    Virusname and isolatename templates.";
	echo "  all          All of the above. This is the default option.";
	echo ;
}



####################################################################
# Save tables related to the samples.  
####################################################################
function save_samples(){
	filename="samples.sql"
	mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD -t \
		$MYSQL_DATABASE samples samples_collection samples_health_status \
		  samples_host samples_library samples_location \
			samples_patient_treatment samples_sampling samples_sequencing \
			  > "$BACKUPS_DIR/$filename"
}


####################################################################
# Save tables related to authors, author groups and institutions.  
####################################################################
save_groups(){
	filename="groups.sql"
	mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD -t \
		$MYSQL_DATABASE authors author_groups authors_in_group institutions \
		  > "$BACKUPS_DIR/$filename"
}


####################################################################
# Save default values.  
####################################################################
save_defaults(){
	filename="defaults.sql"
	mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD \
		$MYSQL_DATABASE default_values > "$BACKUPS_DIR/$filename"
}



####################################################################
# Save misc tables.  
####################################################################
save_misc(){
	filename="misc.sql"
	mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD \
		$MYSQL_DATABASE hosts assembly_methods sampling_strategies \
		specimen_sources collection_devices host_anatomical_materials \
		host_body_products purposes_of_sampling purposes_of_sequencing \
		  > "$BACKUPS_DIR/$filename"
}


####################################################################
# Save virusname and isolatename templates.  
####################################################################
save_templates(){
	filename="templates.sql"
	mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD -t \
		$MYSQL_DATABASE virusnames > "$BACKUPS_DIR/$filename"
}




####################################################################
# Main script
####################################################################


for p in $@; do

	case $p in

		-d=*|--data=*)
			SAVE_DATA="${p#*=}"
			shift
			;;

		-h|--help)
			help;
			exit;
			;;

		*)
			echo "Invalid options given. Please check the help menu."
			exit 1;;

	esac;

done;



case $SAVE_DATA in

	groups)	
		save_groups;
		;;

  samples)
    save_samples;
		;;

	defaults)
		save_defaults;
		;;

	misc)
    save_misc;
		;;

	templates)
		save_templates;
		;;

  all)
		save_groups;
		save_samples;
		save_defaults;
		save_misc;
		save_templates;
    ;;

	*)
		echo "Invalid value given for saving. Please check the help menu.";
		exit 2;
	;;


esac;
