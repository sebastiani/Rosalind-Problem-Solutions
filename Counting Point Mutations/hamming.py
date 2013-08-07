def hammingDist(DNA_file):
    
    adn = open('rosalind_hamm.txt', 'r').read().split()
    
    count =0
    for i in range(adn[0].__len__()):
        if adn[0][i] != adn[1][i]:
            count +=1
            
    print count
#---------------------------------------------------------------
import sys

try:
	hammingDist(sys.argv[1])
except:
	print "\nUsage: python hamming.py <name of file here>"