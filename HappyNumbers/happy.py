import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.strip()
		count = 0
		while count < 50:
			sumof = 0
			for c in line:
				sumof += int(c) * int(c)
			if sumof == 1:
				print(1)
				break
			line = str(sumof)
			count += 1
		if count == 50: print(0)
