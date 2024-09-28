#!/bin/bash
#
#  Script to make directory and new empty files for problem on Linux.

if [[ -z ${1} ]]; then
  
  echo
  echo 'New directory name not specified!'
  echo 'Syntax: set_new_dir.sh ${dir_name}'
  echo 

  exit 2

else

  declare -a file_list
  file_list=("code.py" "test.py" "sample_dataset.txt")
  file_list+=("sample_output.txt" "dataset.txt" "output.txt")

  for file in $(ls problems)
  do
      mtch=$(cat "problems/${file}" | grep ${1})
      
      if [ $mtch ]; then
        problems=($(echo $file | tr '.' "\n"))
        problems=${problems[0]}
        break
      fi
  done

  if [ $problems ]; then
  
    problem_path="${problems}/${1}"

    if [ ! -d ${problem_path} ]; then
      mkdir ${problem_path}
    fi

    cd ${problem_path}

    for file in ${file_list[@]}
    do

      if [ ! -f ${file} ]; then
        touch ${file}
      else
        echo
        echo "${file} already exists!"
      fi

    done

  else

    echo
    echo 'Problem name not found!'
    echo 

    exit 2

  fi

fi
