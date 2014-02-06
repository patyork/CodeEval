import sys

#line generator
def FileParse(filepath):
    with open(filepath, 'r') as f:
        for line in f:
        	yield int(line.strip())
					
#reverse
output = 0
for num in FileParse(sys.argv[1]):
	output += num
print(output)
