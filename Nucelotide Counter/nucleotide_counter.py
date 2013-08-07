try:
	DNA = open(sys.argv[1],'r').read()
	print DNA.count('A'), DNA.count('T'), DNA.count('G'), DNA.count('C')
except:
	print "Usage: python nucleotide_counter.py <Enter name of file containing DNA string here>"