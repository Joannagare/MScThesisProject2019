#!/bin/bash

## Author Joanna Garefalaki ##

## This script prepares the MELT output for GridFileCreator.py 
## Input: vcf output from MELT
## Output: 1 vcf file with the same names as the 3kSNP.vcf, only polymorphic > 10 loci
## Output: 3 csv files with the first columns from the edited vcf
## Output: files with a list of grid points

grep '^\#' mPingElement.final_comp.vcf > mPingElement.final_comp_pass.vcf
grep 'PASS' mPingElement.final_comp.vcf >> mPingElement.final_comp_pass.vcf 
sed 's/.realigned//g' mPingElement.final_comp_pass.vcf | sed 's/01_Nipponbare_//g' > mPing_Pass_Right_Names.vcf
# select >10 threshold 
#python /home/pavlos/synology/joanna/MscThesis/SweeD/DoubleTheNames.py 
python VCFilterbySampleQuan.py -v mPing_PASS_Right_Names.vcf -t 10 

grep -v '^\#' mPing_PASS_Right_Names.filtered.vcf | cut -f 1,2 | awk '{gsub(/\chr/,"")}1' > Column_1_2_from_mPing_PASS_Right_Names.csv # create a list of chromosomes with their positions

awk '{ print $1 }' Column_1_2_from_mPing_PASS_Right_Names.csv > Column_1_from_mPing_PASS_Right_Names.csv   # split to use later                                                    

awk '{ print $2 }' Column_1_2_from_mPing_PASS_Right_Names.csv > Column_2_from_mPing_PASS_Right_Names.csv   # split to use later

python PrepareForGridFileCreator.py # create window and call grid creator

mkdir -p GridListFrom_MELT

mv points* GridListFrom_MELT
