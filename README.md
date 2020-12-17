# genomic-code-snippets
This repo contain random code snippets I wrote to process high-throughput sequencing data. 

## Usage

### Pre-Sequencing
Currently, it contains python script to match iTru well index with iTru sequences. It will save time than doing it manually and can prevent copy-pasting mistakes. The easiest way to run the code is to match the file names of your files with the filenames in the sample data provided in the directory of the script. Then, you can run the code like you run any python script.

### Quality-Control
This directory contains multiple bash files to quickly check sequencing read. The 'nt_count_read_gunzip.sh' is the fastest code in my test. It is multithreaded using GNU parallel. You will need to install GNU parallel do use it. 
