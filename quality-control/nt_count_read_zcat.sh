#!/bin/bash

parallel "echo {}; gunzip -c {} | awk 'END {print NR/4}';" ::: sequences/*.gz
