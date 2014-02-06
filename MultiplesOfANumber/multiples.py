import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		split = line.split(',')
		x = int(split[0])
		n = int(split[1].strip())
		out = n
		while out < x:
			out += n
		print out
