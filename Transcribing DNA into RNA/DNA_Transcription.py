def toRNA(DNA_file):
	import string
    
    line = open(DNA_file, 'r').read()
    line = string.replace(line,'T','U')
    print line

#----------------------------------------
import sys

try:
	toRNA(sys.ARGV[1])
except:
	print "Usage: python DNA_Transcription.py <Insert name of file containing DNA string here>"