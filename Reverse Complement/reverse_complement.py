def rComplement(DNA_file):
	DNA = list(open(DNA_file, 'r').read()).reverse()
	reference = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
	DNA_complement = []
	for nucelotide in DNA:
		DNA_complement.append(reference[nucleotide])
		
	print " ".join(DNA_complement)
#-----------------------------------------
import sys

try:
	rComplement(sys.argv[1])
except:
	print "\nUsage: python reverse_complement.py <Enter name of file containing DNA string here>"