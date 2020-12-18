# genomic-code-snippets
This repo contains random code snippets I wrote to process high-throughput sequencing data. 

## Usage

### Pre-Sequencing
Currently, it contains python script to match iTru well index with iTru sequences. It will save time than doing it manually and can prevent copy-pasting mistakes. The easiest way to run the code is to match the file names of your files with the filenames in the sample data provided in the directory of the script. Then, you can run the code like you run any python script.

### Quality-Control
This directory contains multiple bash files to quickly check sequencing read. I recommend using the nt_count_read_zcat.sh. The script only work on Linux or MacOS.

Check if you have GNU Parallel installed in your system. This command below should shows the program version. 

```
parallel --version
```

If you don't have GNU parallel installed, it will show command not found error. Install it using the command below. Choose based on your operating system.

```
# Ubuntu
sudo apt install parallel

# OpenSuse
sudo zypper in parallel

# Fedora
sudo dnf in parallel

# On MacOS use homebrew. 
brew install parallel

```

You can run the script from the directory of your fastaq.gz files or copy it to your path variable and then call it from your fastaq directories. 

## The State of the Code
All the code here is experimental. In some cases, it can appears in multiple implimentation for doing the same thing. I use them to find the most efficient code for the problem. 
