import sys

#line generator
def FileParse(filepath):
    with open(filepath, 'r') as f:
        for line in f:
        	yield line
					
#reverse
for line in FileParse(sys.argv[1]):
	c = line.split()
	for i in range(len(c)):
		print(c[len(c) - i - 1]),
	print
