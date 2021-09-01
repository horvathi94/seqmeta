#!/bin/bash

# File from which to restore the data
RESTORE_FILE="all.sql"


####################################################################
# Display help message  
####################################################################
help(){
  echo "Restore MySQL tables from backip."
  echo 
  echo "Syntax: $0 [-d|-h] backup.sql"
  echo "options:"
  echo "  -d, --data   Which data to restore. If not specified the "
  echo "               script will restore from the given file."
  echo "  -h, --help   Displays this help screen."
  echo
  echo ;
	echo "Restore options:";
	echo "  samples      Data related to the samples.";
	echo "  groups       Authors, author groups and institutions.";
	echo "  defaults     The default values.";
	echo "  misc         Values specified on the misc page.";
	echo "  templates    Virusname and isolatename templates.";
	echo "  all          All of the above. This is the default option.";
	echo ;
}



####################################################################
# Restore table data from a script  
####################################################################
restore(){
    if [ -f "$1" ]; then
      echo "Restoring from: $1"
        mysql --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
            --database=$MYSQL_DATABASE < $1
    else
        exit 10
    fi

}



if [ "$#" -ne 1 ]; then
    echo "Invalid number of arguments given."
    exit 1
fi




for p in $@; do

    case $p in

        -d=*|--data=*)
            RESTORE_FILE="/backups/${p#*=}.sql"
            ;;

        -h|--help)
            help
            exit 0
            ;;        

        *)
            RESTORE_FILE=$1
            ;;


    esac;

done;


restore $RESTORE_FILE

