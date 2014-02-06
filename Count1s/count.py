import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		binary = str(bin(int(line.strip())))[2:]
		print str.count(binary, '1')


	
