#!/bin/bash
#递归
function getdir(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then 
            getdir $dir_or_file
        else
            echo $dir_or_file
        fi  
    done
}

#非递归
function getdir_first(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then 
            py_path="iOS_system_framework_sqllitte.py"
            system_run_path=$(cd $dir_or_file ;pwd)
            python3 $system_run_path/$py_path
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