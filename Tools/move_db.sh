#!/bin/bash

function getdir_first(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then 
            db_ext=".db"
            db_file_path=$element$db_ext
            system_run_path=$(cd $dir_or_file ;pwd)
            output_brain_path=$(cd $curdir; cd .. ;pwd)
            output_db=$(cd $output_brain_path; cd "DB" ;pwd)
            echo $db_file_path

            cp  $system_run_path/$db_file_path $output_db/$db_file_path 
        else
            echo $dir_or_file
        fi  
    done
}


curdir=$(cd "$(dirname $0)";pwd)
output_brain=$(cd $curdir; cd .. ;pwd)
output=$(cd $output_brain; cd "Output" ;pwd)

echo 'project: '$output
getdir_first $output