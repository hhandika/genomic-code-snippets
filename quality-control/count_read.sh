for i in sequences/*R1_001.fastq.gz; do echo $i; gunzip -c -f $i | awk 'END {print NR/4}'; done
