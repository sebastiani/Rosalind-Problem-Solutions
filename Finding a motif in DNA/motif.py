def findMotif(DNA_file, motif):
	DNA = open(DNA_file, 'r').read()
	for i in range(DNA.__len__()):
		if DNA.startswith(motif,i):
			print i+1
#----------------------------------------

import sys

try:
	findMotif(sys.argv[1], sys.argv[2])
except:
	print "\nUsage: python motif.py <Name of file> <motif string>\n"