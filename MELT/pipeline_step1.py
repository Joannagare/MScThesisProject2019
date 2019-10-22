#!/usr/bin/python 

# step1: Download from http://snp-seek.irri.org/_download.zul

from os import system
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Provide input file")
parser.add_argument("-k", help="Provide an index")
args = parser.parse_args()

index = args.k

D = args.i
time = 'time '
A = 'wget '
B = '--no-check-certificate ' 
C = '-i '
#D = 'first100random.txt '
#D = '2_1random_SORTED.txt '
osfrasi= time + A + B + C + D

system(osfrasi)

#step2: function to open files stripping blanks and return it as a list, I call it later with my list = read_file(myfile)

def read_file(filename):
	with open(filename) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	return content

# rep bam$ 2_1random_SORTED.txt  | sed 's/https.*\///'
#step3: save to file to use for preprocess:
##A0 = 'ls -d -1 $PWD/*.bam > forpreprocess.txt '
A0 = 'grep bam$ ' + D + ' | sed \'s/https.*\///\' ' + ' > forpreprocess.' + index + '.txt'
print(A0)

print("Running Grep Command")

system(A0)

print("Ran Grep Command")

#step4: create a list with paths for bamfiles to use in preprocess
bamlistfilename = 'forpreprocess.'+index+'.txt'
bamlist = read_file(bamlistfilename)

#step5: Preprocess of bam files with MELT
preprocess = 'java -Xmx2G -jar /home/pavlos/synology/joanna/MscThesis/software/MELTv2.1.5/MELT.jar Preprocess'
bamfile = ' -bamfile $PWD/'
reference = ' -h /home/pavlos/synology/joanna/MscThesis/DATA/FASTA/IRGSP-1.0_genome.fasta '
for i in bamlist:
	bam = i
	print(preprocess + bamfile + bam + reference) #to see spaces
	system(preprocess + bamfile + bam + reference)

#step 6: run MELT-split
#IndivAnalysis
inidanalysis = 'java -Xmx6G -jar /home/pavlos/synology/joanna/MscThesis/software/MELTv2.1.5/MELT.jar IndivAnalysis -w /home/pavlos/synology/joanna/MscThesis/CODE/MELT/meltsplit/mPingElement -c 14 -h /home/pavlos/synology/joanna/MscThesis/DATA/FASTA/IRGSP-1.0_genome.fasta -t /home/joanna/synology/joanna/MscThesis/ZipTransposon/mPing/mPingElement_MELT.zip'
for i in bamlist:
	print(inidanalysis + bamfile + i)
	system(inidanalysis + bamfile + i)

system('cd /home/pavlos/synology/joanna/MscThesis/RESULTS/ResultsFromMELT/ mkdir MeltStep1Results mv 
