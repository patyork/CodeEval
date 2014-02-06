import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		split = line.strip().split(',')
		n = int(split[0])
		m = int(split[1])
		while n >= m:
			n -= m
		print n
		
