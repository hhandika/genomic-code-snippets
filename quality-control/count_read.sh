#!/bin/bash

parallel --result read_counts.csv "echo {}; zcat {} | awk 'END {print NR/4}';" ::: *.gz
