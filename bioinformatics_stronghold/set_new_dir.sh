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
  file_list=(".gitignore" "code.py" "test.py" "sample_dataset.txt")
  file_list+=("sample_output.txt" "dataset.txt" "output.txt")

  gitignore_text=('__pycache__/*' 'sample_*')

  if [ ! -d ${1} ]; then
    mkdir ${1}
  fi

  cd ${1}

  for file in  ${file_list[@]}
  do

    if [ ! -f ${file} ]; then
      touch ${file}
    else
      echo
      echo "${file} already exists!"
    fi

  done

  gitignore_cont=$(cat .gitignore)

  for line in "${gitignore_text[@]}"
  do

    if [ -z "$(echo "${gitignore_cont}" | grep "${line}")" ]; then
      echo "${line}" >> .gitignore
    fi

  done

fi
