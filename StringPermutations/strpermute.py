import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		chars = list(line.strip())
		out = []
		for i in range(0, len(chars)):
			
