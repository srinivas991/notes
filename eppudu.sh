#!/bin/bash

# find_command="find . -type f 2>/dev/null"
# something like this for php extension maybe ?
# find_command = "find . -type f -name '*php*'"

find_dir="../"
ext=".*"
# ext=".*\.php"
# ext=".*\.conf"
# ext=".*\.config"

dir_rand_prefix=$(openssl rand -hex 2)

for j in $(find $find_dir -type f -iregex "$ext" 2>/dev/null); do

	if ! [[ "$j" =~ \.git ]]; then

		# add more awk in the below line according to your preference
		# like awk '{ print $1$2$3$4 }' - adds year in linux

		dir_name="$dir_rand_prefix"$(date -r "$j" | awk '{ print $1$2$3$4 }')
		mkdir "$dir_name" 2>/dev/null
		cp "$j" $dir_name/

	fi

done

# name the folders with the number of files inside
for j in $(find $find_dir -type d -maxdepth 1 2>/dev/null); do

	if [[ $j =~ .*$dir_rand_prefix.* ]] ; then

		cnt=$(ls -la "$j" | wc -l | sed 's/ //g')
		mv "$j" "$j-$cnt"

	fi

done