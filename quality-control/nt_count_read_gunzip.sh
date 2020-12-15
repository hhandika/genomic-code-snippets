#!/bin/bash

parallel "echo {}; gunzip -c {} | wc -l/4" ::: sequences/*.gz
