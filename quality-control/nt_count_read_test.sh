#!/bin/bash

parallel "echo {}; gunzip -c {} | wc -l" ::: *.gz
