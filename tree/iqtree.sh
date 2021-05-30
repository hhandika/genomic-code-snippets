#!/bin/bash

ALIGNMENT=$1

iqtree2 -s $ALIGNMENT -T AUTO --prefix $ALIGNMENT
