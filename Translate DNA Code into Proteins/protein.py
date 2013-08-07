def translate(RNA_file):
    
    f = open(RNA_file, 'r').read()
    data= """UUU F      CUU L      AUU I      GUU V
            UUC F      CUC L      AUC I      GUC V
            UUA L      CUA L      AUA I      GUA V
			UUG L      CUG L      AUG M      GUG V
			UCU S      CCU P      ACU T      GCU A
			UCC S      CCC P      ACC T      GCC A
			UCA S      CCA P      ACA T      GCA A
			UCG S      CCG P      ACG T      GCG A
			UAU Y      CAU H      AAU N      GAU D
			UAC Y      CAC H      AAC N      GAC D
			UAA Stop   CAA Q      AAA K      GAA E
			UAG Stop   CAG Q      AAG K      GAG E
			UGU C      CGU R      AGU S      GGU G
			UGC C      CGC R      AGC S      GGC G
			UGA Stop   CGA R      AGA R      GGA G
			UGG W      CGG R      AGG R      GGG G""".split()
	
	data_dict =  dict(zip(data[0::2], data[1::2])) 
    codon =""
    aminoacids =''
	
    for i in range(f.__len__()):
        
        codon = codon + f[i]  #Builds the codon
        
        if codon.__len__()== 3: #As soon as the codon is built, the if-block executes
            if data_dict[codon]=='Stop':
				#Stops looping if the 'Stop' aminoacid is found
                break
            else:
                aminoacids = aminoacids + data_dict[codon] 
                codon = ''
    print aminoacids
#-------------------------------------------------------------------------------
import sys
	
try:
	translate(sys.ARGV[1])
except:
	print "\nUsage: python protein.py <Enter name of file containing RNA here>"    
    