import sys

#line generator
def FileParse(filepath):
    with open(filepath, 'r') as f:
        for line in f:
        	yield line
					
#reverse
for line in FileParse(sys.argv[1]):
	c = line.split()
	
	#int(c[-1]) contains m
	#
	if int(c[-1].strip())+1 <= len(c) : print(c[-(int(c[-1].strip())+1)])
