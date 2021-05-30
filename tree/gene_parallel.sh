#!/bin/bash

parallel "echo {}; iqtree2 -s {} --prefix concat_bash -T AUTO" ::: loci/*.nexus
