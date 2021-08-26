#!/bin/bash

# Perform backups for the MySQL database


help(){
	# Display help
	echo "Backup tables from the MySQL database.";
	echo ;
  echo "Syntax: backup [-s|-h]";
  echo "options:";
  echo "  -s, --save   Specify the type of save you want to perform.";
  echo "  -h, --help   Print this help screen.";
  echo ;
	echo "Save options:";
	echo "  samples      Data related to the samples.";
	echo "  groups       Authors, author groups and institutions.";
	echo "  default      The default values.";
	echo "  misc         Values specified on the misc page.";
	echo "  templates    Virusname and isolatename templates.";
	echo "  all          All of the above. This is the default option.";
	echo ;
}


####################################################################
# Save tables related to the samples.  
####################################################################
save_samples(){
	mysqldump --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
		-t \
		$MYSQL_DATABASE \
			samples samples_collection samples_health_status \
			samples_host samples_library samples_location \
			samples_patient_treatment samples_sampling samples_sequencing \
			seqfiles;
}


####################################################################
# Save tables related to authors, author groups and institutions.  
####################################################################
save_groups(){
	mysqldump --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
		-t \
		$MYSQL_DATABASE \
			authors author_groups authors_in_group institutions;
}


####################################################################
# Save default values.  
####################################################################
save_defaults(){
	mysqldump --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
		-t \
		$MYSQL_DATABASE \
			default_values;
}



####################################################################
# Save misc tables.  
####################################################################
save_misc(){
	mysqldump --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
		-t \
		$MYSQL_DATABASE \
			hosts assembly_methods sampling_strategies specimen_sources \
			collection_devices anatomical_materials body_products \
			purposes_of_sampling purposes_of_sequencing;
}


####################################################################
# Save virusname and isolatename templates.  
####################################################################
save_templates(){
	mysqldump --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
		-t \
		$MYSQL_DATABASE \
			virusnames;
}





####################################################################
# Main script
####################################################################

SAVE_DATA="all";

for p in $@; do

	case $p in

		-s=*|--save=*)
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
