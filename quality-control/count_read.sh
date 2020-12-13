#!/bin/bash

parallel "echo {}; zcat {} | awk 'END {print NR/4}';" ::: sequences/*.gz
