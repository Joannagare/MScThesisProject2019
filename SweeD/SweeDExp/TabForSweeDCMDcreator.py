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
parser.add_option("-g", "--grid", dest = "gridfile", help = "add grid file", metavar='FILE')
parser.add_option("-v", "--vcfiles", dest = "vcfiles", help = "add vcf file", metavar='FILE')
parser.add_option("-a", "--vcfpath", dest = "vcfpath", help = "add vcf path file", metavar='FILE')
parser.add_option("-b", "--filepath", dest = "filepath", help = "add 00 names file", metavar='FILE')
parser.add_option("-c", "--wilepath", dest = "wilepath", help = "add 11 names file", metavar='FILE')
parser.add_option("-d", "--gridpath", dest = "gridpath", help = "add grid path file", metavar='FILE')

(options, args) = parser.parse_args()

names00 = options.file
names11 = options.file11
gridf= options.gridfile
vcfile = options.vcfiles
vcfpathfile = options.vcfpath
zeropath = options.filepath
onepath = options.wilepath
gridfilepath = options.gridpath

def read_file(filename):
        with open(filename) as f:
                content = f.readlines()
        content = [x.strip() for x in content]
        return content

def listToStringWithoutBrackets(list1):
        return str(list1).replace('[','').replace(']','').replace("'","")

NameListToExportNames00 = read_file(names00)
NameListToExportNames11 = read_file(names11)
grid= read_file(gridf)
parsechrs =read_file(vcfile)
directory = read_file(vcfpathfile)
gridpath = read_file(gridfilepath) 
samplelistdir00 = read_file(zeropath)
samplelistdir11 = read_file(onepath)

vcf = '.vcf'
chromosomes11= []
positions11 = []
SampleSplitted = []
finallist = []
chromosomes = []
positions =[]

for j00 in NameListToExportNames00:
       SampleSplitted.append( j00.split('.'))
        
for o00 in SampleSplitted:
       chromosomes.append(o00[2])
       positions.append(o00[3])

for k in chromosomes:
        finallist.append(listToStringWithoutBrackets(directory)+k+vcf)
        print(k, str(listToStringWithoutBrackets(directory)+k+vcf), listToStringWithoutBrackets(directory)+k+vcf)

with open('newfile00.list', 'w') as output:
        for i in range(len(positions)):
                ##print(chromosomes[i], listToStringWithoutBrackets(gridpath), grid[i])
                output.write(str(chromosomes[i])+"\t"+str(positions[i])+"\t"+str(finallist[i])+"\t"+listToStringWithoutBrackets(gridpath)+str(grid[i])+"\t"+listToStringWithoutBrackets(samplelistdir00)+str(NameListToExportNames00[i])+"\n")

#.join(str(j).join("\t".join.vcf.join("\t",grid,"\t",sample,"\n"    \n")     
with open('newfile11.list', 'w') as output:
      for u in range(len(positions)):
               output.write(str(chromosomes[u])+"\t"+str(positions[u])+"\t"+str(finallist[u])+"\t"+listToStringWithoutBrackets(gridpath)+str(grid[u])+"\t"+listToStringWithoutBrackets(samplelistdir11)+str(NameListToExportNames11[u])+"\n")
