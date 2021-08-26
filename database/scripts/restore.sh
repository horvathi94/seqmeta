#!/bin/bash

####################################################################
# Display help message  
####################################################################
help(){
  echo "Restore MySQL tables from backip."
  echo 
  echo "Syntax: $0 [-h] backup.sql"
  echo "options:"
  echo "  -h, --help   Displays this help screen."
  echo
}



####################################################################
# Restore table data from a script  
####################################################################
restore(){
    if [ -f "$1" ]; then
        mysql --user=$MYSQL_USER --password=$MYSQL_PASSWORD \
            $MYSQL_DATABASE -e $1
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

        -h|--help)
            help
            exit 0
            ;;        

        *)
            ;;


    esac;

done;


restore $1

