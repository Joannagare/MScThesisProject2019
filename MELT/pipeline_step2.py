#!/usr/bin/python

from os import system

def read_file(filename):
	with open(filename) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	return content

#step3: save to file to use for preprocess:

bamlist = read_file("forpreprocess.txt")
bamfile = ' -bamfile $PWD/'

#GroupAnalysis
groupanalysis = 'java -Xmx6G -jar /home/joanna/synology/joanna/MscThesis/software/MELTv2.1.5/MELT.jar GroupAnalysis -w /home/joanna/synology/joanna/MscThesis/meltsplit  -discoverydir /home/joanna/synology/joanna/MscThesis/meltsplit/mPingElement -h /home/joanna/synology/joanna/MscThesis/ZipTransposon/IRGSP-1.0_genome.fasta -t /home/joanna/synology/joanna/MscThesis/ZipTransposon/mPing/mPingElement_MELT.zip -n /home/joanna/synology/joanna/MscThesis/meltsplit/bed.txt'
#system(groupanalysis)

#Genotype 
genotype = 'java -Xmx2G -jar /home/joanna/synology/joanna/MscThesis/software/MELTv2.1.5/MELT.jar Genotype'
part3 = ' -w /home/joanna/synology/joanna/MscThesis/meltsplit -p /home/joanna/synology/joanna/MscThesis/meltsplit -h /home/joanna/synology/joanna/MscThesis/ZipTransposon/IRGSP-1.0_genome.fasta -t /home/joanna/synology/joanna/MscThesis/ZipTransposon/mPing/mPingElement_MELT.zip' 
from os import path

#print(path.isdir(pwd + i))
#print(path.exists("/home/el/myfile.txt"))
for i in bamlist:
     directory = '/home/joanna/synology/joanna/MscThesis/meltsplit/' + i
        if path.exists(directory): 
                system(genotype + bamfile + i + part3)

from os import listdir, stat

files=listdir('/home/joanna/synology/joanna/MscThesis/meltsplit/')
for i in range(len(files)):
        if stat(files[i]).st_size==0:
                system('rm ' + files[i])
                print(files[i])
                
#makeVCF

makeVCF = 'java -Xmx2G -jar /home/joanna/MscThesis/software/MELTv2.1.5/MELT.jar MakeVCF -genotypingdir /home/joanna/MscThesis/meltsplit -w /home/joanna/synology/joanna/MscThesis/meltsplit -h /home/joanna/MscThesis/ZipTransposon/IRGSP-1.0_genome.fasta -t /home/joanna/MscThesis/ZipTransposon/mPing/mPingElement_MELT.zip -p /home/joanna/synology/joanna/MscThesis/meltsplit -o ./'
system(makeVCF)

