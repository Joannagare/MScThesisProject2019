#!/usr/bin/python3
## Author Joanna Garefalaki ##

## In order to run SweeDCMDcreator, this script creates tab-delimited file
## with 5 fixed fields per line. Fixed fields are:
## chr - an identifier to the chromosome to be scanned
## position - which defines the position on the chromosome to be scanned
## input data filepath - the path to the vcf/bam file, that is going to be used for applying SweeD.
## grid list filepath - the path to the file containing the grid points
## samplelist filepath - the path to the file containing the samples' list     

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest = "file", help = "add 00 names file", metavar='FILE')
parser.add_option("-w", "--file11", dest = "file11", help = "add 11 names file", metavar='FILE')
parser.add_option("-v", "--vcfiles", dest = "vcfiles", help = "add vcf file", metavar='FILE')
parser.add_option("-a", "--vcfpath", dest = "vcfpath", help = "add vcf path file", metavar='FILE')
parser.add_option("-b", "--filepath", dest = "filepath", help = "add 00 names file", metavar='FILE')
parser.add_option("-c", "--wilepath", dest = "wilepath", help = "add 11 names file", metavar='FILE')
parser.add_option("-s", "--sativa", dest = "sativa", help = "add Osativa chrom file", metavar='FILE')

(options, args) = parser.parse_args()

names00 = options.file
names11 = options.file11
vcfile = options.vcfiles
vcfpathfile = options.vcfpath
zeropath = options.filepath
onepath = options.wilepath
osativa = options.sativa

def read_file(filename):
        with open(filename) as f:
                content = f.readlines()
        content = [x.strip() for x in content]
        return content

def listToStringWithoutBrackets(list1):
        return str(list1).replace('[','').replace(']','').replace("'","")

NameListToExportNames00 = read_file(names00)
NameListToExportNames11 = read_file(names11)
parsechrs =read_file(vcfile)
directory = read_file(vcfpathfile)
samplelistdir00 = read_file(zeropath)
samplelistdir11 = read_file(onepath)
twelve = read_file(osativa)
vcf = '.vcf'
SampleSplitted = []
finallist = []
chromosomes = []
positions =[]

for j00 in NameListToExportNames00:
       SampleSplitted.append( j00.split('.'))
        
for o00 in SampleSplitted:
       chromosomes.append(o00[2])
       positions.append(o00[3])

for k in twelve:
        finallist.append(listToStringWithoutBrackets(directory)+k+vcf)
print(finallist)
with open('newout00.list', 'w') as output:
        for q in finallist:
                for i in range(len(chromosomes)):
                        output.write(str(chromosomes[i])+"\t"+str(positions[i])+"\t"+q+"\t"+listToStringWithoutBrackets(samplelistdir00)+NameListToExportNames00[i]+"\n")
#.join(str(j).join("\t".join.vcf.join("\t",grid,"\t",sample,"\n"    \n")     

with open('newout11.list', 'w') as output:
        for a in finallist:   
                for u in range(len(chromosomes)):
                        output.write(str(chromosomes[u])+"\t"+str(positions[u])+"\t"+a+"\t"+listToStringWithoutBrackets(samplelistdir11)+NameListToExportNames11[u]+"\n")
