#!/bin/bash

for i in sequences/*.fastq.gz; do 
	echo $i; gunzip -c -f $i | awk 'END {print NR/4}'; 
done
