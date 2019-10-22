#!/usr/bin/python3
## <><><>< Author Joanna Garefalaki ><><><>
## This script opens a manifest list file and creates links ready for download
## Example: wget https://3kricegenome.s3.amazonaws.com/Nipponbare/IRIS_313-10294.realigned.bam
## There are manifest files in each resource : AWS - https://3kricegenome.s3.amazonaws.com/MANIFEST
## and ASTI - https://anonymous:anonymous@irods-webdav.asti.dost.gov.ph/pub/3kRG/nipponbare/nipponbarebam_manifest.txt

from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-m", "--manifest", dest = "manifest", help = "add manifest file", metavar='FILE')
(options, args) = parser.parse_args()
manifest_file = options.manifest

bulklist = open(manifest_file)
link ='https://anonymous:anonymous@irods-webdav.asti.dost.gov.ph/pub/'
for i in bulklist:
	i=link+i
	listhttp=[]
	listhttp.append(i)
	with open('readymanifest.txt', 'a') as output:	
		for u in listhttp:
			output.write("%s" % u)
