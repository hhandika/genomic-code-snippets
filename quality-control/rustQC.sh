#!/bin/bash

parallel "echo {} | realFastQC -i {}" ::: *.gz