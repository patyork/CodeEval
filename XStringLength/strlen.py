import sys
					
#reverse
output = []
firstLine = True
printX = 0
for line in open(sys.argv[1], 'r'):
	if firstLine:
		printX = int(line)
		firstLine = False
		continue
		
	output.append(line)
	
output.sort(key = len)

for i in range(printX):
	print output[-(i+1)],
