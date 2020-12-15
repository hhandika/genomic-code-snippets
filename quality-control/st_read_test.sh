#!/bin/bash

for i in *.gz; do 
	echo $i;(zcat $i | wc -l)/4 
done
