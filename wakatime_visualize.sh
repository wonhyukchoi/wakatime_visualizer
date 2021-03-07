#!/usr/bin/env bash
if [ $# != 2 ]; then
	echo "USAGE: ./wakatime_visualize.sh <input(json)> <output(csv)>"
	exit 1
fi

input_name=$1
output_name=$2

output_name | wakadump --input input_name --output csv

python3 visualize.py output_name
