#!/usr/bin/python

## Author Joanna Garefalaki ##

## This script takes as input 2 csvfiles containing a list of chromosomes and positions, 
## it parses them and creates a window of 500000 base pairs around the polymorphic loci. 
## As output it creates a list of grid files which can be used as input for SweeD. 
## 101 points will be analyzed, with a distance of 5000bp with the polymorphic loci as the middle point  

import csv
from os import system
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest = "file", help = "add chromosome file", metavar='FILE')
parser.add_option("-w", "--file2", dest = "file2", help = "add positions file", metavar='FILE')
(options, args) = parser.parse_args()
chromos = options.file
posit = options.file2

def read_file(filename):
        with open(filename) as f:
                content = f.readlines()
        content = [x.strip() for x in content]
        return content

chromosomes = read_file(chromos)
positions = read_file(posit)

Sweedrun = 'python GridFileCreator.py '
c = ' -c '
s = ' -s '
e = ' -e '
d = ' -d 5000'
start = [] 
end = []
del_indexes = list()
for x in positions:
        if int(x) <= 250000:
                del_index = positions.index(x)
                del_indexes.append(del_index)
        
counter = 0
new_positions = list()
new_chromosomes = list()
for x in range(len(positions)):
	if x in del_indexes:
		continue
	else:
		new_positions.append(positions[x])
		new_chromosomes.append(chromosomes[counter])
	counter = counter + 1

for g in new_positions:
        if int(g) > 250000:   
                end.append(int(g) + 250000)
                k = int(g) - 250000
                if k < 0:
                        k = 0
                start.append(k)
       
with open('CleanChrs.csv', 'wb') as output:
        writer = csv.writer(output)
        for val in new_chromosomes:
                writer.writerow([val])
with open('CleanPos.csv', 'wb') as posit:
        writerCHR = csv.writer(posit)
        for value in new_positions:
                writerCHR.writerow([value])
 
counter=0
for h in new_chromosomes:
        print(Sweedrun + c + str(h) + s + str(start[counter]) + e + str(end[counter]) + d)
        counter = counter + 1  

      
#for i  in range(len(clean_chrs)):
                ##system(Sweedrun + c + str(nchrom[i]) + s + str(nstart[i]) + e + str(nend[i]) + d)
 #       print(Sweedrun + c + str(clean_chrs[i]) + s + str(start[i]) + e + str(end[i]) + d)
            

#python GridFileCreator.py -c 19 -s 21591536 -e 22091536 -d 5000










