#!/usr/bin/env bash
if [ $# != 1 ]; then
	echo "USAGE: ./wakatime_visualize.sh <input(json)>"
	exit 1
fi

input_name=$1
temp_csv="temp_csv.csv"

echo $temp_csv | wakadump --input $input_name --output csv

python3 visualize.py $temp_csv
rm $temp_csv
