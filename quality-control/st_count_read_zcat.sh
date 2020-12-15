#!/bin/bash

for i in sequences/*.fastq.gz; do 
	echo $i; zcat $i | awk 'END {print NR/4}'; 
done
