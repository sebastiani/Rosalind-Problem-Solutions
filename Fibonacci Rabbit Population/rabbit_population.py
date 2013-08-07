def fibonacci(n,k):
    
    if n <2:
        return n
    else:
        return fibonacci(n-1,k) + k*fibonacci(n-2,k)

#-------------------------------------------------------
import sys

try:
	print fibonacci(sys.argv[1],sys.argv[2])
except:
	print "\nUsage: python rabbit_population.py <enter n> <enter k>
	
    




