import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.strip()
		sumof = 0
		for char in line:
			sumof += int(char)
		print(sumof)
